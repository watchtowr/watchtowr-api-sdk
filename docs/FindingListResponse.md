# FindingListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientFinding]**](ClientFinding.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api.models.finding_list_response import FindingListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindingListResponse from a JSON string
finding_list_response_instance = FindingListResponse.from_json(json)
# print the JSON string representation of the object
print(FindingListResponse.to_json())

# convert the object into a dict
finding_list_response_dict = finding_list_response_instance.to_dict()
# create an instance of FindingListResponse from a dict
finding_list_response_from_dict = FindingListResponse.from_dict(finding_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


