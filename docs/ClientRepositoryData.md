# ClientRepositoryData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientRepository**](ClientRepository.md) |  | 

## Example

```python
from watchtowr_api.models.client_repository_data import ClientRepositoryData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientRepositoryData from a JSON string
client_repository_data_instance = ClientRepositoryData.from_json(json)
# print the JSON string representation of the object
print ClientRepositoryData.to_json()

# convert the object into a dict
client_repository_data_dict = client_repository_data_instance.to_dict()
# create an instance of ClientRepositoryData from a dict
client_repository_data_form_dict = client_repository_data.from_dict(client_repository_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


