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
'''bolt.py: API for defining bolt in python'''
from abc import abstractmethod
from .base_bolt import BaseBolt

class Bolt(BaseBolt):
  """API for defining a bolt for Heron in Python"""

  @abstractmethod
  def initialize(self, config, context):
    """Called when a task for this component is initialized within a worker on the cluster

    It is compatible with StreamParse API.
    (Parameter name changed from ``storm_conf`` to ``config``)

    It provides the bolt with the environment in which the bolt executes. Note that
    you should NOT override ``__init__()`` for initialization of your bolt, as it is
    used internally by Heron Instance; instead, you should use this method to initialize
    any custom instance variables or connections to databases.

    *Should be implemented by a subclass.*

    :type config: dict
    :param config: The Heron configuration for this bolt. This is the configuration provided to
                   the topology merged in with cluster configuration on this machine.
                   Note that types of string values in the config have been automatically converted,
                   meaning that number strings and boolean strings are converted to appropriate
                   types.
    :type context: dict
    :param context: This object can be used to get information about this task's place within the
                    topology, including the task id and component id of this task, input and output
                    information, etc.
    """
    pass

  @abstractmethod
  def process(self, tup):
    """Process a single tuple of input

    The Tuple object contains metadata on it about which component/stream/task it came from.
    To emit a tuple, call ``self.emit(tuple)``.

    **Must be implemented by a subclass, otherwise NotImplementedError is raised.**

    :type tup: heron.common.src.python.utils.tuple.HeronTuple
    :param tup: HeronTuple to process
    """
    raise NotImplementedError("Bolt not implementing process() method.")
