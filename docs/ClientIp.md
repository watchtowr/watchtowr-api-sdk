# ClientIp


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
from watchtowr_api.models.client_ip import ClientIp

# TODO update the JSON string below
json = "{}"
# create an instance of ClientIp from a JSON string
client_ip_instance = ClientIp.from_json(json)
# print the JSON string representation of the object
print ClientIp.to_json()

# convert the object into a dict
client_ip_dict = client_ip_instance.to_dict()
# create an instance of ClientIp from a dict
client_ip_form_dict = client_ip.from_dict(client_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


