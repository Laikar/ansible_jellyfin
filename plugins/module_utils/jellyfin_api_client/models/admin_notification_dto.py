from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.notification_level import NotificationLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminNotificationDto")


@_attrs_define
class AdminNotificationDto:
    """The admin notification dto.

    Attributes:
        name (Union[None, Unset, str]): Gets or sets the notification name.
        description (Union[None, Unset, str]): Gets or sets the notification description.
        notification_level (Union[None, NotificationLevel, Unset]): Gets or sets the notification level.
        url (Union[None, Unset, str]): Gets or sets the notification url.
    """

    name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    notification_level: Union[None, NotificationLevel, Unset] = UNSET
    url: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        notification_level: Union[None, Unset, str]
        if isinstance(self.notification_level, Unset):
            notification_level = UNSET
        elif isinstance(self.notification_level, NotificationLevel):
            notification_level = self.notification_level.value
        else:
            notification_level = self.notification_level

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if description is not UNSET:
            field_dict["Description"] = description
        if notification_level is not UNSET:
            field_dict["NotificationLevel"] = notification_level
        if url is not UNSET:
            field_dict["Url"] = url

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

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("Description", UNSET))

        def _parse_notification_level(data: object) -> Union[None, NotificationLevel, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                notification_level_type_1 = NotificationLevel(data)

                return notification_level_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, NotificationLevel, Unset], data)

        notification_level = _parse_notification_level(d.pop("NotificationLevel", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("Url", UNSET))

        admin_notification_dto = cls(
            name=name,
            description=description,
            notification_level=notification_level,
            url=url,
        )

        return admin_notification_dto
