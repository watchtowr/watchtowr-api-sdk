# ClientDomainData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientDomain**](ClientDomain.md) |  | 

## Example

```python
from watchtowr_api.models.client_domain_data import ClientDomainData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientDomainData from a JSON string
client_domain_data_instance = ClientDomainData.from_json(json)
# print the JSON string representation of the object
print(ClientDomainData.to_json())

# convert the object into a dict
client_domain_data_dict = client_domain_data_instance.to_dict()
# create an instance of ClientDomainData from a dict
client_domain_data_from_dict = ClientDomainData.from_dict(client_domain_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


