# PaginatedClientIp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientIp]**](ClientIp.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api.models.paginated_client_ip import PaginatedClientIp

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientIp from a JSON string
paginated_client_ip_instance = PaginatedClientIp.from_json(json)
# print the JSON string representation of the object
print PaginatedClientIp.to_json()

# convert the object into a dict
paginated_client_ip_dict = paginated_client_ip_instance.to_dict()
# create an instance of PaginatedClientIp from a dict
paginated_client_ip_form_dict = paginated_client_ip.from_dict(paginated_client_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


