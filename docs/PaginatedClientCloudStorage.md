# PaginatedClientCloudStorage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientCloudStorage]**](ClientCloudStorage.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api.models.paginated_client_cloud_storage import PaginatedClientCloudStorage

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientCloudStorage from a JSON string
paginated_client_cloud_storage_instance = PaginatedClientCloudStorage.from_json(json)
# print the JSON string representation of the object
print(PaginatedClientCloudStorage.to_json())

# convert the object into a dict
paginated_client_cloud_storage_dict = paginated_client_cloud_storage_instance.to_dict()
# create an instance of PaginatedClientCloudStorage from a dict
paginated_client_cloud_storage_from_dict = PaginatedClientCloudStorage.from_dict(paginated_client_cloud_storage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


