# PaginatedClientSubdomain


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientSubdomain]**](ClientSubdomain.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api.models.paginated_client_subdomain import PaginatedClientSubdomain

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientSubdomain from a JSON string
paginated_client_subdomain_instance = PaginatedClientSubdomain.from_json(json)
# print the JSON string representation of the object
print PaginatedClientSubdomain.to_json()

# convert the object into a dict
paginated_client_subdomain_dict = paginated_client_subdomain_instance.to_dict()
# create an instance of PaginatedClientSubdomain from a dict
paginated_client_subdomain_form_dict = paginated_client_subdomain.from_dict(paginated_client_subdomain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


