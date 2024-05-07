# PaginatedBusinessUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientBusinessUnitDetail]**](ClientBusinessUnitDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api.models.paginated_business_unit import PaginatedBusinessUnit

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedBusinessUnit from a JSON string
paginated_business_unit_instance = PaginatedBusinessUnit.from_json(json)
# print the JSON string representation of the object
print(PaginatedBusinessUnit.to_json())

# convert the object into a dict
paginated_business_unit_dict = paginated_business_unit_instance.to_dict()
# create an instance of PaginatedBusinessUnit from a dict
paginated_business_unit_from_dict = PaginatedBusinessUnit.from_dict(paginated_business_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


