from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ParentalRating")


@_attrs_define
class ParentalRating:
    """Class ParentalRating.

    Attributes:
        name (Union[None, Unset, str]): Gets or sets the name.
        value (Union[Unset, int]): Gets or sets the value.
    """

    name: Union[None, Unset, str] = UNSET
    value: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if value is not UNSET:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        value = d.pop("Value", UNSET)

        parental_rating = cls(
            name=name,
            value=value,
        )

        return parental_rating
