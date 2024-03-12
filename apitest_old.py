import pprint
from plugins.module_utils.jellyfin_api_client import Client, AuthenticatedClient
from plugins.module_utils.jellyfin_api_client.models import StartupConfigurationDto, StartupRemoteAccessDto, StartupUserDto, AuthenticateUserByName, AuthenticationResult
from plugins.module_utils.jellyfin_api_client.api.startup import update_startup_user, complete_wizard, get_first_user, get_first_user_2, get_startup_configuration, set_remote_access, update_initial_configuration
from plugins.module_utils.jellyfin_api_client.api.user import authenticate_user_by_name
from plugins.module_utils.jellyfin_api_client.api.api_key import create_key, get_keys
user="admin"
password="Admin123"

with Client(base_url="http://localhost:8096").with_headers(
    {"X-Emby-Authorization": 'MediaBrowser Client="Jellyfin Web", Device="Firefox", DeviceId="Test", Version="10.8.13"'}
    ) as client:
    print(client._headers)
    print(get_first_user.sync(client=client))
    print(update_startup_user.sync_detailed(client=client, body=StartupUserDto(name=user, password=password)))
    print(get_first_user_2.sync(client=client))
    print(get_startup_configuration.sync(client=client))
    print(update_initial_configuration.sync_detailed(client=client, body=StartupConfigurationDto(
        metadata_country_code="ES",
        preferred_metadata_language="es",
        ui_culture="en-US")))
    print(set_remote_access.sync_detailed(client=client, body= StartupRemoteAccessDto(
        enable_automatic_port_mapping=False,
        enable_remote_access=True
    )))
    # print(complete_wizard.sync_detailed(client=client))
# print("user auth")
# auth_headers = 'MediaBrowser Client="Jellyfin Web", Device="Firefox", DeviceId="Test", Version="10.8.13"'
# 
# with Client(base_url="http://localhost:8096").with_headers(
#     {"X-Emby-Authorization": 'MediaBrowser Client="Jellyfin Web", Device="Firefox", DeviceId="Test", Version="10.8.13"'}
#     ) as client:
#     body = AuthenticateUserByName(username=user, pw=password)
#     auth_result = authenticate_user_by_name.sync_detailed(client=client, body=body)
#     print(auth_result.status_code)
#     print(auth_result.parsed.access_token)
#     token = auth_result.parsed.access_token
#     if auth_result.status_code == 200:
#         with Client(base_url="http://localhost:8096").with_headers({"X-Emby-Authorization": auth_headers + f", Token=\"{token}\""}) as new_client:
#             print(create_key.sync_detailed(client=new_client, app="lahs"))
#             print(get_keys.sync_detailed(client=new_client).parsed.items)
