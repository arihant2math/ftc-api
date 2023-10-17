from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.precision_models import PrecisionModels
from ..types import UNSET, Unset

T = TypeVar("T", bound="PrecisionModel")


@_attrs_define
class PrecisionModel:
    """
    Attributes:
        is_floating (Union[Unset, bool]):
        maximum_significant_digits (Union[Unset, int]):
        scale (Union[Unset, float]):
        precision_model_type (Union[Unset, PrecisionModels]):
    """

    is_floating: Union[Unset, bool] = UNSET
    maximum_significant_digits: Union[Unset, int] = UNSET
    scale: Union[Unset, float] = UNSET
    precision_model_type: Union[Unset, PrecisionModels] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_floating = self.is_floating
        maximum_significant_digits = self.maximum_significant_digits
        scale = self.scale
        precision_model_type: Union[Unset, str] = UNSET
        if not isinstance(self.precision_model_type, Unset):
            precision_model_type = self.precision_model_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_floating is not UNSET:
            field_dict["isFloating"] = is_floating
        if maximum_significant_digits is not UNSET:
            field_dict["maximumSignificantDigits"] = maximum_significant_digits
        if scale is not UNSET:
            field_dict["scale"] = scale
        if precision_model_type is not UNSET:
            field_dict["precisionModelType"] = precision_model_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_floating = d.pop("isFloating", UNSET)

        maximum_significant_digits = d.pop("maximumSignificantDigits", UNSET)

        scale = d.pop("scale", UNSET)

        _precision_model_type = d.pop("precisionModelType", UNSET)
        precision_model_type: Union[Unset, PrecisionModels]
        if isinstance(_precision_model_type, Unset):
            precision_model_type = UNSET
        else:
            precision_model_type = PrecisionModels(_precision_model_type)

        precision_model = cls(
            is_floating=is_floating,
            maximum_significant_digits=maximum_significant_digits,
            scale=scale,
            precision_model_type=precision_model_type,
        )

        return precision_model
