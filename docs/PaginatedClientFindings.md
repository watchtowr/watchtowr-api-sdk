# PaginatedClientFindings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientFinding]**](ClientFinding.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api.models.paginated_client_findings import PaginatedClientFindings

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientFindings from a JSON string
paginated_client_findings_instance = PaginatedClientFindings.from_json(json)
# print the JSON string representation of the object
print(PaginatedClientFindings.to_json())

# convert the object into a dict
paginated_client_findings_dict = paginated_client_findings_instance.to_dict()
# create an instance of PaginatedClientFindings from a dict
paginated_client_findings_from_dict = PaginatedClientFindings.from_dict(paginated_client_findings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


