# WhoisData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID | 
**data** | [**WhoisDataObject**](WhoisDataObject.md) |  | 
**raw** | **str** | Raw | 

## Example

```python
from watchtowr_api.models.whois_data import WhoisData

# TODO update the JSON string below
json = "{}"
# create an instance of WhoisData from a JSON string
whois_data_instance = WhoisData.from_json(json)
# print the JSON string representation of the object
print(WhoisData.to_json())

# convert the object into a dict
whois_data_dict = whois_data_instance.to_dict()
# create an instance of WhoisData from a dict
whois_data_from_dict = WhoisData.from_dict(whois_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


