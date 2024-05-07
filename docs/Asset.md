# Asset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | 
**created_at** | **datetime** | Created at | 
**source** | **str** | Source | 
**type** | **str** | Type | 
**status** | **str** | Status | 
**name** | **str** | Name | 
**country** | **str** | Country | 
**platform** | **str** | Platform | 
**provider** | **str** | Provider | 
**url** | **str** | URL | 
**business_units** | **List[str]** | Business Units | 
**discovery_reason** | **str** | Discovery Reason | 
**owner** | **str** | Owner | 
**live** | **bool** | Live | 
**metadata** | **object** | Metadata | 

## Example

```python
from watchtowr_api.models.asset import Asset

# TODO update the JSON string below
json = "{}"
# create an instance of Asset from a JSON string
asset_instance = Asset.from_json(json)
# print the JSON string representation of the object
print(Asset.to_json())

# convert the object into a dict
asset_dict = asset_instance.to_dict()
# create an instance of Asset from a dict
asset_from_dict = Asset.from_dict(asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


