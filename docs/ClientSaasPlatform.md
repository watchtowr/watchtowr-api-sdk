# ClientSaasPlatform


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**source** | **str** |  | 
**status** | **str** |  | 
**created_at** | [**ModelDate**](ModelDate.md) |  | 
**updated_at** | [**ModelDate**](ModelDate.md) |  | 
**deleted_at** | [**ModelDate**](ModelDate.md) |  | 
**id** | **float** |  | 
**url** | **str** |  | 
**provider** | **str** |  | 
**business_units** | [**List[ClientBusinessUnit]**](ClientBusinessUnit.md) |  | 

## Example

```python
from watchtowr_api.models.client_saas_platform import ClientSaasPlatform

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSaasPlatform from a JSON string
client_saas_platform_instance = ClientSaasPlatform.from_json(json)
# print the JSON string representation of the object
print(ClientSaasPlatform.to_json())

# convert the object into a dict
client_saas_platform_dict = client_saas_platform_instance.to_dict()
# create an instance of ClientSaasPlatform from a dict
client_saas_platform_from_dict = ClientSaasPlatform.from_dict(client_saas_platform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


