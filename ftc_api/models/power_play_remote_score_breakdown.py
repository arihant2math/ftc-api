from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PowerPlayRemoteScoreBreakdown")


@_attrs_define
class PowerPlayRemoteScoreBreakdown:
    """ """

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        src_dict.copy()
        power_play_remote_score_breakdown = cls()

        return power_play_remote_score_breakdown
