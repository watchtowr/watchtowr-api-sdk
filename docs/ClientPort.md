# ClientPort


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**status** | **str** |  | 
**created_at** | [**ModelDate**](ModelDate.md) |  | 
**updated_at** | [**ModelDate**](ModelDate.md) |  | 
**deleted_at** | [**ModelDate**](ModelDate.md) |  | 
**id** | **float** |  | 
**ip** | **str** |  | 
**ip_id** | **float** |  | 
**port** | **float** |  | 
**banner** | **str** |  | 
**service** | **str** |  | 
**business_units** | [**List[ClientBusinessUnit]**](ClientBusinessUnit.md) |  | 

## Example

```python
from watchtowr_api.models.client_port import ClientPort

# TODO update the JSON string below
json = "{}"
# create an instance of ClientPort from a JSON string
client_port_instance = ClientPort.from_json(json)
# print the JSON string representation of the object
print ClientPort.to_json()

# convert the object into a dict
client_port_dict = client_port_instance.to_dict()
# create an instance of ClientPort from a dict
client_port_form_dict = client_port.from_dict(client_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


