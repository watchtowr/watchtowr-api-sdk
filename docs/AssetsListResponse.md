# AssetsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Asset]**](Asset.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api.models.assets_list_response import AssetsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetsListResponse from a JSON string
assets_list_response_instance = AssetsListResponse.from_json(json)
# print the JSON string representation of the object
print(AssetsListResponse.to_json())

# convert the object into a dict
assets_list_response_dict = assets_list_response_instance.to_dict()
# create an instance of AssetsListResponse from a dict
assets_list_response_from_dict = AssetsListResponse.from_dict(assets_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


