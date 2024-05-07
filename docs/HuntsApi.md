# watchtowr_api.HuntsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_hunts**](HuntsApi.md#get_client_hunts) | **GET** /api/client/hunts/list | List all hunts
[**get_list_asset_by_hunt**](HuntsApi.md#get_list_asset_by_hunt) | **GET** /api/client/hunts/show/{id}/assets | Get list assets of specific hunt
[**get_list_finding_by_hunt**](HuntsApi.md#get_list_finding_by_hunt) | **GET** /api/client/hunts/show/{id}/findings | Get list findings of specific hunt
[**show_the_detail_hunt**](HuntsApi.md#show_the_detail_hunt) | **GET** /api/client/hunts/show/{id} | Show the detail of specific hunt


# **get_client_hunts**
> PaginatedHunts get_client_hunts(page=page, page_size=page_size, statuses=statuses, hunt_search=hunt_search, types=types, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, priorities=priorities, general=general)

List all hunts

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
from watchtowr_api.models.paginated_hunts import PaginatedHunts
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
    api_instance = watchtowr_api.HuntsApi(api_client)
    page = 1 # float | Pagination page. The default value is 1 (optional)
    page_size = 10 # float | Pagination size. The default value is 10 and the maximum is 30 (optional)
    statuses = 'statuses_example' # str | Hunt statuses (optional)
    hunt_search = 'search text' # str | Search by hunt name (optional)
    types = 'types_example' # str | Hunt types (optional)
    created_from = '2022-02-22 22:00:00' # datetime | created_at Date Range Beginning (optional)
    created_to = '2022-02-23 22:00:00' # datetime | created_at Date Range Ending (optional)
    updated_from = '2022-02-22 22:00:00' # datetime | updated_at Date Range Beginning (optional)
    updated_to = '2022-02-23 22:00:00' # datetime | updated_at Date Range Ending (optional)
    priorities = 'priorities_example' # str | Hunt priorities (optional)
    general = 'general_example' # str | General (optional)

    try:
        # List all hunts
        api_response = api_instance.get_client_hunts(page=page, page_size=page_size, statuses=statuses, hunt_search=hunt_search, types=types, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, priorities=priorities, general=general)
        print("The response of HuntsApi->get_client_hunts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HuntsApi->get_client_hunts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| Pagination page. The default value is 1 | [optional] 
 **page_size** | **float**| Pagination size. The default value is 10 and the maximum is 30 | [optional] 
 **statuses** | **str**| Hunt statuses | [optional] 
 **hunt_search** | **str**| Search by hunt name | [optional] 
 **types** | **str**| Hunt types | [optional] 
 **created_from** | **datetime**| created_at Date Range Beginning | [optional] 
 **created_to** | **datetime**| created_at Date Range Ending | [optional] 
 **updated_from** | **datetime**| updated_at Date Range Beginning | [optional] 
 **updated_to** | **datetime**| updated_at Date Range Ending | [optional] 
 **priorities** | **str**| Hunt priorities | [optional] 
 **general** | **str**| General | [optional] 

### Return type

[**PaginatedHunts**](PaginatedHunts.md)

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

# **get_list_asset_by_hunt**
> AssetsListResponse get_list_asset_by_hunt(id, page=page, page_size=page_size)

Get list assets of specific hunt

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
from watchtowr_api.models.assets_list_response import AssetsListResponse
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
    api_instance = watchtowr_api.HuntsApi(api_client)
    id = 3.4 # float | 
    page = 1 # float | Pagination page. The default value is 1 (optional)
    page_size = 10 # float | Pagination size. The default value is 10 and the maximum is 30 (optional)

    try:
        # Get list assets of specific hunt
        api_response = api_instance.get_list_asset_by_hunt(id, page=page, page_size=page_size)
        print("The response of HuntsApi->get_list_asset_by_hunt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HuntsApi->get_list_asset_by_hunt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 
 **page** | **float**| Pagination page. The default value is 1 | [optional] 
 **page_size** | **float**| Pagination size. The default value is 10 and the maximum is 30 | [optional] 

### Return type

[**AssetsListResponse**](AssetsListResponse.md)

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

# **get_list_finding_by_hunt**
> FindingListResponse get_list_finding_by_hunt(id, page=page, page_size=page_size)

Get list findings of specific hunt

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
from watchtowr_api.models.finding_list_response import FindingListResponse
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
    api_instance = watchtowr_api.HuntsApi(api_client)
    id = 3.4 # float | 
    page = 1 # float | Pagination page. The default value is 1 (optional)
    page_size = 10 # float | Pagination size. The default value is 10 and the maximum is 30 (optional)

    try:
        # Get list findings of specific hunt
        api_response = api_instance.get_list_finding_by_hunt(id, page=page, page_size=page_size)
        print("The response of HuntsApi->get_list_finding_by_hunt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HuntsApi->get_list_finding_by_hunt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 
 **page** | **float**| Pagination page. The default value is 1 | [optional] 
 **page_size** | **float**| Pagination size. The default value is 10 and the maximum is 30 | [optional] 

### Return type

[**FindingListResponse**](FindingListResponse.md)

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

# **show_the_detail_hunt**
> HuntDetailResponse show_the_detail_hunt(id)

Show the detail of specific hunt

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
from watchtowr_api.models.hunt_detail_response import HuntDetailResponse
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
    api_instance = watchtowr_api.HuntsApi(api_client)
    id = 3.4 # float | 

    try:
        # Show the detail of specific hunt
        api_response = api_instance.show_the_detail_hunt(id)
        print("The response of HuntsApi->show_the_detail_hunt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HuntsApi->show_the_detail_hunt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 

### Return type

[**HuntDetailResponse**](HuntDetailResponse.md)

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

