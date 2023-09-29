# ClientIpData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientIp**](ClientIp.md) |  | 

## Example

```python
from watchtowr_api.models.client_ip_data import ClientIpData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientIpData from a JSON string
client_ip_data_instance = ClientIpData.from_json(json)
# print the JSON string representation of the object
print ClientIpData.to_json()

# convert the object into a dict
client_ip_data_dict = client_ip_data_instance.to_dict()
# create an instance of ClientIpData from a dict
client_ip_data_form_dict = client_ip_data.from_dict(client_ip_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


