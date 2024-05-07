# HuntDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**HuntDetail**](HuntDetail.md) |  | 

## Example

```python
from watchtowr_api.models.hunt_detail_response import HuntDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HuntDetailResponse from a JSON string
hunt_detail_response_instance = HuntDetailResponse.from_json(json)
# print the JSON string representation of the object
print(HuntDetailResponse.to_json())

# convert the object into a dict
hunt_detail_response_dict = hunt_detail_response_instance.to_dict()
# create an instance of HuntDetailResponse from a dict
hunt_detail_response_from_dict = HuntDetailResponse.from_dict(hunt_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


