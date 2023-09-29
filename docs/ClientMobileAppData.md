# ClientMobileAppData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientMobileApp**](ClientMobileApp.md) |  | 

## Example

```python
from watchtowr_api.models.client_mobile_app_data import ClientMobileAppData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientMobileAppData from a JSON string
client_mobile_app_data_instance = ClientMobileAppData.from_json(json)
# print the JSON string representation of the object
print ClientMobileAppData.to_json()

# convert the object into a dict
client_mobile_app_data_dict = client_mobile_app_data_instance.to_dict()
# create an instance of ClientMobileAppData from a dict
client_mobile_app_data_form_dict = client_mobile_app_data.from_dict(client_mobile_app_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


