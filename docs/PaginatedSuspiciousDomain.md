# PaginatedSuspiciousDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SuspiciousDomain]**](SuspiciousDomain.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api.models.paginated_suspicious_domain import PaginatedSuspiciousDomain

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSuspiciousDomain from a JSON string
paginated_suspicious_domain_instance = PaginatedSuspiciousDomain.from_json(json)
# print the JSON string representation of the object
print(PaginatedSuspiciousDomain.to_json())

# convert the object into a dict
paginated_suspicious_domain_dict = paginated_suspicious_domain_instance.to_dict()
# create an instance of PaginatedSuspiciousDomain from a dict
paginated_suspicious_domain_from_dict = PaginatedSuspiciousDomain.from_dict(paginated_suspicious_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


