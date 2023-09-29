# ClientContainerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientContainer**](ClientContainer.md) |  | 

## Example

```python
from watchtowr_api.models.client_container_data import ClientContainerData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientContainerData from a JSON string
client_container_data_instance = ClientContainerData.from_json(json)
# print the JSON string representation of the object
print ClientContainerData.to_json()

# convert the object into a dict
client_container_data_dict = client_container_data_instance.to_dict()
# create an instance of ClientContainerData from a dict
client_container_data_form_dict = client_container_data.from_dict(client_container_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


