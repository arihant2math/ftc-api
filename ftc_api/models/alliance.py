from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Alliance")


@attr.s(auto_attribs=True)
class Alliance:
    """
    Attributes:
        number (Union[Unset, int]):
        name (Union[Unset, None, str]):
        captain (Union[Unset, None, int]):
        round1 (Union[Unset, None, int]):
        round2 (Union[Unset, None, int]):
        round3 (Union[Unset, None, int]):
        backup (Union[Unset, None, int]):
        backup_replaced (Union[Unset, None, int]):
    """

    number: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    captain: Union[Unset, None, int] = UNSET
    round1: Union[Unset, None, int] = UNSET
    round2: Union[Unset, None, int] = UNSET
    round3: Union[Unset, None, int] = UNSET
    backup: Union[Unset, None, int] = UNSET
    backup_replaced: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        name = self.name
        captain = self.captain
        round1 = self.round1
        round2 = self.round2
        round3 = self.round3
        backup = self.backup
        backup_replaced = self.backup_replaced

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if number is not UNSET:
            field_dict["number"] = number
        if name is not UNSET:
            field_dict["name"] = name
        if captain is not UNSET:
            field_dict["captain"] = captain
        if round1 is not UNSET:
            field_dict["round1"] = round1
        if round2 is not UNSET:
            field_dict["round2"] = round2
        if round3 is not UNSET:
            field_dict["round3"] = round3
        if backup is not UNSET:
            field_dict["backup"] = backup
        if backup_replaced is not UNSET:
            field_dict["backupReplaced"] = backup_replaced

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number = d.pop("number", UNSET)

        name = d.pop("name", UNSET)

        captain = d.pop("captain", UNSET)

        round1 = d.pop("round1", UNSET)

        round2 = d.pop("round2", UNSET)

        round3 = d.pop("round3", UNSET)

        backup = d.pop("backup", UNSET)

        backup_replaced = d.pop("backupReplaced", UNSET)

        alliance = cls(
            number=number,
            name=name,
            captain=captain,
            round1=round1,
            round2=round2,
            round3=round3,
            backup=backup,
            backup_replaced=backup_replaced,
        )

        return alliance
