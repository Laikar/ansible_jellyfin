#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
import imp
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
from ansible_collections.laikar.jellyfin.plugins.module_utils.common import KeyClient, UserPassClient, auth_module_args, connection_module_args
from ansible_collections.laikar.jellyfin.plugins.module_utils.api_keys import get_api_keys

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(

    )
    module_args.update(connection_module_args)
    module_args.update(auth_module_args)

    module = AnsibleModule(
        argument_spec=module_args,
        required_one_of=[
            ('api_key', 'admin_user'),
            ],
        required_by={
            'admin_user': 'admin_password',
        },
    )

    result = dict(
        changed=False,
        api_keys={}
    )

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
        query_result= get_api_keys(client=client)
        match query_result:
            case Ok(keys):
                result['api_keys'] = keys
                result['changed'] = False
                module.exit_json(**result)
            case Err(e):
                result['changed'] = False
                module.fail_json(msg=e, **result)




def main():
    run_module()


if __name__ == '__main__':
    main()