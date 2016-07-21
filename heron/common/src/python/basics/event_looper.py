# Copyright 2016 Twitter. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import time
import traceback
from heapq import heappush, heappop
from abc import abstractmethod
from heron.common.src.python.log import Log

import sys

class EventLooper(object):
  """Event Looper can block the thread on ``do_wait()`` and unblock on ``wake_up()``"""
  def __init__(self):
    self.should_exit = False
    self.wakeup_tasks = []
    self.timer_tasks = []
    self.exit_tasks = []

  def loop(self):
    while not self.should_exit:
      self.run_once()

    self.on_exit()

  def run_once(self):
    try:
      self.do_wait()
      self.execute_wakeup_tasks()
      self.trigger_timers()
    except Exception as e:
      Log.error("Error occured during run_once(): " + e.message)
      Log.error(traceback.format_exc())
      self.should_exit = True

  def on_exit(self):
    Log.info("In on_exit() of event_looper")
    for task in self.exit_tasks:
      task()

  @abstractmethod
  def do_wait(self):
    pass

  @abstractmethod
  def wake_up(self):
    pass

  def add_wakeup_task(self, task):
    self.wakeup_tasks.append(task)
    # make sure to run this at least once
    self.wake_up()

  def add_exit_task(self, task):
    self.exit_tasks.append(task)

  def register_timer_task_in_sec(self, task, second):
    # Python time is in float
    second_in_float = float(second)
    expiration = time.time() + second_in_float
    heappush(self.timer_tasks, (expiration, task))

  def exit_loop(self):
    self.should_exit = True
    self.wake_up()

  def get_next_timeout_interval(self):
    """Get the next timeout from now

    This should be used from do_wait().
    :returns (float) next_timeout, or 10.0 if there are no timer events
    """
    if len(self.timer_tasks) == 0:
      return sys.maxint
    else:
      next_timeout_interval = self.timer_tasks[0][0] - time.time()
      return next_timeout_interval

  def execute_wakeup_tasks(self):
    # Check the length of wakeup tasks first to avoid concurrent issues
    size = len(self.wakeup_tasks)
    for i in range(size):
      self.wakeup_tasks[i]()

  def trigger_timers(self):
    current = time.time()
    while len(self.timer_tasks) > 0 and (self.timer_tasks[0][0] - current <= 0):
      task = heappop(self.timer_tasks)[1]
      task()

