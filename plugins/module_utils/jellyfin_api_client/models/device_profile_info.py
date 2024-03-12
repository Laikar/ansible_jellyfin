from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.device_profile_type import DeviceProfileType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceProfileInfo")


@_attrs_define
class DeviceProfileInfo:
    """
    Attributes:
        id (Union[None, Unset, str]): Gets or sets the identifier.
        name (Union[None, Unset, str]): Gets or sets the name.
        type (Union[Unset, DeviceProfileType]):
    """

    id: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    type: Union[Unset, DeviceProfileType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if type is not UNSET:
            field_dict["Type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        _type = d.pop("Type", UNSET)
        type: Union[Unset, DeviceProfileType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DeviceProfileType(_type)

        device_profile_info = cls(
            id=id,
            name=name,
            type=type,
        )

        return device_profile_info
