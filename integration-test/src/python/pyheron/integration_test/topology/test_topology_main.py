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
'''main method for integration test topology'''

import sys

from .basic_one_task import basic_one_task_builder

TOPOLOGY_BUILDERS = {'PyHeron_IntegrationTest_BasicOneTask': basic_one_task_builder}

def main():
  if len(sys.argv) != 3:
    print "Usage: %s <http server url> <topology name>" % sys.argv[0]
    sys.exit(1)

  http_server_url = sys.argv[1]
  topology_name = sys.argv[2]

  if topology_name not in TOPOLOGY_BUILDERS:
    print "%s not found in the list" % topology_name
    sys.exit(2)

  builder = TOPOLOGY_BUILDERS[topology_name]
  topo_class = builder(http_server_url)
  topo_class.write()

if __name__ == '__main__':
  main()
