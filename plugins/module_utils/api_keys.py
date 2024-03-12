from typing import Dict, List
from result import Result, Ok, Err
from .jellyfin_api_client.api.api_key import get_keys, create_key, revoke_key

def get_api_keys(client) -> Result[Dict[str, str], str]:
    """
    Returns a dict in the following format:
    api_key: api_key_name
    """
    get_keys_result = get_keys.sync_detailed(client=client)
    match get_keys_result.status_code:
        case 200:
            return Ok({item['AccessToken']: item['AppName'] for item in get_keys_result.parsed.items})
        case _:
            return Err('Unknown error when getting api keys')
def create_api_keys(client, key_names: List[str], create_duplciates = False) -> Result[dict[str, str], str]:
    existing_keys = get_api_keys(client=client).unwrap()
    created_keys = []
    output_keys =  {}
    for key_name in key_names:
        if key_name not in existing_keys.keys() or create_duplciates :
            create_key_result = create_key.sync_detailed(client=client, app=key_name)
            match create_key_result.status_code:
                case 204:
                    created_keys.append(key_name)
                case _:
                    return Err('Unknown error when creating api key')
    new_keys = get_api_keys(client=client).unwrap()
    for key, key_name in new_keys.items():
        if key_name in created_keys:
            output_keys[key] = key_name
    return Ok(output_keys)

def delete_api_keys(client, api_keys: List[str], delete_duplicates_only = False) -> Result[dict[str, str], str]:
    existing_keys = get_api_keys(client=client).unwrap()
    output_keys = {}
    single_keys = []
    for key, key_name in existing_keys.items():
        if key_name in api_keys:
            if delete_duplicates_only and key_name not in single_keys:
                single_keys.append(key_name)
            else:              
                create_key_result = revoke_key.sync_detailed(client=client, key=key)
                match create_key_result.status_code:
                    case 204:
                        output_keys[key] = key_name
                    case _:
                        return Err('Unknown error when deleting api key')
    return Ok(output_keys)
