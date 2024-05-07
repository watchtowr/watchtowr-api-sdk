# ClientSuspiciousDomainData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SuspiciousDomain**](SuspiciousDomain.md) |  | 

## Example

```python
from watchtowr_api.models.client_suspicious_domain_data import ClientSuspiciousDomainData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSuspiciousDomainData from a JSON string
client_suspicious_domain_data_instance = ClientSuspiciousDomainData.from_json(json)
# print the JSON string representation of the object
print(ClientSuspiciousDomainData.to_json())

# convert the object into a dict
client_suspicious_domain_data_dict = client_suspicious_domain_data_instance.to_dict()
# create an instance of ClientSuspiciousDomainData from a dict
client_suspicious_domain_data_from_dict = ClientSuspiciousDomainData.from_dict(client_suspicious_domain_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


