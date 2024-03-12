from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.notification_level import NotificationLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationsSummaryDto")


@_attrs_define
class NotificationsSummaryDto:
    """The notification summary DTO.

    Attributes:
        unread_count (Union[Unset, int]): Gets or sets the number of unread notifications.
        max_unread_notification_level (Union[None, NotificationLevel, Unset]): Gets or sets the maximum unread
            notification level.
    """

    unread_count: Union[Unset, int] = UNSET
    max_unread_notification_level: Union[None, NotificationLevel, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        unread_count = self.unread_count

        max_unread_notification_level: Union[None, Unset, str]
        if isinstance(self.max_unread_notification_level, Unset):
            max_unread_notification_level = UNSET
        elif isinstance(self.max_unread_notification_level, NotificationLevel):
            max_unread_notification_level = self.max_unread_notification_level.value
        else:
            max_unread_notification_level = self.max_unread_notification_level

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if unread_count is not UNSET:
            field_dict["UnreadCount"] = unread_count
        if max_unread_notification_level is not UNSET:
            field_dict["MaxUnreadNotificationLevel"] = max_unread_notification_level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unread_count = d.pop("UnreadCount", UNSET)

        def _parse_max_unread_notification_level(data: object) -> Union[None, NotificationLevel, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                max_unread_notification_level_type_1 = NotificationLevel(data)

                return max_unread_notification_level_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, NotificationLevel, Unset], data)

        max_unread_notification_level = _parse_max_unread_notification_level(d.pop("MaxUnreadNotificationLevel", UNSET))

        notifications_summary_dto = cls(
            unread_count=unread_count,
            max_unread_notification_level=max_unread_notification_level,
        )

        return notifications_summary_dto
