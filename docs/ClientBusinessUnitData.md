# ClientBusinessUnitData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientBusinessUnitDetail**](ClientBusinessUnitDetail.md) |  | 

## Example

```python
from watchtowr_api.models.client_business_unit_data import ClientBusinessUnitData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientBusinessUnitData from a JSON string
client_business_unit_data_instance = ClientBusinessUnitData.from_json(json)
# print the JSON string representation of the object
print ClientBusinessUnitData.to_json()

# convert the object into a dict
client_business_unit_data_dict = client_business_unit_data_instance.to_dict()
# create an instance of ClientBusinessUnitData from a dict
client_business_unit_data_form_dict = client_business_unit_data.from_dict(client_business_unit_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


