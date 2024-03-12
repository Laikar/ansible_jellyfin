from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.dlna_profile_type import DlnaProfileType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_condition import ProfileCondition


T = TypeVar("T", bound="ResponseProfile")


@_attrs_define
class ResponseProfile:
    """
    Attributes:
        container (Union[None, Unset, str]):
        audio_codec (Union[None, Unset, str]):
        video_codec (Union[None, Unset, str]):
        type (Union[Unset, DlnaProfileType]):
        org_pn (Union[None, Unset, str]):
        mime_type (Union[None, Unset, str]):
        conditions (Union[List['ProfileCondition'], None, Unset]):
    """

    container: Union[None, Unset, str] = UNSET
    audio_codec: Union[None, Unset, str] = UNSET
    video_codec: Union[None, Unset, str] = UNSET
    type: Union[Unset, DlnaProfileType] = UNSET
    org_pn: Union[None, Unset, str] = UNSET
    mime_type: Union[None, Unset, str] = UNSET
    conditions: Union[List["ProfileCondition"], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        container: Union[None, Unset, str]
        if isinstance(self.container, Unset):
            container = UNSET
        else:
            container = self.container

        audio_codec: Union[None, Unset, str]
        if isinstance(self.audio_codec, Unset):
            audio_codec = UNSET
        else:
            audio_codec = self.audio_codec

        video_codec: Union[None, Unset, str]
        if isinstance(self.video_codec, Unset):
            video_codec = UNSET
        else:
            video_codec = self.video_codec

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        org_pn: Union[None, Unset, str]
        if isinstance(self.org_pn, Unset):
            org_pn = UNSET
        else:
            org_pn = self.org_pn

        mime_type: Union[None, Unset, str]
        if isinstance(self.mime_type, Unset):
            mime_type = UNSET
        else:
            mime_type = self.mime_type

        conditions: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.conditions, Unset):
            conditions = UNSET
        elif isinstance(self.conditions, list):
            conditions = []
            for conditions_type_0_item_data in self.conditions:
                conditions_type_0_item = conditions_type_0_item_data.to_dict()
                conditions.append(conditions_type_0_item)

        else:
            conditions = self.conditions

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if container is not UNSET:
            field_dict["Container"] = container
        if audio_codec is not UNSET:
            field_dict["AudioCodec"] = audio_codec
        if video_codec is not UNSET:
            field_dict["VideoCodec"] = video_codec
        if type is not UNSET:
            field_dict["Type"] = type
        if org_pn is not UNSET:
            field_dict["OrgPn"] = org_pn
        if mime_type is not UNSET:
            field_dict["MimeType"] = mime_type
        if conditions is not UNSET:
            field_dict["Conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.profile_condition import ProfileCondition

        d = src_dict.copy()

        def _parse_container(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        container = _parse_container(d.pop("Container", UNSET))

        def _parse_audio_codec(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        audio_codec = _parse_audio_codec(d.pop("AudioCodec", UNSET))

        def _parse_video_codec(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        video_codec = _parse_video_codec(d.pop("VideoCodec", UNSET))

        _type = d.pop("Type", UNSET)
        type: Union[Unset, DlnaProfileType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DlnaProfileType(_type)

        def _parse_org_pn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        org_pn = _parse_org_pn(d.pop("OrgPn", UNSET))

        def _parse_mime_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mime_type = _parse_mime_type(d.pop("MimeType", UNSET))

        def _parse_conditions(data: object) -> Union[List["ProfileCondition"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conditions_type_0 = []
                _conditions_type_0 = data
                for conditions_type_0_item_data in _conditions_type_0:
                    conditions_type_0_item = ProfileCondition.from_dict(conditions_type_0_item_data)

                    conditions_type_0.append(conditions_type_0_item)

                return conditions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ProfileCondition"], None, Unset], data)

        conditions = _parse_conditions(d.pop("Conditions", UNSET))

        response_profile = cls(
            container=container,
            audio_codec=audio_codec,
            video_codec=video_codec,
            type=type,
            org_pn=org_pn,
            mime_type=mime_type,
            conditions=conditions,
        )

        return response_profile
