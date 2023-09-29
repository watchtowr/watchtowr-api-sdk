# Technology


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID | 
**name** | **str** | Name | 
**version** | **str** | Version | 
**display_name** | **str** | Display name | 

## Example

```python
from watchtowr_api.models.technology import Technology

# TODO update the JSON string below
json = "{}"
# create an instance of Technology from a JSON string
technology_instance = Technology.from_json(json)
# print the JSON string representation of the object
print Technology.to_json()

# convert the object into a dict
technology_dict = technology_instance.to_dict()
# create an instance of Technology from a dict
technology_form_dict = technology.from_dict(technology_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


