from result import Result, Err, Ok
from .jellyfin_api_client import Client as _Client
from .jellyfin_api_client import AuthenticatedClient as _AuthenticatedClient
from .jellyfin_api_client.models import AuthenticateUserByName
from .jellyfin_api_client.api.user import authenticate_user_by_name
from .jellyfin_api_client.api.system import get_public_system_info

def Client(base_url: str, client_name: str, device_name : str, device_id: str, version: str, token: str = None):
    common_headers = {
        'MediaBrowser Client': f"{client_name}" ,
        'Device': f"{device_name}",
        'DeviceId': f"{device_id}",
        'Version': f"{version}",
    }
    if token is not None:
        common_headers['Token'] = token
    headers = {
        'X-Emby-Authorization': ', '.join(f'{key}="{value}"' for key, value in common_headers.items())
    }
    return _Client(base_url=base_url).with_headers(headers=headers)

def UserPassClient(base_url: str, client_name: str, device_name : str, device_id: str, version: str, username: str, password: str):
    with Client(base_url=base_url, client_name=client_name, device_name=device_name, device_id=device_id, version=version) as base_client:
        body = AuthenticateUserByName(username=username, pw=password)
        auth_result = authenticate_user_by_name.sync_detailed(client=base_client, body=body)
        match auth_result.status_code:
            case 200:
                token = auth_result.parsed.access_token
                return Client(base_url=base_url, client_name=client_name, device_name=device_name, device_id=device_id, version=version, token=token)
            case _:
                raise ValueError("Unknown Error")
            

def KeyClient(base_url: str, client_name: str, device_name : str, device_id: str, version: str, key: str):
    common_headers = {
        'MediaBrowser Client': f"{client_name}" ,
        'Device': f"{device_name}",
        'DeviceId': f"{device_id}",
        'Version': f"{version}",
    }
    headers = {
        'X-Emby-Authorization': ', '.join(f'{key}="{value}"' for key, value in common_headers.items())
    }
    return _AuthenticatedClient(base_url=base_url, token=key).with_headers(headers=headers)

def server_reachable(client) -> bool:
    system_info_response  = get_public_system_info.sync_detailed(client=client)
    return system_info_response.status_code == 200

connection_module_args = dict(
    jellyfin_url = dict(type='str', required=True),

    device_name = dict(type='str', required=False, default="Ansible Controller"),
    client_name = dict(type='str', required=False, default="Ansible Client"),
    device_id = dict(type='str', required=False, default="Ansible Client ID"),
    client_version = dict(type='str', required=False, default="10.8.13"),

)
auth_module_args = dict(
    admin_user = dict(type='str'),
    admin_password = dict(type='str'),
    api_key  = dict(type='str'),
)