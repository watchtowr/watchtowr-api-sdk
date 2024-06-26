# watchtowr_api.FindingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_pdf_for_finding**](FindingsApi.md#export_pdf_for_finding) | **GET** /api/client/findings/export/{id} | Export a PDF of a specific finding
[**get_available_finding_statuses**](FindingsApi.md#get_available_finding_statuses) | **GET** /api/client/findings/statuses | List the available statuses for a finding.
[**get_finding_details**](FindingsApi.md#get_finding_details) | **GET** /api/client/findings/show/{id} | Show the detail of a specific finding
[**get_list_findings**](FindingsApi.md#get_list_findings) | **GET** /api/client/findings/list | List all discovered findings, ordered by date identified.
[**start_specific_finding_retest**](FindingsApi.md#start_specific_finding_retest) | **POST** /api/client/findings/retest/{finding_id} | Start specific finding retest
[**update_finding_status**](FindingsApi.md#update_finding_status) | **POST** /api/client/findings/status/{id} | Update the status of a finding.


# **export_pdf_for_finding**
> export_pdf_for_finding(id, api_token)

Export a PDF of a specific finding

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
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
    api_instance = watchtowr_api.FindingsApi(api_client)
    id = 3.4 # float | 
    api_token = 'api_token_example' # str | 

    try:
        # Export a PDF of a specific finding
        api_instance.export_pdf_for_finding(id, api_token)
    except Exception as e:
        print("Exception when calling FindingsApi->export_pdf_for_finding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 
 **api_token** | **str**|  | 

### Return type

void (empty response body)

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

# **get_available_finding_statuses**
> get_available_finding_statuses()

List the available statuses for a finding.

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
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
    api_instance = watchtowr_api.FindingsApi(api_client)

    try:
        # List the available statuses for a finding.
        api_instance.get_available_finding_statuses()
    except Exception as e:
        print("Exception when calling FindingsApi->get_available_finding_statuses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finding_details**
> ClientFindingData get_finding_details(id, api_token)

Show the detail of a specific finding

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
from watchtowr_api.models.client_finding_data import ClientFindingData
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
    api_instance = watchtowr_api.FindingsApi(api_client)
    id = 3.4 # float | 
    api_token = 'api_token_example' # str | 

    try:
        # Show the detail of a specific finding
        api_response = api_instance.get_finding_details(id, api_token)
        print("The response of FindingsApi->get_finding_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->get_finding_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 
 **api_token** | **str**|  | 

### Return type

[**ClientFindingData**](ClientFindingData.md)

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

# **get_list_findings**
> PaginatedClientFindings get_list_findings(page=page, page_size=page_size, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, statuses=statuses, business_unit_ids=business_unit_ids, finding_impact_threshold=finding_impact_threshold, finding_title=finding_title, severities=severities, asset_title=asset_title, asset_types=asset_types, assignee=assignee, tags=tags)

List all discovered findings, ordered by date identified.

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
from watchtowr_api.models.paginated_client_findings import PaginatedClientFindings
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
    api_instance = watchtowr_api.FindingsApi(api_client)
    page = 1 # float | Pagination page. The default value is 1 (optional)
    page_size = 10 # float | Pagination size. The default value is 10 and the maximum is 30 (optional)
    created_from = '2022-02-22 22:00:00' # datetime | created_at Date Range Beginning (optional)
    created_to = '2022-02-23 22:00:00' # datetime | created_at Date Range Ending (optional)
    updated_from = '2022-02-22 22:00:00' # datetime | updated_at Date Range Beginning (optional)
    updated_to = '2022-02-23 22:00:00' # datetime | updated_at Date Range Ending (optional)
    statuses = 'confirmed,unconfirmed,remediated,risk-accepted,closed,asset-no-longer-tracked' # str | Comma separated list of statuses (optional)
    business_unit_ids = '1,2,3' # str | Comma separated list of Business Unit IDs (optional)
    finding_impact_threshold = 'finding_impact_threshold_example' # str | Impact Setting: * High - Prioritised Findings (vulnerabilities, misconfigurations and weaknesses) that could have an immediate, direct impact on your organisation's security posture. * All - All Findings, a broader range of findings that may not directly impact your organisation's security posture, but may represent deviations from best practices. (optional)
    finding_title = 'Example title' # str | Finding title (optional)
    severities = 'critical,high,medium,low,info' # str | Finding Severity (optional)
    asset_title = 'Example asset title' # str | Title's asset belong to finding (optional)
    asset_types = 'domain,subdomain,ip,ipRange,port,dnsRecord,repository,cloudStorage,container,mobileApp,saasPlatform,cloudAssets' # str | Asset Types (optional)
    assignee = 'some assignee name' # str | Assignee for finding, if want to filter findings which don't have assignee, please use assignee=No Assignee (optional)
    tags = 'CISA-KEV,Defacement,Credentials' # str | Comma separated list of tags (optional)

    try:
        # List all discovered findings, ordered by date identified.
        api_response = api_instance.get_list_findings(page=page, page_size=page_size, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, statuses=statuses, business_unit_ids=business_unit_ids, finding_impact_threshold=finding_impact_threshold, finding_title=finding_title, severities=severities, asset_title=asset_title, asset_types=asset_types, assignee=assignee, tags=tags)
        print("The response of FindingsApi->get_list_findings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->get_list_findings: %s\n" % e)
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
 **statuses** | **str**| Comma separated list of statuses | [optional] 
 **business_unit_ids** | **str**| Comma separated list of Business Unit IDs | [optional] 
 **finding_impact_threshold** | **str**| Impact Setting: * High - Prioritised Findings (vulnerabilities, misconfigurations and weaknesses) that could have an immediate, direct impact on your organisation&#39;s security posture. * All - All Findings, a broader range of findings that may not directly impact your organisation&#39;s security posture, but may represent deviations from best practices. | [optional] 
 **finding_title** | **str**| Finding title | [optional] 
 **severities** | **str**| Finding Severity | [optional] 
 **asset_title** | **str**| Title&#39;s asset belong to finding | [optional] 
 **asset_types** | **str**| Asset Types | [optional] 
 **assignee** | **str**| Assignee for finding, if want to filter findings which don&#39;t have assignee, please use assignee&#x3D;No Assignee | [optional] 
 **tags** | **str**| Comma separated list of tags | [optional] 

### Return type

[**PaginatedClientFindings**](PaginatedClientFindings.md)

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

# **start_specific_finding_retest**
> ClientFinding start_specific_finding_retest(finding_id)

Start specific finding retest

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
from watchtowr_api.models.client_finding import ClientFinding
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
    api_instance = watchtowr_api.FindingsApi(api_client)
    finding_id = 3.4 # float | 

    try:
        # Start specific finding retest
        api_response = api_instance.start_specific_finding_retest(finding_id)
        print("The response of FindingsApi->start_specific_finding_retest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->start_specific_finding_retest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finding_id** | **float**|  | 

### Return type

[**ClientFinding**](ClientFinding.md)

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
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_finding_status**
> ClientFinding update_finding_status(id, api_token, update_client_finding_status_request_body)

Update the status of a finding.

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
from watchtowr_api.models.client_finding import ClientFinding
from watchtowr_api.models.update_client_finding_status_request_body import UpdateClientFindingStatusRequestBody
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
    api_instance = watchtowr_api.FindingsApi(api_client)
    id = 3.4 # float | 
    api_token = 'api_token_example' # str | 
    update_client_finding_status_request_body = watchtowr_api.UpdateClientFindingStatusRequestBody() # UpdateClientFindingStatusRequestBody | 

    try:
        # Update the status of a finding.
        api_response = api_instance.update_finding_status(id, api_token, update_client_finding_status_request_body)
        print("The response of FindingsApi->update_finding_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->update_finding_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 
 **api_token** | **str**|  | 
 **update_client_finding_status_request_body** | [**UpdateClientFindingStatusRequestBody**](UpdateClientFindingStatusRequestBody.md)|  | 

### Return type

[**ClientFinding**](ClientFinding.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | 404 Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

