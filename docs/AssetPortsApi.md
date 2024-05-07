# watchtowr_api.AssetPortsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_port_details**](AssetPortsApi.md#get_asset_port_details) | **GET** /api/client/assets/ip/port/show/{id} | Show the details of a specific port asset.
[**get_list_asset_ports**](AssetPortsApi.md#get_list_asset_ports) | **GET** /api/client/assets/ip/port/list | List all discovered ports belonging to IP Addresses, ordered by date identified.


# **get_asset_port_details**
> ClientPortData get_asset_port_details(id, api_token)

Show the details of a specific port asset.

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
from watchtowr_api.models.client_port_data import ClientPortData
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
    api_instance = watchtowr_api.AssetPortsApi(api_client)
    id = 3.4 # float | 
    api_token = 'api_token_example' # str | 

    try:
        # Show the details of a specific port asset.
        api_response = api_instance.get_asset_port_details(id, api_token)
        print("The response of AssetPortsApi->get_asset_port_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPortsApi->get_asset_port_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 
 **api_token** | **str**|  | 

### Return type

[**ClientPortData**](ClientPortData.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_asset_ports**
> PaginatedClientPort get_list_asset_ports(page=page, page_size=page_size, asset_name=asset_name, statuses=statuses, business_unit_ids=business_unit_ids, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to)

List all discovered ports belonging to IP Addresses, ordered by date identified.

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
from watchtowr_api.models.paginated_client_port import PaginatedClientPort
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
    api_instance = watchtowr_api.AssetPortsApi(api_client)
    page = 1 # float | Pagination page. The default value is 1 (optional)
    page_size = 10 # float | Pagination size. The default value is 10 and the maximum is 30 (optional)
    asset_name = 'www.example.com' # str | Asset name/SaaS URL/IP/IP Range/Port (optional)
    statuses = ['verified,Third Party,Unregistered,Incorrect Identification,pending,VerifiedOutOfScope,VerifiedReducedAttack,CDN,Hanging Cloud IP'] # List[str] | Asset statuses (optional)
    business_unit_ids = '1,2,3' # str | Comma separated list of Business Unit IDs (optional)
    created_from = '2022-02-22 22:00:00' # datetime | created_at Date Range Beginning (optional)
    created_to = '2022-02-23 22:00:00' # datetime | created_at Date Range Ending (optional)
    updated_from = '2022-02-22 22:00:00' # datetime | updated_at Date Range Beginning (optional)
    updated_to = '2022-02-23 22:00:00' # datetime | updated_at Date Range Ending (optional)

    try:
        # List all discovered ports belonging to IP Addresses, ordered by date identified.
        api_response = api_instance.get_list_asset_ports(page=page, page_size=page_size, asset_name=asset_name, statuses=statuses, business_unit_ids=business_unit_ids, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to)
        print("The response of AssetPortsApi->get_list_asset_ports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPortsApi->get_list_asset_ports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| Pagination page. The default value is 1 | [optional] 
 **page_size** | **float**| Pagination size. The default value is 10 and the maximum is 30 | [optional] 
 **asset_name** | **str**| Asset name/SaaS URL/IP/IP Range/Port | [optional] 
 **statuses** | [**List[str]**](str.md)| Asset statuses | [optional] 
 **business_unit_ids** | **str**| Comma separated list of Business Unit IDs | [optional] 
 **created_from** | **datetime**| created_at Date Range Beginning | [optional] 
 **created_to** | **datetime**| created_at Date Range Ending | [optional] 
 **updated_from** | **datetime**| updated_at Date Range Beginning | [optional] 
 **updated_to** | **datetime**| updated_at Date Range Ending | [optional] 

### Return type

[**PaginatedClientPort**](PaginatedClientPort.md)

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

