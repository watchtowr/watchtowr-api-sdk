# PaginatedServiceInformationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ServiceInformationResponse]**](ServiceInformationResponse.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api.models.paginated_service_information_response import PaginatedServiceInformationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedServiceInformationResponse from a JSON string
paginated_service_information_response_instance = PaginatedServiceInformationResponse.from_json(json)
# print the JSON string representation of the object
print(PaginatedServiceInformationResponse.to_json())

# convert the object into a dict
paginated_service_information_response_dict = paginated_service_information_response_instance.to_dict()
# create an instance of PaginatedServiceInformationResponse from a dict
paginated_service_information_response_from_dict = PaginatedServiceInformationResponse.from_dict(paginated_service_information_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


