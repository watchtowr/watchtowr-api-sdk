# FindingRetestResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_by** | **str** |  | 
**requested_at** | **datetime** |  | 
**retest_status** | **str** |  | 
**status_occurred_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**evidence** | **str** |  | 

## Example

```python
from watchtowr_api.models.finding_retest_response_dto import FindingRetestResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of FindingRetestResponseDto from a JSON string
finding_retest_response_dto_instance = FindingRetestResponseDto.from_json(json)
# print the JSON string representation of the object
print(FindingRetestResponseDto.to_json())

# convert the object into a dict
finding_retest_response_dto_dict = finding_retest_response_dto_instance.to_dict()
# create an instance of FindingRetestResponseDto from a dict
finding_retest_response_dto_from_dict = FindingRetestResponseDto.from_dict(finding_retest_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


