# watchtowr_api.ServiceListingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_service_listing**](ServiceListingApi.md#get_list_service_listing) | **GET** /api/client/service-listing/list | List all discovered services.


# **get_list_service_listing**
> PaginatedServiceListing get_list_service_listing(page=page, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, search=search, countries=countries, technology_ids=technology_ids, ports=ports, port_services=port_services, service_type_ids=service_type_ids, business_unit_ids=business_unit_ids, sort_by=sort_by, order_by=order_by)

List all discovered services.

### Example

* Bearer (Hex string) Authentication (bearer):
```python
import time
import os
import watchtowr_api
from watchtowr_api.models.paginated_service_listing import PaginatedServiceListing
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
    api_instance = watchtowr_api.ServiceListingApi(api_client)
    page = 1 # float | Pagination page (optional)
    created_from = '2022-02-22 22:00:00' # datetime | created_at Date Range Beginning (optional)
    created_to = '2022-02-23 22:00:00' # datetime | created_at Date Range Ending (optional)
    updated_from = '2022-02-22 22:00:00' # datetime | updated_at Date Range Beginning (optional)
    updated_to = '2022-02-23 22:00:00' # datetime | updated_at Date Range Ending (optional)
    search = '192.168.1.1' # str | Search string (optional)
    countries = 'US,UK' # str | Comma separated list of countries. (optional)
    technology_ids = '1,2,3' # str | Comma separated list of technology IDs. (optional)
    ports = ['[\"ports[0][port]=5&ports[0][type]=TCP\",\"ports[1][port]=80&ports[1][type]=TCP\"]'] # List[str] | Filter by port and protocol pairs. (optional)
    port_services = 'SSH,HTTP' # str | Comma separated list of services. (optional)
    service_type_ids = '1,2,3' # str | Comma separated list of service type IDs. (optional)
    business_unit_ids = '1,2,3' # str | Comma separated list of business unit IDs (optional)
    sort_by = 'last_seen' # str | Sort by (optional)
    order_by = 'DESC' # str | Order by (optional)

    try:
        # List all discovered services.
        api_response = api_instance.get_list_service_listing(page=page, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, search=search, countries=countries, technology_ids=technology_ids, ports=ports, port_services=port_services, service_type_ids=service_type_ids, business_unit_ids=business_unit_ids, sort_by=sort_by, order_by=order_by)
        print("The response of ServiceListingApi->get_list_service_listing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceListingApi->get_list_service_listing: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| Pagination page | [optional] 
 **created_from** | **datetime**| created_at Date Range Beginning | [optional] 
 **created_to** | **datetime**| created_at Date Range Ending | [optional] 
 **updated_from** | **datetime**| updated_at Date Range Beginning | [optional] 
 **updated_to** | **datetime**| updated_at Date Range Ending | [optional] 
 **search** | **str**| Search string | [optional] 
 **countries** | **str**| Comma separated list of countries. | [optional] 
 **technology_ids** | **str**| Comma separated list of technology IDs. | [optional] 
 **ports** | [**List[str]**](str.md)| Filter by port and protocol pairs. | [optional] 
 **port_services** | **str**| Comma separated list of services. | [optional] 
 **service_type_ids** | **str**| Comma separated list of service type IDs. | [optional] 
 **business_unit_ids** | **str**| Comma separated list of business unit IDs | [optional] 
 **sort_by** | **str**| Sort by | [optional] 
 **order_by** | **str**| Order by | [optional] 

### Return type

[**PaginatedServiceListing**](PaginatedServiceListing.md)

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

