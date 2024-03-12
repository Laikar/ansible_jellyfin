#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
from typing import List
__metaclass__ = type

#!TODO: Update documentation string 
DOCUMENTATION = r'''
---
module: config_info

short_description: This module performs the initial setup on a jellyfin server

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "0.1"

description: This is my longer description explaining my test module.

options:

# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
# extends_documentation_fragment:
#     - my_namespace.my_collection.my_doc_fragment_name

author:
    - David "Laikar" Bañón Gil (@Laikar)
'''
#!TODO: Update example ussages
EXAMPLES = r'''
# Bare minimum
- name: Setup Jellyfin
  laikar.jellyfin.setup:
    jellyfin_url: "http://localhost:8096"
    admin_user: admin
    admin_password: admin123

# pass in a message and have changed true
- name: Test with a message and changed output
  my_namespace.my_collection.my_test:
    name: hello world
    new: true

# fail the module
- name: Test failure of the module
  my_namespace.my_collection.my_test:
    name: fail me
'''
#!TODO: Update return values
RETURN = r'''
'''

from result import Result, Ok, Err
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.laikar.jellyfin.plugins.module_utils.common import KeyClient, UserPassClient


from ansible_collections.laikar.jellyfin.plugins.module_utils.jellyfin_api_client.api.configuration import get_configuration

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        jellyfin_url = dict(type='str', required=True),
        admin_user = dict(type='str'),
        admin_password = dict(type='str'),
        api_key  = dict(type='str'),

        device_name = dict(type='str', required=False, default="Ansible Controller"),
        client_name = dict(type='str', required=False, default="Ansible Client"),
        device_id = dict(type='str', required=False, default="Ansible Client ID"),
        client_version = dict(type='str', required=False, default="10.8.13"),

    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        jellyfin_config={}
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        required_one_of=[
            ('api_key', 'admin_user'),
            ],
        required_by={
            'admin_user': 'admin_password',
        },
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    with KeyClient(base_url = module.params['jellyfin_url'], 
                client_name = module.params['client_name'],
                device_name = module.params['device_name'],
                device_id = module.params['device_id'],
                version = module.params['client_version'],
                key=module.params['api_key'])\
        if module.params['api_key'] else\
        UserPassClient(base_url = module.params['jellyfin_url'], 
                        client_name = module.params['client_name'],
                        device_name = module.params['device_name'],
                        device_id = module.params['device_id'],
                        version = module.params['client_version'],
                        username=module.params['admin_user'],
                        password=module.params['admin_password']) as client:
        get_config_response = get_configuration.sync_detailed(client=client)
        match get_config_response.status_code:
            case 200:
                result['jellyfin_config'] = get_config_response.parsed.to_dict()
                result['changed'] = False
                module.exit_json(**result)
            case _:
                result['changed'] = False
                module.fail_json(msg='Unknown error', **result)



def main():
    run_module()


if __name__ == '__main__':
    main()