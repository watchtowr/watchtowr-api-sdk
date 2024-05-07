# ClientContainer


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
**name** | **str** |  | 
**owner** | **str** |  | 
**platform** | **str** |  | 
**url** | **str** |  | 
**business_units** | [**List[ClientBusinessUnit]**](ClientBusinessUnit.md) |  | 

## Example

```python
from watchtowr_api.models.client_container import ClientContainer

# TODO update the JSON string below
json = "{}"
# create an instance of ClientContainer from a JSON string
client_container_instance = ClientContainer.from_json(json)
# print the JSON string representation of the object
print(ClientContainer.to_json())

# convert the object into a dict
client_container_dict = client_container_instance.to_dict()
# create an instance of ClientContainer from a dict
client_container_from_dict = ClientContainer.from_dict(client_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


