# PaginatedClientPort


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientPort]**](ClientPort.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api.models.paginated_client_port import PaginatedClientPort

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientPort from a JSON string
paginated_client_port_instance = PaginatedClientPort.from_json(json)
# print the JSON string representation of the object
print PaginatedClientPort.to_json()

# convert the object into a dict
paginated_client_port_dict = paginated_client_port_instance.to_dict()
# create an instance of PaginatedClientPort from a dict
paginated_client_port_form_dict = paginated_client_port.from_dict(paginated_client_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


