# watchtowr_api.SuspiciousDomainsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_suspicious_domain**](SuspiciousDomainsApi.md#get_list_suspicious_domain) | **GET** /api/client/suspicious-domain/list | List all discovered Suspicious Domains.
[**get_suspicious_domain_details**](SuspiciousDomainsApi.md#get_suspicious_domain_details) | **GET** /api/client/suspicious-domain/show/{id} | Show the details of a specific Suspicious Domain.


# **get_list_suspicious_domain**
> PaginatedSuspiciousDomain get_list_suspicious_domain(page=page, page_size=page_size, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, search=search, discovery_reason=discovery_reason, whois_search=whois_search, statuses=statuses)

List all discovered Suspicious Domains.

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
from watchtowr_api.models.paginated_suspicious_domain import PaginatedSuspiciousDomain
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
    api_instance = watchtowr_api.SuspiciousDomainsApi(api_client)
    page = 1 # float | Pagination page. The default value is 1 (optional)
    page_size = 10 # float | Pagination size. The default value is 10 and the maximum is 30 (optional)
    created_from = '2022-02-22 22:00:00' # datetime | created_at Date Range Beginning (optional)
    created_to = '2022-02-23 22:00:00' # datetime | created_at Date Range Ending (optional)
    updated_from = '2022-02-22 22:00:00' # datetime | updated_at Date Range Beginning (optional)
    updated_to = '2022-02-23 22:00:00' # datetime | updated_at Date Range Ending (optional)
    search = 'example.com' # str | Search Text (optional)
    discovery_reason = 'Example reason' # str | Search Discovery Reason (optional)
    whois_search = 'example.com' # str | Search Whois Data (optional)
    statuses = 'pending,malicious,legitimate' # str | Comma separated list of statuses (optional)

    try:
        # List all discovered Suspicious Domains.
        api_response = api_instance.get_list_suspicious_domain(page=page, page_size=page_size, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, search=search, discovery_reason=discovery_reason, whois_search=whois_search, statuses=statuses)
        print("The response of SuspiciousDomainsApi->get_list_suspicious_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuspiciousDomainsApi->get_list_suspicious_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| Pagination page. The default value is 1 | [optional] 
 **page_size** | **float**| Pagination size. The default value is 10 and the maximum is 30 | [optional] 
 **created_from** | **datetime**| created_at Date Range Beginning | [optional] 
 **created_to** | **datetime**| created_at Date Range Ending | [optional] 
 **updated_from** | **datetime**| updated_at Date Range Beginning | [optional] 
 **updated_to** | **datetime**| updated_at Date Range Ending | [optional] 
 **search** | **str**| Search Text | [optional] 
 **discovery_reason** | **str**| Search Discovery Reason | [optional] 
 **whois_search** | **str**| Search Whois Data | [optional] 
 **statuses** | **str**| Comma separated list of statuses | [optional] 

### Return type

[**PaginatedSuspiciousDomain**](PaginatedSuspiciousDomain.md)

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

# **get_suspicious_domain_details**
> ClientSuspiciousDomainData get_suspicious_domain_details(id)

Show the details of a specific Suspicious Domain.

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
from watchtowr_api.models.client_suspicious_domain_data import ClientSuspiciousDomainData
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
    api_instance = watchtowr_api.SuspiciousDomainsApi(api_client)
    id = 3.4 # float | 

    try:
        # Show the details of a specific Suspicious Domain.
        api_response = api_instance.get_suspicious_domain_details(id)
        print("The response of SuspiciousDomainsApi->get_suspicious_domain_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuspiciousDomainsApi->get_suspicious_domain_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 

### Return type

[**ClientSuspiciousDomainData**](ClientSuspiciousDomainData.md)

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
**403** | Forbidden |  -  |
**404** | 404 Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

