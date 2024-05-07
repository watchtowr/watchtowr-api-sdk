# ClientRepository


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
**provider** | **str** |  | 
**business_units** | [**List[ClientBusinessUnit]**](ClientBusinessUnit.md) |  | 

## Example

```python
from watchtowr_api.models.client_repository import ClientRepository

# TODO update the JSON string below
json = "{}"
# create an instance of ClientRepository from a JSON string
client_repository_instance = ClientRepository.from_json(json)
# print the JSON string representation of the object
print(ClientRepository.to_json())

# convert the object into a dict
client_repository_dict = client_repository_instance.to_dict()
# create an instance of ClientRepository from a dict
client_repository_from_dict = ClientRepository.from_dict(client_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


