# PaginatedServiceListing


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ServiceListing]**](ServiceListing.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api.models.paginated_service_listing import PaginatedServiceListing

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedServiceListing from a JSON string
paginated_service_listing_instance = PaginatedServiceListing.from_json(json)
# print the JSON string representation of the object
print PaginatedServiceListing.to_json()

# convert the object into a dict
paginated_service_listing_dict = paginated_service_listing_instance.to_dict()
# create an instance of PaginatedServiceListing from a dict
paginated_service_listing_form_dict = paginated_service_listing.from_dict(paginated_service_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


