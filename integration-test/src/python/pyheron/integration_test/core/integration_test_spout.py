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
'''integration test spout'''

from heron.common.src.python.utils.log import Log
from heron.streamparse.src.python import Spout, Stream
from . import constants as integ_constants

class IntegrationTestSpout(Spout):
  # TODO: make sure this is added to topology
  outputs = [Stream(fields=[integ_constants.INTEGRATION_TEST_TERMINAL],
                    name=integ_constants.INTEGRATION_TEST_CONTROL_STREAM_ID)]

  def initialize(self, config, context):
    self.max_executions = integ_constants.MAX_EXECUTIONS
    assert self.max_executions > 0
    self.tuples_to_complete = 0

  @property
  def is_done(self):
    return self.max_executions <= 0

  def next_tuple(self):
    if self.is_done:
      return

    self.max_executions -= 1
    Log.info("max executions: %d" % self.max_executions)

    if self.is_done:
      self._emit_terminal_if_necessary()
      Log.info("This topology is finished.")

  def ack(self, tup_id):
    pass

  def fail(self, tup_id):
    pass

  def emit(self, tup, tup_id=None, stream=Stream.DEFAULT_STREAM_ID,
           direct_task=None, need_task_ids=False):
    self.tuples_to_complete += 1

    if tup_id is None:
      Log.info("Add tup_id for tuple: %s" % str(tup))
      _tup_id = integ_constants.INTEGRATION_TEST_MOCK_MESSAGE_ID
    else:
      _tup_id = tup_id

    super(IntegrationTestSpout, self).emit(tup, _tup_id, stream, direct_task, need_task_ids)
