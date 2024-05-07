# ServiceInformationAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID | 
**name** | **str** | Asset name | 
**type** | **str** | Asset type | 
**business_units** | [**List[ClientBusinessUnit]**](ClientBusinessUnit.md) | Business Unit | [optional] 

## Example

```python
from watchtowr_api.models.service_information_asset import ServiceInformationAsset

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceInformationAsset from a JSON string
service_information_asset_instance = ServiceInformationAsset.from_json(json)
# print the JSON string representation of the object
print(ServiceInformationAsset.to_json())

# convert the object into a dict
service_information_asset_dict = service_information_asset_instance.to_dict()
# create an instance of ServiceInformationAsset from a dict
service_information_asset_from_dict = ServiceInformationAsset.from_dict(service_information_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


