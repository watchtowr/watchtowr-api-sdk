# ClientPortData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientPort**](ClientPort.md) |  | 

## Example

```python
from watchtowr_api.models.client_port_data import ClientPortData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientPortData from a JSON string
client_port_data_instance = ClientPortData.from_json(json)
# print the JSON string representation of the object
print ClientPortData.to_json()

# convert the object into a dict
client_port_data_dict = client_port_data_instance.to_dict()
# create an instance of ClientPortData from a dict
client_port_data_form_dict = client_port_data.from_dict(client_port_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


