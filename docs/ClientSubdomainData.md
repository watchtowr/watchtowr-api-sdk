# ClientSubdomainData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientSubdomain**](ClientSubdomain.md) |  | 

## Example

```python
from watchtowr_api.models.client_subdomain_data import ClientSubdomainData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSubdomainData from a JSON string
client_subdomain_data_instance = ClientSubdomainData.from_json(json)
# print the JSON string representation of the object
print ClientSubdomainData.to_json()

# convert the object into a dict
client_subdomain_data_dict = client_subdomain_data_instance.to_dict()
# create an instance of ClientSubdomainData from a dict
client_subdomain_data_form_dict = client_subdomain_data.from_dict(client_subdomain_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


