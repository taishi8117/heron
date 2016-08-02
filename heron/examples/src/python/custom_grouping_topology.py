# copyright 2016 twitter. all rights reserved.
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
'''module for example topology: CustomGroupingTopology'''

from heron.instance.src.python.basics import Topology, Bolt, Grouping
from heron.examples.src.python.word_spout import WordSpout
from heron.common.src.python.utils.topology import ICustomGrouping
from heron.common.src.python.log import Log

import heron.common.src.python.constants as constants

class SampleCustomGrouping(ICustomGrouping):
  def prepare(self, context, component, stream, target_tasks):
    Log.info("In prepare of SampleCustomGrouping, "
             "with src component: %s, "
             "with stream id: %s, "
             "with target tasks: %s"
             % (component, stream, str(target_tasks)))
    self.target_tasks = target_tasks

  def choose_tasks(self, values):
    # only emits to the first task id
    return [self.target_tasks[0]]

class ConsumeBolt(Bolt):
  def initialize(self, config, context):
    self.logger.info("In prepare() of ConsumerBolt")
    self.total = 0

  def process(self, tup):
    if self.is_tick():
      self.log("Got tick tuple!")
      self.log("Total received data tuple: %d" % self.total)
    else:
      self.total += 1

class CustomGrouping(Topology):
  custom_grouping = SampleCustomGrouping()

  word_spout = WordSpout(par=1)
  consume_bolt = ConsumeBolt(par=3,
                             inputs={word_spout: Grouping.custom(custom_grouping),
                                     word_spout['error']: Grouping.ALL},
                             config={constants.TOPOLOGY_TICK_TUPLE_FREQ_SECS: 10})
