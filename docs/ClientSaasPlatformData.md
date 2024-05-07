# ClientSaasPlatformData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientSaasPlatform**](ClientSaasPlatform.md) |  | 

## Example

```python
from watchtowr_api.models.client_saas_platform_data import ClientSaasPlatformData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSaasPlatformData from a JSON string
client_saas_platform_data_instance = ClientSaasPlatformData.from_json(json)
# print the JSON string representation of the object
print(ClientSaasPlatformData.to_json())

# convert the object into a dict
client_saas_platform_data_dict = client_saas_platform_data_instance.to_dict()
# create an instance of ClientSaasPlatformData from a dict
client_saas_platform_data_from_dict = ClientSaasPlatformData.from_dict(client_saas_platform_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


