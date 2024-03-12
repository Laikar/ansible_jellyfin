from ansible.module_utils.basic import AnsibleModule
from plugins.module_utils.common import Client, UserPassClient, check_correct_code
from plugins.module_utils.jellyfin_api_client.api.api_key import create_key, get_keys

from plugins.module_utils.jellyfin_api_client.models import StartupConfigurationDto, StartupRemoteAccessDto, StartupUserDto
from plugins.module_utils.jellyfin_api_client.api.startup import update_startup_user, complete_wizard, get_first_user, get_startup_configuration, set_remote_access, update_initial_configuration
from plugins.module_utils.jellyfin_api_client.api.system import get_public_system_info
from plugins.module_utils.jellyfin_api_client.api.configuration import get_named_configuration
user ="admin"
password="admin123"
print("performin initial setup")
# with Client(base_url = "http://localhost:8096",
#             client_name = "Jellyfin Web",
#             device_name = "Firefox",
#             device_id = "Test",
#             version = "10.8.13") as client:
#     check_correct_code(get_startup_configuration.sync_detailed(client=client), 200)
#     check_correct_code(get_first_user.sync_detailed(client=client), 200)
#     user_request = update_startup_user.sync_detailed(client=client, body=StartupUserDto(
#         name=user,
#         password=password
#     ))
#     check_correct_code(user_request, 204)
#     print(user_request.status_code)
#     print(get_first_user.sync_detailed(client=client))
#     remote_asccess_request = set_remote_access.sync_detailed(client=client, body= StartupRemoteAccessDto(
#         enable_automatic_port_mapping=False,
#         enable_remote_access=True
#     ))
#     check_correct_code(remote_asccess_request, 204)
#     initial_config_request = update_initial_configuration.sync_detailed(client=client, body=StartupConfigurationDto(
#         metadata_country_code="EN",
#         preferred_metadata_language="en",
#         ui_culture="en-US"
#     ))
#     check_correct_code(initial_config_request, 204)
#     complete_wizrd_request = complete_wizard.sync_detailed(client=client)
#     check_correct_code(complete_wizrd_request, 204)
with UserPassClient(base_url = "http://localhost:8096",
                    client_name = "Jellyfin Web",
                    device_name = "Firefox",
                    device_id = "Test",
                    version = "10.8.13",
                    username = user,
                    password = password) as client:
    get_config_response = get_named_configuration.sync_detailed(client=client, key='network')
    print(get_config_response)