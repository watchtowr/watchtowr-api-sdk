# coding: utf-8

"""
    watchTowr Platform Client API SDK

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
from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from watchtowr_api.models.client_business_unit import ClientBusinessUnit

class PointsOfInterest(BaseModel):
    """
    PointsOfInterest
    """
    id: Union[StrictFloat, StrictInt] = Field(..., description="ID")
    name: StrictStr = Field(..., description="Name")
    type: StrictStr = Field(..., description="Type")
    url: StrictStr = Field(..., description="Url")
    discovery_tool_id: StrictStr = Field(..., alias="discoveryToolId", description="Discovery tool ID")
    discovery_date: Optional[datetime] = Field(None, alias="discoveryDate", description="Discovery date")
    asset_id: Union[StrictFloat, StrictInt] = Field(..., alias="assetId", description="Asset ID")
    asset_name: StrictStr = Field(..., alias="assetName", description="Asset name")
    asset_type: StrictStr = Field(..., alias="assetType", description="Asset type")
    business_units: conlist(ClientBusinessUnit) = Field(..., alias="businessUnits", description="Business unit")
    __properties = ["id", "name", "type", "url", "discoveryToolId", "discoveryDate", "assetId", "assetName", "assetType", "businessUnits"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PointsOfInterest:
        """Create an instance of PointsOfInterest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in business_units (list)
        _items = []
        if self.business_units:
            for _item in self.business_units:
                if _item:
                    _items.append(_item.to_dict())
            _dict['businessUnits'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PointsOfInterest:
        """Create an instance of PointsOfInterest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PointsOfInterest.parse_obj(obj)

        _obj = PointsOfInterest.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "url": obj.get("url"),
            "discovery_tool_id": obj.get("discoveryToolId"),
            "discovery_date": obj.get("discoveryDate"),
            "asset_id": obj.get("assetId"),
            "asset_name": obj.get("assetName"),
            "asset_type": obj.get("assetType"),
            "business_units": [ClientBusinessUnit.from_dict(_item) for _item in obj.get("businessUnits")] if obj.get("businessUnits") is not None else None
        })
        return _obj


