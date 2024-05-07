# ClientServiceInformationResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceInformationResponse**](ServiceInformationResponse.md) |  | 

## Example

```python
from watchtowr_api.models.client_service_information_response_data import ClientServiceInformationResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientServiceInformationResponseData from a JSON string
client_service_information_response_data_instance = ClientServiceInformationResponseData.from_json(json)
# print the JSON string representation of the object
print(ClientServiceInformationResponseData.to_json())

# convert the object into a dict
client_service_information_response_data_dict = client_service_information_response_data_instance.to_dict()
# create an instance of ClientServiceInformationResponseData from a dict
client_service_information_response_data_from_dict = ClientServiceInformationResponseData.from_dict(client_service_information_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


