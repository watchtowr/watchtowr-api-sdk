# HuntDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID | 
**priority** | **str** | Priority | 
**type** | **str** | Type | 
**created_at** | **datetime** | Created at | 
**updated_at** | **datetime** | Updated at | 
**total_findings** | **float** | Total Findings | 
**total_assets** | **float** | Total Assets | 
**hunt_request_type** | **str** | Hunt Request Type | 
**title** | **str** | Title | 
**description** | **str** |  | 
**hypothesis** | **str** | Hypothesis | 
**references** | **List[str]** | references | 
**completed_at** | **datetime** | Completed at | 
**completed_by** | **str** | Completed by | 
**requested_by** | **str** | Request by | 
**status** | **str** | Status | 

## Example

```python
from watchtowr_api.models.hunt_detail import HuntDetail

# TODO update the JSON string below
json = "{}"
# create an instance of HuntDetail from a JSON string
hunt_detail_instance = HuntDetail.from_json(json)
# print the JSON string representation of the object
print(HuntDetail.to_json())

# convert the object into a dict
hunt_detail_dict = hunt_detail_instance.to_dict()
# create an instance of HuntDetail from a dict
hunt_detail_from_dict = HuntDetail.from_dict(hunt_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


