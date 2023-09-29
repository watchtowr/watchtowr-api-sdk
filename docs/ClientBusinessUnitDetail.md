# ClientBusinessUnitDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID | 
**name** | **str** | Name | 
**description** | **str** | Description | 
**created_at** | **object** | Created At | 

## Example

```python
from watchtowr_api.models.client_business_unit_detail import ClientBusinessUnitDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ClientBusinessUnitDetail from a JSON string
client_business_unit_detail_instance = ClientBusinessUnitDetail.from_json(json)
# print the JSON string representation of the object
print ClientBusinessUnitDetail.to_json()

# convert the object into a dict
client_business_unit_detail_dict = client_business_unit_detail_instance.to_dict()
# create an instance of ClientBusinessUnitDetail from a dict
client_business_unit_detail_form_dict = client_business_unit_detail.from_dict(client_business_unit_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


