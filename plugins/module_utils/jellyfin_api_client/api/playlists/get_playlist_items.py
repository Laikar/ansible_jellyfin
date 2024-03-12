from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.image_type import ImageType
from ...models.item_fields import ItemFields
from ...types import UNSET, Response, Unset


def _get_kwargs(
    playlist_id: str,
    *,
    user_id: str,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
    enable_images: Union[Unset, bool] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["userId"] = user_id

    params["startIndex"] = start_index

    params["limit"] = limit

    json_fields: Union[Unset, List[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    params["enableImages"] = enable_images

    params["enableUserData"] = enable_user_data

    params["imageTypeLimit"] = image_type_limit

    json_enable_image_types: Union[Unset, List[str]] = UNSET
    if not isinstance(enable_image_types, Unset):
        json_enable_image_types = []
        for enable_image_types_item_data in enable_image_types:
            enable_image_types_item = enable_image_types_item_data.value
            json_enable_image_types.append(enable_image_types_item)

    params["enableImageTypes"] = json_enable_image_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/Playlists/{playlist_id}/Items",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BaseItemDtoQueryResult.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    playlist_id: str,
    *,
    client: AuthenticatedClient,
    user_id: str,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
    enable_images: Union[Unset, bool] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets the original items of a playlist.

    Args:
        playlist_id (str):
        user_id (str):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        fields (Union[Unset, List[ItemFields]]):
        enable_images (Union[Unset, bool]):
        enable_user_data (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        fields=fields,
        enable_images=enable_images,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    playlist_id: str,
    *,
    client: AuthenticatedClient,
    user_id: str,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
    enable_images: Union[Unset, bool] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets the original items of a playlist.

    Args:
        playlist_id (str):
        user_id (str):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        fields (Union[Unset, List[ItemFields]]):
        enable_images (Union[Unset, bool]):
        enable_user_data (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        playlist_id=playlist_id,
        client=client,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        fields=fields,
        enable_images=enable_images,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
    ).parsed


async def asyncio_detailed(
    playlist_id: str,
    *,
    client: AuthenticatedClient,
    user_id: str,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
    enable_images: Union[Unset, bool] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets the original items of a playlist.

    Args:
        playlist_id (str):
        user_id (str):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        fields (Union[Unset, List[ItemFields]]):
        enable_images (Union[Unset, bool]):
        enable_user_data (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        fields=fields,
        enable_images=enable_images,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    playlist_id: str,
    *,
    client: AuthenticatedClient,
    user_id: str,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
    enable_images: Union[Unset, bool] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets the original items of a playlist.

    Args:
        playlist_id (str):
        user_id (str):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        fields (Union[Unset, List[ItemFields]]):
        enable_images (Union[Unset, bool]):
        enable_user_data (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            playlist_id=playlist_id,
            client=client,
            user_id=user_id,
            start_index=start_index,
            limit=limit,
            fields=fields,
            enable_images=enable_images,
            enable_user_data=enable_user_data,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
        )
    ).parsed
