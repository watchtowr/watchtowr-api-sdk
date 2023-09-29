# ClientBusinessUnit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID | 
**name** | **str** | Name | 

## Example

```python
from watchtowr_api.models.client_business_unit import ClientBusinessUnit

# TODO update the JSON string below
json = "{}"
# create an instance of ClientBusinessUnit from a JSON string
client_business_unit_instance = ClientBusinessUnit.from_json(json)
# print the JSON string representation of the object
print ClientBusinessUnit.to_json()

# convert the object into a dict
client_business_unit_dict = client_business_unit_instance.to_dict()
# create an instance of ClientBusinessUnit from a dict
client_business_unit_form_dict = client_business_unit.from_dict(client_business_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


