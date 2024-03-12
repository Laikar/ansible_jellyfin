from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    include_external_content: Union[Unset, bool] = UNSET,
    preset_views: Union[Unset, List[str]] = UNSET,
    include_hidden: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["includeExternalContent"] = include_external_content

    json_preset_views: Union[Unset, List[str]] = UNSET
    if not isinstance(preset_views, Unset):
        json_preset_views = preset_views

    params["presetViews"] = json_preset_views

    params["includeHidden"] = include_hidden

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/Users/{user_id}/Views",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BaseItemDtoQueryResult.from_dict(response.json())

        return response_200
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
    user_id: str,
    *,
    client: AuthenticatedClient,
    include_external_content: Union[Unset, bool] = UNSET,
    preset_views: Union[Unset, List[str]] = UNSET,
    include_hidden: Union[Unset, bool] = False,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Get user views.

    Args:
        user_id (str):
        include_external_content (Union[Unset, bool]):
        preset_views (Union[Unset, List[str]]):
        include_hidden (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        include_external_content=include_external_content,
        preset_views=preset_views,
        include_hidden=include_hidden,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    include_external_content: Union[Unset, bool] = UNSET,
    preset_views: Union[Unset, List[str]] = UNSET,
    include_hidden: Union[Unset, bool] = False,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Get user views.

    Args:
        user_id (str):
        include_external_content (Union[Unset, bool]):
        preset_views (Union[Unset, List[str]]):
        include_hidden (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        include_external_content=include_external_content,
        preset_views=preset_views,
        include_hidden=include_hidden,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    include_external_content: Union[Unset, bool] = UNSET,
    preset_views: Union[Unset, List[str]] = UNSET,
    include_hidden: Union[Unset, bool] = False,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Get user views.

    Args:
        user_id (str):
        include_external_content (Union[Unset, bool]):
        preset_views (Union[Unset, List[str]]):
        include_hidden (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        include_external_content=include_external_content,
        preset_views=preset_views,
        include_hidden=include_hidden,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    include_external_content: Union[Unset, bool] = UNSET,
    preset_views: Union[Unset, List[str]] = UNSET,
    include_hidden: Union[Unset, bool] = False,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Get user views.

    Args:
        user_id (str):
        include_external_content (Union[Unset, bool]):
        preset_views (Union[Unset, List[str]]):
        include_hidden (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            include_external_content=include_external_content,
            preset_views=preset_views,
            include_hidden=include_hidden,
        )
    ).parsed
