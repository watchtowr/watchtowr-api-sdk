# ClientIpRangeData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientIpRange**](ClientIpRange.md) |  | 

## Example

```python
from watchtowr_api.models.client_ip_range_data import ClientIpRangeData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientIpRangeData from a JSON string
client_ip_range_data_instance = ClientIpRangeData.from_json(json)
# print the JSON string representation of the object
print ClientIpRangeData.to_json()

# convert the object into a dict
client_ip_range_data_dict = client_ip_range_data_instance.to_dict()
# create an instance of ClientIpRangeData from a dict
client_ip_range_data_form_dict = client_ip_range_data.from_dict(client_ip_range_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


