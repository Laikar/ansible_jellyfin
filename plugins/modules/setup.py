#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
from typing import Dict, List
__metaclass__ = type

DOCUMENTATION = r'''
---
module: jellyfin_initial_setup

short_description: This module performs the initial setup on a jellyfin server

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "0.1"

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
    remote_access:
        description: enable remote access
        required: false
        default: true
        type: bool
    automatic_port_mapping:
        description: Enable remote port mapping (UPnP)
        required: false
        default: false
        type: bool
     metadata_country_code:
        description: Device name for X-Emby-Authorization header
        required: false
        default: "EN"
        type: str     
    preferred_metadata_language:
        description: Device name for X-Emby-Authorization header
        required: false
        default: "en"
        type: str     
    ui_culture:
        description: Device name for X-Emby-Authorization header
        required: false
        default: "en-US"
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

from result import Result, Ok, Err, UnwrapError, as_result
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.laikar.jellyfin.plugins.module_utils.common import Client, auth_module_args, connection_module_args, server_reachable
from ansible_collections.laikar.jellyfin.plugins.module_utils.setup import setup, setup_completed

from ansible_collections.laikar.jellyfin.plugins.module_utils.jellyfin_api_client.models import StartupConfigurationDto, StartupRemoteAccessDto, StartupUserDto
from ansible_collections.laikar.jellyfin.plugins.module_utils.jellyfin_api_client.api.startup import update_startup_user, complete_wizard, get_first_user, get_startup_configuration, set_remote_access, update_initial_configuration

def perform_setup(client, params) -> Result[None, str]:
    # This needs to be done or jellyfin throws server error on updating startup user
    default_user_response= get_first_user.sync_detailed(client=client)
    if default_user_response.status_code != 200:
        return Err("Unexpected response when obtaining default user")
    update_user_response = update_startup_user.sync_detailed(client=client, body=StartupUserDto(
        name=params['admin_user'],
        password=params['admin_password']
    ))
    if update_user_response.status_code != 204:
        return Err("Unexpected response when updating default user")
    remote_asccess_response = set_remote_access.sync_detailed(client=client, body= StartupRemoteAccessDto(
        enable_automatic_port_mapping=params['automatic_port_mapping'],
        enable_remote_access=params['remote_access']
    ))
    if remote_asccess_response.status_code != 204:
        return Err("Unexpected response when updating remote acess settings")
    initial_config_response = update_initial_configuration.sync_detailed(client=client, body=StartupConfigurationDto(
        metadata_country_code=params['metadata_country_code'],
        preferred_metadata_language=params['preferred_metadata_language'],
        ui_culture=params['ui_culture']
    ))
    if initial_config_response.status_code != 204:
        return Err("Unexpected response when updating initial configuration")
    complete_wizrd_request = complete_wizard.sync_detailed(client=client)
    if complete_wizrd_request.status_code != 204:
        return Err("Unexpected response when finishing the setup wizard")
    return Ok(None)
@as_result(UnwrapError)
def action(params) -> Result[Dict, str]:
    with Client(base_url = params['jellyfin_url'], 
            client_name = params['client_name'],
            device_name = params['device_name'],
            device_id = params['device_id'],
            version = params['client_version']) as client:
        if not server_reachable(client=client):
            return Err('Jellyfin server is not reachable')
        if setup_completed(client=client).unwrap():

            #!TODO: Update server settings even when initial setup has already been done
            return Ok({'changed': False})
        match setup(client=client, 
            admin_user=params['admin_user'], 
            admin_password=params['admin_password'], 
            automatic_port_mapping=params['automatic_port_mapping'], 
            remote_access=params['remote_access'], 
            metadata_country_code=params['metadata_country_code'],
            metadata_language=params['preferred_metadata_language'],
            ui_culture=params['ui_culture']):
            case Ok(None):
                return Ok({'changed': True})
            case Err(e):
                return Err(e)
def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        admin_user = dict(type='str', required=True),
        admin_password = dict(type='str', required=True),

        remote_access = dict(type='bool', required=False, default=True),
        automatic_port_mapping = dict(type='bool', required=False, default=False),

        metadata_country_code = dict(type='str', required=False, default="EN"),
        preferred_metadata_language = dict(type='str', required=False, default="en"),
        ui_culture = dict(type='str', required=False, default="en-US"),
    )
    module_args.update(connection_module_args)
    module_args.update(auth_module_args)

    
    module = AnsibleModule(
        argument_spec=module_args,
    )


    match action(module.params):
        case Ok(result):
            module.exit_json(**result.unwrap())
        case Err(e):
            module.fail_json(msg=e, changed=False, failed=True)



def main():
    run_module()


if __name__ == '__main__':
    main()