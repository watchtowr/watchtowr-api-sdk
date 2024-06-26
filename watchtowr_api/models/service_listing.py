# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from watchtowr_api.models.client_business_unit import ClientBusinessUnit
from watchtowr_api.models.service_type import ServiceType
from watchtowr_api.models.technology import Technology
from typing import Optional, Set
from typing_extensions import Self

class ServiceListing(BaseModel):
    """
    ServiceListing
    """ # noqa: E501
    id: Union[StrictFloat, StrictInt] = Field(description="ID")
    port_id: Union[StrictFloat, StrictInt] = Field(description="Port ID", alias="portId")
    ip: StrictStr = Field(description="IP Address")
    port: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Port number")
    type: Optional[StrictStr] = Field(default=None, description="Port Protocol")
    country: Optional[StrictStr] = Field(default=None, description="Country code")
    banner: Optional[StrictStr] = Field(default=None, description="Banner")
    service: Optional[StrictStr] = Field(default=None, description="Service")
    source: Optional[StrictStr] = Field(default=None, description="Asset source")
    last_seen: datetime = Field(description="Last seen date Range", alias="lastSeen")
    technologies: List[Technology] = Field(description="Technology list")
    service_types: List[ServiceType] = Field(description="Service types", alias="serviceTypes")
    business_units: List[ClientBusinessUnit] = Field(description="Business Units", alias="businessUnits")
    __properties: ClassVar[List[str]] = ["id", "portId", "ip", "port", "type", "country", "banner", "service", "source", "lastSeen", "technologies", "serviceTypes", "businessUnits"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ServiceListing from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in technologies (list)
        _items = []
        if self.technologies:
            for _item in self.technologies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['technologies'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in service_types (list)
        _items = []
        if self.service_types:
            for _item in self.service_types:
                if _item:
                    _items.append(_item.to_dict())
            _dict['serviceTypes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in business_units (list)
        _items = []
        if self.business_units:
            for _item in self.business_units:
                if _item:
                    _items.append(_item.to_dict())
            _dict['businessUnits'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceListing from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "portId": obj.get("portId"),
            "ip": obj.get("ip"),
            "port": obj.get("port"),
            "type": obj.get("type"),
            "country": obj.get("country"),
            "banner": obj.get("banner"),
            "service": obj.get("service"),
            "source": obj.get("source"),
            "lastSeen": obj.get("lastSeen"),
            "technologies": [Technology.from_dict(_item) for _item in obj["technologies"]] if obj.get("technologies") is not None else None,
            "serviceTypes": [ServiceType.from_dict(_item) for _item in obj["serviceTypes"]] if obj.get("serviceTypes") is not None else None,
            "businessUnits": [ClientBusinessUnit.from_dict(_item) for _item in obj["businessUnits"]] if obj.get("businessUnits") is not None else None
        })
        return _obj


