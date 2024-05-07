# PaginatedClientDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientDomain]**](ClientDomain.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api.models.paginated_client_domain import PaginatedClientDomain

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientDomain from a JSON string
paginated_client_domain_instance = PaginatedClientDomain.from_json(json)
# print the JSON string representation of the object
print(PaginatedClientDomain.to_json())

# convert the object into a dict
paginated_client_domain_dict = paginated_client_domain_instance.to_dict()
# create an instance of PaginatedClientDomain from a dict
paginated_client_domain_from_dict = PaginatedClientDomain.from_dict(paginated_client_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


