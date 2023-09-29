# watchtowr_api.PointsOfInterestApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_points_of_interest**](PointsOfInterestApi.md#get_list_points_of_interest) | **GET** /api/client/points-of-interest/list | List all discovered Points of Interest


# **get_list_points_of_interest**
> PaginatedPointOfInterest get_list_points_of_interest(page=page, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, discovered_date_order=discovered_date_order, search=search, types=types, has_finding=has_finding, start_date=start_date, end_date=end_date, asset_statuses=asset_statuses, business_unit_ids=business_unit_ids)

List all discovered Points of Interest

### Example

* Bearer (Hex string) Authentication (bearer):
```python
import time
import os
import watchtowr_api
from watchtowr_api.models.paginated_point_of_interest import PaginatedPointOfInterest
from watchtowr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = watchtowr_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Hex string): bearer
configuration = watchtowr_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with watchtowr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = watchtowr_api.PointsOfInterestApi(api_client)
    page = 1 # float | Pagination page (optional)
    created_from = '2022-02-22 22:00:00' # datetime | created_at Date Range Beginning (optional)
    created_to = '2022-02-23 22:00:00' # datetime | created_at Date Range Ending (optional)
    updated_from = '2022-02-22 22:00:00' # datetime | updated_at Date Range Beginning (optional)
    updated_to = '2022-02-23 22:00:00' # datetime | updated_at Date Range Ending (optional)
    discovered_date_order = 'DESC' # str | Discovered Date Order (optional)
    search = '' # str | Search text (optional)
    types = 'admin-panel,open-directory' # str | Comma separated list of types (optional)
    has_finding = false # bool | Has Finding (optional)
    start_date = '2022-02-23 22:00:00' # datetime | Start date (optional)
    end_date = '2022-02-23 22:00:00' # datetime | End date (optional)
    asset_statuses = 'verified,Third Party,CDN,Unregistered,Parked,Incorrect Identification,Hanging Cloud IP,pending,VerifiedOutOfScope,VerifiedReducedAttack,Tracked' # str | Comma separated list of asset statuses (optional)
    business_unit_ids = '1,2,3' # str | Comma separated list of business unit IDs (optional)

    try:
        # List all discovered Points of Interest
        api_response = api_instance.get_list_points_of_interest(page=page, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, discovered_date_order=discovered_date_order, search=search, types=types, has_finding=has_finding, start_date=start_date, end_date=end_date, asset_statuses=asset_statuses, business_unit_ids=business_unit_ids)
        print("The response of PointsOfInterestApi->get_list_points_of_interest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsOfInterestApi->get_list_points_of_interest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| Pagination page | [optional] 
 **created_from** | **datetime**| created_at Date Range Beginning | [optional] 
 **created_to** | **datetime**| created_at Date Range Ending | [optional] 
 **updated_from** | **datetime**| updated_at Date Range Beginning | [optional] 
 **updated_to** | **datetime**| updated_at Date Range Ending | [optional] 
 **discovered_date_order** | **str**| Discovered Date Order | [optional] 
 **search** | **str**| Search text | [optional] 
 **types** | **str**| Comma separated list of types | [optional] 
 **has_finding** | **bool**| Has Finding | [optional] 
 **start_date** | **datetime**| Start date | [optional] 
 **end_date** | **datetime**| End date | [optional] 
 **asset_statuses** | **str**| Comma separated list of asset statuses | [optional] 
 **business_unit_ids** | **str**| Comma separated list of business unit IDs | [optional] 

### Return type

[**PaginatedPointOfInterest**](PaginatedPointOfInterest.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

