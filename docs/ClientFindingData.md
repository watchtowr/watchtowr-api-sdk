# ClientFindingData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientFinding**](ClientFinding.md) |  | 

## Example

```python
from watchtowr_api.models.client_finding_data import ClientFindingData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientFindingData from a JSON string
client_finding_data_instance = ClientFindingData.from_json(json)
# print the JSON string representation of the object
print(ClientFindingData.to_json())

# convert the object into a dict
client_finding_data_dict = client_finding_data_instance.to_dict()
# create an instance of ClientFindingData from a dict
client_finding_data_from_dict = ClientFindingData.from_dict(client_finding_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


