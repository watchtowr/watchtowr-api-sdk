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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Union
from watchtowr_api.models.client_business_unit import ClientBusinessUnit
from typing import Optional, Set
from typing_extensions import Self

class ClientContainer(BaseModel):
    """
    ClientContainer
    """ # noqa: E501
    type: StrictStr
    source: StrictStr
    status: StrictStr
    created_at: ModelDate
    updated_at: ModelDate
    deleted_at: ModelDate
    id: Union[StrictFloat, StrictInt]
    name: StrictStr
    owner: StrictStr
    platform: StrictStr
    url: StrictStr
    business_units: List[ClientBusinessUnit] = Field(alias="businessUnits")
    __properties: ClassVar[List[str]] = ["type", "source", "status", "created_at", "updated_at", "deleted_at", "id", "name", "owner", "platform", "url", "businessUnits"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['verified', 'Third Party', 'Unregistered', 'Incorrect Identification', 'pending', 'VerifiedOutOfScope', 'VerifiedReducedAttack', 'Tracked']):
            raise ValueError("must be one of enum values ('verified', 'Third Party', 'Unregistered', 'Incorrect Identification', 'pending', 'VerifiedOutOfScope', 'VerifiedReducedAttack', 'Tracked')")
        return value

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
        """Create an instance of ClientContainer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_at
        if self.created_at:
            _dict['created_at'] = self.created_at.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_at
        if self.updated_at:
            _dict['updated_at'] = self.updated_at.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deleted_at
        if self.deleted_at:
            _dict['deleted_at'] = self.deleted_at.to_dict()
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
        """Create an instance of ClientContainer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "source": obj.get("source"),
            "status": obj.get("status"),
            "created_at": ModelDate.from_dict(obj["created_at"]) if obj.get("created_at") is not None else None,
            "updated_at": ModelDate.from_dict(obj["updated_at"]) if obj.get("updated_at") is not None else None,
            "deleted_at": ModelDate.from_dict(obj["deleted_at"]) if obj.get("deleted_at") is not None else None,
            "id": obj.get("id"),
            "name": obj.get("name"),
            "owner": obj.get("owner"),
            "platform": obj.get("platform"),
            "url": obj.get("url"),
            "businessUnits": [ClientBusinessUnit.from_dict(_item) for _item in obj["businessUnits"]] if obj.get("businessUnits") is not None else None
        })
        return _obj


