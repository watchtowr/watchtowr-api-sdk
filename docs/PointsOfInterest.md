# PointsOfInterest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID | 
**name** | **str** | Name | 
**type** | **str** | Type | 
**url** | **str** | Url | 
**discovery_tool_id** | **str** | Discovery tool ID | 
**discovery_date** | **datetime** | Discovery date | [optional] 
**asset_id** | **float** | Asset ID | 
**asset_name** | **str** | Asset name | 
**asset_type** | **str** | Asset type | 
**business_units** | [**List[ClientBusinessUnit]**](ClientBusinessUnit.md) | Business unit | 

## Example

```python
from watchtowr_api.models.points_of_interest import PointsOfInterest

# TODO update the JSON string below
json = "{}"
# create an instance of PointsOfInterest from a JSON string
points_of_interest_instance = PointsOfInterest.from_json(json)
# print the JSON string representation of the object
print PointsOfInterest.to_json()

# convert the object into a dict
points_of_interest_dict = points_of_interest_instance.to_dict()
# create an instance of PointsOfInterest from a dict
points_of_interest_form_dict = points_of_interest.from_dict(points_of_interest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


