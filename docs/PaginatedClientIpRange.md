# PaginatedClientIpRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientIpRange]**](ClientIpRange.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api.models.paginated_client_ip_range import PaginatedClientIpRange

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientIpRange from a JSON string
paginated_client_ip_range_instance = PaginatedClientIpRange.from_json(json)
# print the JSON string representation of the object
print(PaginatedClientIpRange.to_json())

# convert the object into a dict
paginated_client_ip_range_dict = paginated_client_ip_range_instance.to_dict()
# create an instance of PaginatedClientIpRange from a dict
paginated_client_ip_range_from_dict = PaginatedClientIpRange.from_dict(paginated_client_ip_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


