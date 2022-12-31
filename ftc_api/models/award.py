from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Award")


@attr.s(auto_attribs=True)
class Award:
    """
    Attributes:
        award_id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        for_person (Union[Unset, bool]):
    """

    award_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    for_person: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        award_id = self.award_id
        name = self.name
        description = self.description
        for_person = self.for_person

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if award_id is not UNSET:
            field_dict["awardId"] = award_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if for_person is not UNSET:
            field_dict["forPerson"] = for_person

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        award_id = d.pop("awardId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        for_person = d.pop("forPerson", UNSET)

        award = cls(
            award_id=award_id,
            name=name,
            description=description,
            for_person=for_person,
        )

        return award
