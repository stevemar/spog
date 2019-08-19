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

import random
import yaml

BUG_SEVERITY = ['critical', 'high', 'medium', 'low']
BUG_USERNAMES = ['dolphm', 'stevemar', 'cmurphy', 'mdrnstm', 'jheck', 'lbragtad']
BUG_DESCRIPTIONS = [
    'cannot use trusts with federated users',
    'Keystone ldap tree_dn does not support Chinese',
    'The v3 grant API should account for different scopes',
    'The ec2 credential API should account for different scopes',
    'Unable to remove an assignment from domain and project',
    'Documentation builds failing with Sphinx 1.7.5',
    'The v3 role API should account for different scopes',
    '[rfe] Renewable Application Credentials',
    'Self-service policies for credential APIs are broken in stable/rocky',
    'Zero-downtime upgrades lead to spurious token validation failures when caching is enabled',
    'keystone (stein), python3, and postgresql: hex in database',
    'Logs filled with unnecessary policy deprecation warnings',
    'able to validate a Fernet token with garbage at the end (cryptography limitation)',
    'RFE: keystone-manage CLI to allow using syslog & specific log files',
    'oauth login silently ignores scope',
    'Forbid invalid operations in expand, migrate, and contract repositories',
    'policy.v3cloudsample.json does not allow domain admin list role assignments on project',
    'RFE: Whitelisting (opt-in) users/projects/domains for PCI compliance',
    'Moving/disabling LDAP users break Keystone queries depending on role ID',
    'Mapping a federated user to a local user does not return concrete role assignments',
    'Dependency between subsystems at the DB layer',
    'Create OAUTH request token gives 401 error when request url is admin endpoint',
    '/v3/users is unproportionally slow',
    'policy cloudsample checks on is_admin_project',
    'Lack of documentation for role inheritance',
    'system scope does not work for the service which use project specified endpoint',
    'keystone tests fail scope checking',
    'Upgrade procedure performance issues',
    'keystone-manage db_sync fails with MariaDB 10.3',
    'Lack of documentation for role permutations and possibilities',
    'LDAP backend should support python-ldap trace logging',
    'Enhance PCI-DSS compliance documentation',
    'User cannot list their own trusts',
    'keystone upgrade fails q->r oslo.log requirement to low',
    'Upgrade to Ocata: Keystone Intermittent Missing options Key',
    'Federation Protocol saml2 fails on Rocky',
    'Keystone as a SAML IdP does not work when mod_auth_mellon is used as the SP',
    'cache guide is out of date',
    'Policy names need to be updated for consistency'
]

# generate fake bug data
bugs_contents = []
for _ in range(random.randint(0, 100)):
    bug = {
        'number': random.randint(1, 1000),
        'title': random.choice(BUG_DESCRIPTIONS),
        'severity': random.choice(BUG_SEVERITY),
        'reporter': random.choice(BUG_USERNAMES),
        'assigned_to': random.choice(BUG_USERNAMES)
    }
    bugs_contents.append(bug)

# generate fake baseball stats data
stats_contents = []
for _ in range(random.randint(0, 100)):
    stat = {
        'average': random.randint(0, 100) / 100,
        'hits': random.randint(0, 80),
        'homers': random.randint(0, 30),
        'rbis': random.randint(0, 60)
    }
    stats_contents.append(stat)


# print both sets of data to YAML

with open('bugs.yaml', 'w+') as ff:
    yaml.dump(
        {'bugs': bugs_contents},
        ff,
        width=60,
        allow_unicode=True,
        default_flow_style=False)

with open('stats.yaml', 'w+') as ff:
    yaml.dump(
        {'stats': stats_contents},
        ff,
        width=60,
        allow_unicode=True,
        default_flow_style=False)


print('done generating YAML files')
