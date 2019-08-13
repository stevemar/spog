# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import yaml

# TODO(stevemar): create more random data cause that's more fun.

# bug reports
bug = {
    'number': 6,
    'title': 'popen() breaks install',
    'description': 'longer description',
    'severity': 'high',
    'reporter': 'stevemar',
    'assigned_to': 'stevemar'
}

# baseball stats
stat = {
    'average': 0.450,
    'hits': 13,
    'homers': 4,
    'rbis': 15
}

bugs_contents = []
bugs_contents.append(bug)
stats_contents = []
stats_contents.append(stat)

with open('stats.yaml', 'w+') as ff:
    yaml.dump(
        {'stats': stats_contents},
        ff,
        width=60,
        allow_unicode=True,
        default_flow_style=False)

with open('bugs.yaml', 'w+') as ff:
    yaml.dump(
        {'bugs': bugs_contents},
        ff,
        width=60,
        allow_unicode=True,
        default_flow_style=False)

print('done generating YAML files')
