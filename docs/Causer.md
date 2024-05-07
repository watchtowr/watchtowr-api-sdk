# Causer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID | 
**name** | **object** | User name | 

## Example

```python
from watchtowr_api.models.causer import Causer

# TODO update the JSON string below
json = "{}"
# create an instance of Causer from a JSON string
causer_instance = Causer.from_json(json)
# print the JSON string representation of the object
print(Causer.to_json())

# convert the object into a dict
causer_dict = causer_instance.to_dict()
# create an instance of Causer from a dict
causer_from_dict = Causer.from_dict(causer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


