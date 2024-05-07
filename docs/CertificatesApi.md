# watchtowr_api.CertificatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_certificate_details**](CertificatesApi.md#get_certificate_details) | **GET** /api/client/certificates/show/{id} | Show the details of a specific TLS/SSL certificate
[**get_list_certificates**](CertificatesApi.md#get_list_certificates) | **GET** /api/client/certificates/list | List all discovered certificates


# **get_certificate_details**
> ClientServiceInformationResponseData get_certificate_details(id)

Show the details of a specific TLS/SSL certificate

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
from watchtowr_api.models.client_service_information_response_data import ClientServiceInformationResponseData
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
    api_instance = watchtowr_api.CertificatesApi(api_client)
    id = 3.4 # float | 

    try:
        # Show the details of a specific TLS/SSL certificate
        api_response = api_instance.get_certificate_details(id)
        print("The response of CertificatesApi->get_certificate_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->get_certificate_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 

### Return type

[**ClientServiceInformationResponseData**](ClientServiceInformationResponseData.md)

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

# **get_list_certificates**
> PaginatedServiceInformationResponse get_list_certificates(page=page, page_size=page_size, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, not_after_from=not_after_from, not_after_to=not_after_to, subject_common_name_search=subject_common_name_search, subject_alt_name_search=subject_alt_name_search, subject_organisation_search=subject_organisation_search, subject_countries=subject_countries, asset_name_search=asset_name_search, statuses=statuses, business_unit_ids=business_unit_ids)

List all discovered certificates

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
from watchtowr_api.models.paginated_service_information_response import PaginatedServiceInformationResponse
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
    api_instance = watchtowr_api.CertificatesApi(api_client)
    page = 1 # float | Pagination page. The default value is 1 (optional)
    page_size = 10 # float | Pagination size. The default value is 10 and the maximum is 30 (optional)
    created_from = '2022-02-22 22:00:00' # datetime | created_at Date Range Beginning (optional)
    created_to = '2022-02-23 22:00:00' # datetime | created_at Date Range Ending (optional)
    updated_from = '2022-02-22 22:00:00' # datetime | updated_at Date Range Beginning (optional)
    updated_to = '2022-02-23 22:00:00' # datetime | updated_at Date Range Ending (optional)
    not_after_from = '2022-02-22 22:00:00' # datetime | not_after Validity Date Range Beginning (optional)
    not_after_to = '2022-02-23 22:00:00' # datetime | not_after Validity Date Range Ending (optional)
    subject_common_name_search = 'example.com' # str | Search by Subject Common Name (optional)
    subject_alt_name_search = 'example.com' # str | Search by Subject Alt Name (optional)
    subject_organisation_search = 'example' # str | Search by Subject Organization (optional)
    subject_countries = ['SG,US'] # List[str] | List of Subject Country (optional)
    asset_name_search = 'example' # str | Search by Asset Name (optional)
    statuses = 'Expired,Expiring Within 30 Days,Valid' # str | Comma separated list of statuses (optional)
    business_unit_ids = '1,2,3' # str | Comma separated list of Business Unit IDs (optional)

    try:
        # List all discovered certificates
        api_response = api_instance.get_list_certificates(page=page, page_size=page_size, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, not_after_from=not_after_from, not_after_to=not_after_to, subject_common_name_search=subject_common_name_search, subject_alt_name_search=subject_alt_name_search, subject_organisation_search=subject_organisation_search, subject_countries=subject_countries, asset_name_search=asset_name_search, statuses=statuses, business_unit_ids=business_unit_ids)
        print("The response of CertificatesApi->get_list_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->get_list_certificates: %s\n" % e)
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
 **not_after_from** | **datetime**| not_after Validity Date Range Beginning | [optional] 
 **not_after_to** | **datetime**| not_after Validity Date Range Ending | [optional] 
 **subject_common_name_search** | **str**| Search by Subject Common Name | [optional] 
 **subject_alt_name_search** | **str**| Search by Subject Alt Name | [optional] 
 **subject_organisation_search** | **str**| Search by Subject Organization | [optional] 
 **subject_countries** | [**List[str]**](str.md)| List of Subject Country | [optional] 
 **asset_name_search** | **str**| Search by Asset Name | [optional] 
 **statuses** | **str**| Comma separated list of statuses | [optional] 
 **business_unit_ids** | **str**| Comma separated list of Business Unit IDs | [optional] 

### Return type

[**PaginatedServiceInformationResponse**](PaginatedServiceInformationResponse.md)

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

