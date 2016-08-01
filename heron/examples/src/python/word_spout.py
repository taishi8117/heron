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

from itertools import cycle
from heron.instance.src.python.basics import Spout, Stream

class WordSpout(Spout):
  outputs = ['word', Stream(fields=['error_msg'], name='error')]

  def initialize(self, config, context):
    self.logger.info("In initialize() of WordSpout")
    self.words = cycle(["hello", "bye", "good", "bad", "heron", "storm"])
    self.emit_count = 0
    self.logger.debug("Spout context: \n" + str(context))
    self.ack_count = 0
    self.fail_count = 0
    self.logger.info("Given component-specific config: \n" + str(config))

  def next_tuple(self):
    word = next(self.words)
    self.emit([word], tup_id='message id')
    self.emit_count += 1
    if self.emit_count % 100000 == 0:
      self.logger.info("Emitted " + str(self.emit_count))
      self.emit(["test error"], tup_id='error id', stream='error')

  def ack(self, tup_id):
    self.ack_count += 1
    if self.ack_count % 10000 == 0:
      self.logger.info("Acked " + str(self.ack_count))

  def fail(self, tup_id):
    self.fail_count += 1
    if self.fail_count % 10000 == 0:
      self.logger.info("Failed " + str(self.fail_count))
