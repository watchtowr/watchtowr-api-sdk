# Hunt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID | 
**priority** | **str** | Priority | 
**type** | **str** | Type | 
**created_at** | **datetime** | Created at | 
**updated_at** | **datetime** | Updated at | 
**total_findings** | **float** | Total Findings related to this hunt | 
**total_assets** | **float** | Total assets related to this hunt | 
**hunt_request_type** | **str** | Hunt Request Type | 
**title** | **str** | Title | 
**status** | **str** | Status | 

## Example

```python
from watchtowr_api.models.hunt import Hunt

# TODO update the JSON string below
json = "{}"
# create an instance of Hunt from a JSON string
hunt_instance = Hunt.from_json(json)
# print the JSON string representation of the object
print(Hunt.to_json())

# convert the object into a dict
hunt_dict = hunt_instance.to_dict()
# create an instance of Hunt from a dict
hunt_from_dict = Hunt.from_dict(hunt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


