# ClientCloudStorageData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientCloudStorage**](ClientCloudStorage.md) |  | 

## Example

```python
from watchtowr_api.models.client_cloud_storage_data import ClientCloudStorageData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCloudStorageData from a JSON string
client_cloud_storage_data_instance = ClientCloudStorageData.from_json(json)
# print the JSON string representation of the object
print ClientCloudStorageData.to_json()

# convert the object into a dict
client_cloud_storage_data_dict = client_cloud_storage_data_instance.to_dict()
# create an instance of ClientCloudStorageData from a dict
client_cloud_storage_data_form_dict = client_cloud_storage_data.from_dict(client_cloud_storage_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


