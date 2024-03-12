from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.day_of_week import DayOfWeek
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskTriggerInfo")


@_attrs_define
class TaskTriggerInfo:
    """Class TaskTriggerInfo.

    Attributes:
        type (Union[None, Unset, str]): Gets or sets the type.
        time_of_day_ticks (Union[None, Unset, int]): Gets or sets the time of day.
        interval_ticks (Union[None, Unset, int]): Gets or sets the interval.
        day_of_week (Union[DayOfWeek, None, Unset]): Gets or sets the day of week.
        max_runtime_ticks (Union[None, Unset, int]): Gets or sets the maximum runtime ticks.
    """

    type: Union[None, Unset, str] = UNSET
    time_of_day_ticks: Union[None, Unset, int] = UNSET
    interval_ticks: Union[None, Unset, int] = UNSET
    day_of_week: Union[DayOfWeek, None, Unset] = UNSET
    max_runtime_ticks: Union[None, Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type: Union[None, Unset, str]
        if isinstance(self.type, Unset):
            type = UNSET
        else:
            type = self.type

        time_of_day_ticks: Union[None, Unset, int]
        if isinstance(self.time_of_day_ticks, Unset):
            time_of_day_ticks = UNSET
        else:
            time_of_day_ticks = self.time_of_day_ticks

        interval_ticks: Union[None, Unset, int]
        if isinstance(self.interval_ticks, Unset):
            interval_ticks = UNSET
        else:
            interval_ticks = self.interval_ticks

        day_of_week: Union[None, Unset, str]
        if isinstance(self.day_of_week, Unset):
            day_of_week = UNSET
        elif isinstance(self.day_of_week, DayOfWeek):
            day_of_week = self.day_of_week.value
        else:
            day_of_week = self.day_of_week

        max_runtime_ticks: Union[None, Unset, int]
        if isinstance(self.max_runtime_ticks, Unset):
            max_runtime_ticks = UNSET
        else:
            max_runtime_ticks = self.max_runtime_ticks

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["Type"] = type
        if time_of_day_ticks is not UNSET:
            field_dict["TimeOfDayTicks"] = time_of_day_ticks
        if interval_ticks is not UNSET:
            field_dict["IntervalTicks"] = interval_ticks
        if day_of_week is not UNSET:
            field_dict["DayOfWeek"] = day_of_week
        if max_runtime_ticks is not UNSET:
            field_dict["MaxRuntimeTicks"] = max_runtime_ticks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type = _parse_type(d.pop("Type", UNSET))

        def _parse_time_of_day_ticks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        time_of_day_ticks = _parse_time_of_day_ticks(d.pop("TimeOfDayTicks", UNSET))

        def _parse_interval_ticks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        interval_ticks = _parse_interval_ticks(d.pop("IntervalTicks", UNSET))

        def _parse_day_of_week(data: object) -> Union[DayOfWeek, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                day_of_week_type_1 = DayOfWeek(data)

                return day_of_week_type_1
            except:  # noqa: E722
                pass
            return cast(Union[DayOfWeek, None, Unset], data)

        day_of_week = _parse_day_of_week(d.pop("DayOfWeek", UNSET))

        def _parse_max_runtime_ticks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_runtime_ticks = _parse_max_runtime_ticks(d.pop("MaxRuntimeTicks", UNSET))

        task_trigger_info = cls(
            type=type,
            time_of_day_ticks=time_of_day_ticks,
            interval_ticks=interval_ticks,
            day_of_week=day_of_week,
            max_runtime_ticks=max_runtime_ticks,
        )

        return task_trigger_info
