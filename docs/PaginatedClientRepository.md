# PaginatedClientRepository


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientRepository]**](ClientRepository.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api.models.paginated_client_repository import PaginatedClientRepository

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientRepository from a JSON string
paginated_client_repository_instance = PaginatedClientRepository.from_json(json)
# print the JSON string representation of the object
print PaginatedClientRepository.to_json()

# convert the object into a dict
paginated_client_repository_dict = paginated_client_repository_instance.to_dict()
# create an instance of PaginatedClientRepository from a dict
paginated_client_repository_form_dict = paginated_client_repository.from_dict(paginated_client_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


