# ForbiddenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**status_code** | **float** |  | 

## Example

```python
from watchtowr_api.models.forbidden_response import ForbiddenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ForbiddenResponse from a JSON string
forbidden_response_instance = ForbiddenResponse.from_json(json)
# print the JSON string representation of the object
print(ForbiddenResponse.to_json())

# convert the object into a dict
forbidden_response_dict = forbidden_response_instance.to_dict()
# create an instance of ForbiddenResponse from a dict
forbidden_response_from_dict = ForbiddenResponse.from_dict(forbidden_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


