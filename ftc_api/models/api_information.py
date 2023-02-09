from typing import Any, Dict, Type, TypeVar, Union

import attr

from ftc_api.types import UNSET, Unset

T = TypeVar("T", bound="APIInformation")


@attr.s(auto_attribs=True)
class APIInformation:
    """
    Attributes:
        name (Union[Unset, None, str]): api name Example: FIRST TECH CHALLENGE API.
        api_version (Union[Unset, None, str]): api version Example: 2.0.
        service_mainifest_name (Union[Unset, None, str]):
        service_mainifest_version (Union[Unset, None, str]):
        code_package_name (Union[Unset, None, str]):
        code_package_version (Union[Unset, None, str]):
        status (Union[Unset, None, str]):
        current_season (Union[Unset, int]): current season in the eyes of FTC Example: 2020.
        max_season (Union[Unset, int]): max season that can be retrieved from the API/webpages Example: 2020.
    """

    name: Union[Unset, None, str] = UNSET
    api_version: Union[Unset, None, str] = UNSET
    service_mainifest_name: Union[Unset, None, str] = UNSET
    service_mainifest_version: Union[Unset, None, str] = UNSET
    code_package_name: Union[Unset, None, str] = UNSET
    code_package_version: Union[Unset, None, str] = UNSET
    status: Union[Unset, None, str] = UNSET
    current_season: Union[Unset, int] = UNSET
    max_season: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        api_version = self.api_version
        service_mainifest_name = self.service_mainifest_name
        service_mainifest_version = self.service_mainifest_version
        code_package_name = self.code_package_name
        code_package_version = self.code_package_version
        status = self.status
        current_season = self.current_season
        max_season = self.max_season

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if api_version is not UNSET:
            field_dict["apiVersion"] = api_version
        if service_mainifest_name is not UNSET:
            field_dict["serviceMainifestName"] = service_mainifest_name
        if service_mainifest_version is not UNSET:
            field_dict["serviceMainifestVersion"] = service_mainifest_version
        if code_package_name is not UNSET:
            field_dict["codePackageName"] = code_package_name
        if code_package_version is not UNSET:
            field_dict["codePackageVersion"] = code_package_version
        if status is not UNSET:
            field_dict["status"] = status
        if current_season is not UNSET:
            field_dict["currentSeason"] = current_season
        if max_season is not UNSET:
            field_dict["maxSeason"] = max_season

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        api_version = d.pop("apiVersion", UNSET)

        service_mainifest_name = d.pop("serviceMainifestName", UNSET)

        service_mainifest_version = d.pop("serviceMainifestVersion", UNSET)

        code_package_name = d.pop("codePackageName", UNSET)

        code_package_version = d.pop("codePackageVersion", UNSET)

        status = d.pop("status", UNSET)

        current_season = d.pop("currentSeason", UNSET)

        max_season = d.pop("maxSeason", UNSET)

        api_information = cls(
            name=name,
            api_version=api_version,
            service_mainifest_name=service_mainifest_name,
            service_mainifest_version=service_mainifest_version,
            code_package_name=code_package_name,
            code_package_version=code_package_version,
            status=status,
            current_season=current_season,
            max_season=max_season,
        )

        return api_information
