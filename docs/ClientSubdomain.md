# ClientSubdomain


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
**business_units** | [**List[ClientBusinessUnit]**](ClientBusinessUnit.md) |  | 

## Example

```python
from watchtowr_api.models.client_subdomain import ClientSubdomain

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSubdomain from a JSON string
client_subdomain_instance = ClientSubdomain.from_json(json)
# print the JSON string representation of the object
print ClientSubdomain.to_json()

# convert the object into a dict
client_subdomain_dict = client_subdomain_instance.to_dict()
# create an instance of ClientSubdomain from a dict
client_subdomain_form_dict = client_subdomain.from_dict(client_subdomain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


