# ServiceInformationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID | 
**response** | **str** | Response | 
**certificate** | [**ServiceInformationCertificate**](ServiceInformationCertificate.md) |  | 
**asset** | [**ServiceInformationAsset**](ServiceInformationAsset.md) |  | 

## Example

```python
from watchtowr_api.models.service_information_response import ServiceInformationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceInformationResponse from a JSON string
service_information_response_instance = ServiceInformationResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceInformationResponse.to_json())

# convert the object into a dict
service_information_response_dict = service_information_response_instance.to_dict()
# create an instance of ServiceInformationResponse from a dict
service_information_response_from_dict = ServiceInformationResponse.from_dict(service_information_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


