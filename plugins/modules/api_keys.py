#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
from os import dup
from typing import Dict, List


from result import Result, UnwrapError

__metaclass__ = type

DOCUMENTATION = r'''
---
module: jellyfin_api_keys

short_description: This module performs the initial setup on a jellyfin server

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    jellyfin_url:
        description: the url used to connect to Jellyfin
        required: true
        type: str
    device_name:
        description: Device name for X-Emby-Authorization header
        required: false
        default: "Ansible Controller"
        type: str        
    client_name:
        description: Device name for X-Emby-Authorization header
        required: false
        default: "Ansible Client"
        type: str
     device_id:
        description: Device name for X-Emby-Authorization header
        required: false
        default: "Ansible Client ID"
        type: str    
     client_version:
        description: Device name for X-Emby-Authorization header
        required: false
        default: "10.8.13"
        type: str
    admin_user:
        description: The username for the admin account
        required: true
        type: str
    admin_password:
        description: The password for the admin account
        required: true
        type: str 
    key_name:
        description: The password for the admin account
        required: true
        type: str    

# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
# extends_documentation_fragment:
#     - my_namespace.my_collection.my_doc_fragment_name

author:
    - David "Laikar" Bañón Gil (@Laikar)
'''
#!TODO: Update example ussages
EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  my_namespace.my_collection.my_test:
    name: hello world

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
# These are examples of possible return values, and in general should use other names for return values.
api_key:
    description: The api key created
    type: str
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.laikar.jellyfin.plugins.module_utils.common import KeyClient, UserPassClient, auth_module_args, connection_module_args
from ansible_collections.laikar.jellyfin.plugins.module_utils.api_keys import get_api_keys, create_api_keys, delete_api_keys
from ansible_collections.laikar.jellyfin.plugins.module_utils.jellyfin_api_client.models.authentication_info import AuthenticationInfo
from result import as_result, Ok, Err, Result, UnwrapError

@as_result(UnwrapError)
def action(params) -> Dict:
    result = {}
    with KeyClient(base_url = params['jellyfin_url'], 
                client_name = params['client_name'],
                device_name = params['device_name'],
                device_id = params['device_id'],
                version = params['client_version'],
                key=params['api_key'])\
        if params['api_key'] else\
        UserPassClient(base_url = params['jellyfin_url'], 
                        client_name = params['client_name'],
                        device_name = params['device_name'],
                        device_id = params['device_id'],
                        version = params['client_version'],
                        username=params['admin_user'],
                        password=params['admin_password']) as client:
        created_keys = {}
        deleted_keys = {}
        # Añadir error handling a esto
        match params['state']:
            case 'present':
                created_keys = create_api_keys(client=client, key_names=params['api_keys']).unwrap()    
                if params['delete_duplicate_keys']:
                    deleted_keys = delete_api_keys(client=client, api_keys=params['api_keys'], delete_duplicates_only=True).unwrap()
            case 'absent':
                deleted_keys = delete_api_keys(client=client, api_keys=params['api_keys']).unwrap()
        result['changed'] = len(created_keys) != 0 and len(deleted_keys) !=0
        result['created_keys'] = created_keys
        result['created_keys'] = deleted_keys
    return result
def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        api_keys = dict(type='list', elements='str', required=True)
    )
    
    module_args.update(connection_module_args)
    module_args.update(auth_module_args)

    
    module = AnsibleModule(
        argument_spec=module_args,
    )
    params: Dict = module.params # type: ignore
    
    match action(params):
        case Ok(result):
           module.exit_json(**result) 
        case Err(e):
            module.fail_json(msg=e)


                    
        


def main():
    run_module()


if __name__ == '__main__':
    main()