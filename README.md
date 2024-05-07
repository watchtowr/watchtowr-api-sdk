# watchTowr Platform API SDK


## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/watchtowr/watchtowr-api-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/watchtowr/watchtowr-api-sdk.git`)

Then import the package:
```python
import watchtowr_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import watchtowr_api
```


## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    api_instance = watchtowr_api.ActivityLogApi(api_client)
    page = 1 # float | Pagination page. The default value is 1 (optional)
    page_size = 10 # float | Pagination size. The default value is 10 and the maximum is 30 (optional)
    created_from = '2022-02-22 22:00:00' # datetime | Start Date (optional)
    created_to = '2022-02-23 22:00:00' # datetime | End Date (optional)
    types = ['UserInvite,UserRole,UserLock,ResetUser2FA,SetupSSO,UpdateUserSessionTimeout,SuccessfulLogin,PasswordResetTriggered,IntegrationSetUp,IntegrationUpdated,KillSwitch,FindingSetting,TestingInfrastructureUpdate,UpdatePriorityPort,ReportGenerated,ReportGenerationRequest,ReportDownloaded'] # List[str] | Subject types (optional)
    search = 'e.g access' # str | Description keyword (optional)
    user_ids = ['1,2,3'] # List[str] | User IDs (optional)

    try:
        # List all activity logs.
        api_response = api_instance.get_list_activity_logs(page=page, page_size=page_size, created_from=created_from, created_to=created_to, types=types, search=search, user_ids=user_ids)
        print("The response of ActivityLogApi->get_list_activity_logs:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ActivityLogApi->get_list_activity_logs: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActivityLogApi* | [**get_list_activity_logs**](docs/ActivityLogApi.md#get_list_activity_logs) | **GET** /api/client/activity-log/list | List all activity logs.
*AddAssetApi* | [**submit_asset**](docs/AddAssetApi.md#submit_asset) | **POST** /api/client/seeddata | Add asset to your attack surface for review.
*AssetCloudStorageAssetsApi* | [**get_asset_cloud_storage_details**](docs/AssetCloudStorageAssetsApi.md#get_asset_cloud_storage_details) | **GET** /api/client/assets/cloudStorage/show/{id} | Show the details of a specific Cloud Storage asset.
*AssetCloudStorageAssetsApi* | [**get_list_asset_cloud_storages**](docs/AssetCloudStorageAssetsApi.md#get_list_asset_cloud_storages) | **GET** /api/client/assets/cloudStorage/list | List all discovered Cloud Storage assets, ordered by date identified.
*AssetCloudStorageAssetsApi* | [**update_asset_cloud_storage_status**](docs/AssetCloudStorageAssetsApi.md#update_asset_cloud_storage_status) | **PUT** /api/client/assets/cloudStorage/update-status/{id} | Update status of a specific cloud storage asset.
*AssetContainersApi* | [**get_asset_container_details**](docs/AssetContainersApi.md#get_asset_container_details) | **GET** /api/client/assets/container/show/{id} | Show the details of a specific container asset.
*AssetContainersApi* | [**get_list_asset_container**](docs/AssetContainersApi.md#get_list_asset_container) | **GET** /api/client/assets/container/list | List all discovered Containers, ordered by date identified.
*AssetContainersApi* | [**update_asset_container_status**](docs/AssetContainersApi.md#update_asset_container_status) | **PUT** /api/client/assets/container/update-status/{id} | Update status of a specific container asset.
*AssetDomainsApi* | [**get_asset_domain_details**](docs/AssetDomainsApi.md#get_asset_domain_details) | **GET** /api/client/assets/domain/show/{id} | Show the details of a specific Domain asset.
*AssetDomainsApi* | [**get_list_asset_domains**](docs/AssetDomainsApi.md#get_list_asset_domains) | **GET** /api/client/assets/domain/list | List all discovered Domains, ordered by date identified.
*AssetDomainsApi* | [**update_asset_domain_status**](docs/AssetDomainsApi.md#update_asset_domain_status) | **PUT** /api/client/assets/domain/update-status/{id} | Update status of a specific domain asset.
*AssetIPAddressesApi* | [**get_asset_ip_details**](docs/AssetIPAddressesApi.md#get_asset_ip_details) | **GET** /api/client/assets/ip/show/{id} | Show the details of a specific IP Address asset.
*AssetIPAddressesApi* | [**get_asset_ip_port_details**](docs/AssetIPAddressesApi.md#get_asset_ip_port_details) | **GET** /api/client/assets/ip/show/{ipId}/port/show/{portId} | Show the details of a specific port asset belonging to an IP Address.
*AssetIPAddressesApi* | [**get_asset_ip_ports**](docs/AssetIPAddressesApi.md#get_asset_ip_ports) | **GET** /api/client/assets/ip/show/{id}/port/list | List all discovered ports belonging to an IP Address, ordered by date identified.
*AssetIPAddressesApi* | [**get_list_asset_ips**](docs/AssetIPAddressesApi.md#get_list_asset_ips) | **GET** /api/client/assets/ip/list | List all discovered IP Addresses, ordered by date identified.
*AssetIPAddressesApi* | [**update_asset_ip_status**](docs/AssetIPAddressesApi.md#update_asset_ip_status) | **PUT** /api/client/assets/ip/update-status/{id} | Update status of a specific IP Address asset.
*AssetIPRangesApi* | [**get_asset_iprange_details**](docs/AssetIPRangesApi.md#get_asset_iprange_details) | **GET** /api/client/assets/ipRange/show/{id} | Show the details of a specific IP Range.
*AssetIPRangesApi* | [**get_list_asset_ipranges**](docs/AssetIPRangesApi.md#get_list_asset_ipranges) | **GET** /api/client/assets/ipRange/list | List all discovered IP Ranges, ordered by date identified.
*AssetIPRangesApi* | [**update_asset_ip_range_status**](docs/AssetIPRangesApi.md#update_asset_ip_range_status) | **PUT** /api/client/assets/ipRange/update-status/{id} | Update status of a specific IP range asset.
*AssetMobileApplicationsApi* | [**get_asset_mobile_app_details**](docs/AssetMobileApplicationsApi.md#get_asset_mobile_app_details) | **GET** /api/client/assets/mobileApp/show/{id} | Show the details of a specific Mobile Application.
*AssetMobileApplicationsApi* | [**get_list_asset_mobile_apps**](docs/AssetMobileApplicationsApi.md#get_list_asset_mobile_apps) | **GET** /api/client/assets/mobileApp/list | List all discovered Mobile Applications, ordered by date identified.
*AssetMobileApplicationsApi* | [**update_asset_mobile_app_status**](docs/AssetMobileApplicationsApi.md#update_asset_mobile_app_status) | **PUT** /api/client/assets/mobileApp/update-status/{id} | Update status of a specific mobile app asset.
*AssetPortsApi* | [**get_asset_port_details**](docs/AssetPortsApi.md#get_asset_port_details) | **GET** /api/client/assets/ip/port/show/{id} | Show the details of a specific port asset.
*AssetPortsApi* | [**get_list_asset_ports**](docs/AssetPortsApi.md#get_list_asset_ports) | **GET** /api/client/assets/ip/port/list | List all discovered ports belonging to IP Addresses, ordered by date identified.
*AssetSaaSPlatformsApi* | [**get_asset_saas_platform_details**](docs/AssetSaaSPlatformsApi.md#get_asset_saas_platform_details) | **GET** /api/client/assets/saasPlatform/show/{id} | Show the details of a specific SaaS Platform.
*AssetSaaSPlatformsApi* | [**get_list_asset_saas_platforms**](docs/AssetSaaSPlatformsApi.md#get_list_asset_saas_platforms) | **GET** /api/client/assets/saasPlatform/list | List all discovered SaaS Platforms, ordered by date identified.
*AssetSaaSPlatformsApi* | [**update_asset_saas_platform_status**](docs/AssetSaaSPlatformsApi.md#update_asset_saas_platform_status) | **PUT** /api/client/assets/saasPlatform/update-status/{id} | Update status of a specific SaaS platform asset.
*AssetSourceCodeRepositoriesApi* | [**get_asset_repository_details**](docs/AssetSourceCodeRepositoriesApi.md#get_asset_repository_details) | **GET** /api/client/assets/repository/show/{id} | Show the details of a specific Source Code Repository asset.
*AssetSourceCodeRepositoriesApi* | [**get_list_asset_repositories**](docs/AssetSourceCodeRepositoriesApi.md#get_list_asset_repositories) | **GET** /api/client/assets/repository/list | List all discovered Source Code Repositories, ordered by date identified.
*AssetSourceCodeRepositoriesApi* | [**update_asset_repository_status**](docs/AssetSourceCodeRepositoriesApi.md#update_asset_repository_status) | **PUT** /api/client/assets/repository/update-status/{id} | Update status of a specific repository asset.
*AssetSubdomainsApi* | [**get_asset_subdomain_details**](docs/AssetSubdomainsApi.md#get_asset_subdomain_details) | **GET** /api/client/assets/subdomain/show/{id} | Show the details of a a specific Subdomain asset.
*AssetSubdomainsApi* | [**get_list_asset_subdomains**](docs/AssetSubdomainsApi.md#get_list_asset_subdomains) | **GET** /api/client/assets/subdomain/list | List all discovered Subdomains, ordered by date identified.
*AssetSubdomainsApi* | [**update_asset_subdomain_status**](docs/AssetSubdomainsApi.md#update_asset_subdomain_status) | **PUT** /api/client/assets/subdomain/update-status/{id} | Update status of a specific subdomain asset.
*BusinessUnitApi* | [**get_business_unit_details**](docs/BusinessUnitApi.md#get_business_unit_details) | **GET** /api/client/business-unit/show/{id} | Get Business Unit details by Business Unit ID.
*BusinessUnitApi* | [**get_list_business_unit**](docs/BusinessUnitApi.md#get_list_business_unit) | **GET** /api/client/business-unit/list | List Business Units.
*CertificatesApi* | [**get_certificate_details**](docs/CertificatesApi.md#get_certificate_details) | **GET** /api/client/certificates/show/{id} | Show the details of a specific TLS/SSL certificate
*CertificatesApi* | [**get_list_certificates**](docs/CertificatesApi.md#get_list_certificates) | **GET** /api/client/certificates/list | List all discovered certificates
*FindingsApi* | [**export_pdf_for_finding**](docs/FindingsApi.md#export_pdf_for_finding) | **GET** /api/client/findings/export/{id} | Export a PDF of a specific finding
*FindingsApi* | [**get_available_finding_statuses**](docs/FindingsApi.md#get_available_finding_statuses) | **GET** /api/client/findings/statuses | List the available statuses for a finding.
*FindingsApi* | [**get_finding_details**](docs/FindingsApi.md#get_finding_details) | **GET** /api/client/findings/show/{id} | Show the detail of a specific finding
*FindingsApi* | [**get_list_findings**](docs/FindingsApi.md#get_list_findings) | **GET** /api/client/findings/list | List all discovered findings, ordered by date identified.
*FindingsApi* | [**start_specific_finding_retest**](docs/FindingsApi.md#start_specific_finding_retest) | **POST** /api/client/findings/retest/{finding_id} | Start specific finding retest
*FindingsApi* | [**update_finding_status**](docs/FindingsApi.md#update_finding_status) | **POST** /api/client/findings/status/{id} | Update the status of a finding.
*HuntsApi* | [**get_client_hunts**](docs/HuntsApi.md#get_client_hunts) | **GET** /api/client/hunts/list | List all hunts
*HuntsApi* | [**get_list_asset_by_hunt**](docs/HuntsApi.md#get_list_asset_by_hunt) | **GET** /api/client/hunts/show/{id}/assets | Get list assets of specific hunt
*HuntsApi* | [**get_list_finding_by_hunt**](docs/HuntsApi.md#get_list_finding_by_hunt) | **GET** /api/client/hunts/show/{id}/findings | Get list findings of specific hunt
*HuntsApi* | [**show_the_detail_hunt**](docs/HuntsApi.md#show_the_detail_hunt) | **GET** /api/client/hunts/show/{id} | Show the detail of specific hunt
*PointsOfInterestApi* | [**get_list_points_of_interest**](docs/PointsOfInterestApi.md#get_list_points_of_interest) | **GET** /api/client/points-of-interest/list | List all discovered Points of Interest.
*ServiceListingApi* | [**get_list_service_listing**](docs/ServiceListingApi.md#get_list_service_listing) | **GET** /api/client/service-listing/list | List all discovered services.
*SourceIPAddressesApi* | [**get_list_source_ip_addresses**](docs/SourceIPAddressesApi.md#get_list_source_ip_addresses) | **GET** /api/client/testing-infrastructure | List all source IP Addresses.
*SuspiciousDomainsApi* | [**get_list_suspicious_domain**](docs/SuspiciousDomainsApi.md#get_list_suspicious_domain) | **GET** /api/client/suspicious-domain/list | List all discovered Suspicious Domains.
*SuspiciousDomainsApi* | [**get_suspicious_domain_details**](docs/SuspiciousDomainsApi.md#get_suspicious_domain_details) | **GET** /api/client/suspicious-domain/show/{id} | Show the details of a specific Suspicious Domain.


## Documentation For Models

 - [Asset](docs/Asset.md)
 - [AssetsListResponse](docs/AssetsListResponse.md)
 - [Causer](docs/Causer.md)
 - [ClientActivityLog](docs/ClientActivityLog.md)
 - [ClientBusinessUnit](docs/ClientBusinessUnit.md)
 - [ClientBusinessUnitData](docs/ClientBusinessUnitData.md)
 - [ClientBusinessUnitDetail](docs/ClientBusinessUnitDetail.md)
 - [ClientCloudStorage](docs/ClientCloudStorage.md)
 - [ClientCloudStorageData](docs/ClientCloudStorageData.md)
 - [ClientContainer](docs/ClientContainer.md)
 - [ClientContainerData](docs/ClientContainerData.md)
 - [ClientDomain](docs/ClientDomain.md)
 - [ClientDomainData](docs/ClientDomainData.md)
 - [ClientFinding](docs/ClientFinding.md)
 - [ClientFindingAssignee](docs/ClientFindingAssignee.md)
 - [ClientFindingData](docs/ClientFindingData.md)
 - [ClientFindingImpactTag](docs/ClientFindingImpactTag.md)
 - [ClientIp](docs/ClientIp.md)
 - [ClientIpData](docs/ClientIpData.md)
 - [ClientIpRange](docs/ClientIpRange.md)
 - [ClientIpRangeData](docs/ClientIpRangeData.md)
 - [ClientMobileApp](docs/ClientMobileApp.md)
 - [ClientMobileAppData](docs/ClientMobileAppData.md)
 - [ClientPort](docs/ClientPort.md)
 - [ClientPortData](docs/ClientPortData.md)
 - [ClientRepository](docs/ClientRepository.md)
 - [ClientRepositoryData](docs/ClientRepositoryData.md)
 - [ClientSaasPlatform](docs/ClientSaasPlatform.md)
 - [ClientSaasPlatformData](docs/ClientSaasPlatformData.md)
 - [ClientSeedData](docs/ClientSeedData.md)
 - [ClientSeedDataData](docs/ClientSeedDataData.md)
 - [ClientServiceInformationResponseData](docs/ClientServiceInformationResponseData.md)
 - [ClientSourceIpsAddresses](docs/ClientSourceIpsAddresses.md)
 - [ClientSubdomain](docs/ClientSubdomain.md)
 - [ClientSubdomainData](docs/ClientSubdomainData.md)
 - [ClientSuspiciousDomainData](docs/ClientSuspiciousDomainData.md)
 - [CreateClientSeedDataRequestBody](docs/CreateClientSeedDataRequestBody.md)
 - [FindingListResponse](docs/FindingListResponse.md)
 - [FindingRetestResponseDto](docs/FindingRetestResponseDto.md)
 - [ForbiddenResponse](docs/ForbiddenResponse.md)
 - [Hunt](docs/Hunt.md)
 - [HuntDetail](docs/HuntDetail.md)
 - [HuntDetailResponse](docs/HuntDetailResponse.md)
 - [Link](docs/Link.md)
 - [Meta](docs/Meta.md)
 - [NotFound](docs/NotFound.md)
 - [PaginatedBusinessUnit](docs/PaginatedBusinessUnit.md)
 - [PaginatedClientActivityLog](docs/PaginatedClientActivityLog.md)
 - [PaginatedClientCloudStorage](docs/PaginatedClientCloudStorage.md)
 - [PaginatedClientContainer](docs/PaginatedClientContainer.md)
 - [PaginatedClientDomain](docs/PaginatedClientDomain.md)
 - [PaginatedClientFindings](docs/PaginatedClientFindings.md)
 - [PaginatedClientIp](docs/PaginatedClientIp.md)
 - [PaginatedClientIpRange](docs/PaginatedClientIpRange.md)
 - [PaginatedClientMobileApp](docs/PaginatedClientMobileApp.md)
 - [PaginatedClientPort](docs/PaginatedClientPort.md)
 - [PaginatedClientRepository](docs/PaginatedClientRepository.md)
 - [PaginatedClientSaasPlatform](docs/PaginatedClientSaasPlatform.md)
 - [PaginatedClientSubdomain](docs/PaginatedClientSubdomain.md)
 - [PaginatedHunts](docs/PaginatedHunts.md)
 - [PaginatedPointOfInterest](docs/PaginatedPointOfInterest.md)
 - [PaginatedServiceInformationResponse](docs/PaginatedServiceInformationResponse.md)
 - [PaginatedServiceListing](docs/PaginatedServiceListing.md)
 - [PaginatedSuspiciousDomain](docs/PaginatedSuspiciousDomain.md)
 - [Pagination](docs/Pagination.md)
 - [PointsOfInterest](docs/PointsOfInterest.md)
 - [Retest](docs/Retest.md)
 - [ServiceInformationAsset](docs/ServiceInformationAsset.md)
 - [ServiceInformationCertificate](docs/ServiceInformationCertificate.md)
 - [ServiceInformationResponse](docs/ServiceInformationResponse.md)
 - [ServiceListing](docs/ServiceListing.md)
 - [ServiceType](docs/ServiceType.md)
 - [SuspiciousDomain](docs/SuspiciousDomain.md)
 - [Technology](docs/Technology.md)
 - [Unauthorized](docs/Unauthorized.md)
 - [UnprocessableContent](docs/UnprocessableContent.md)
 - [UpdateClientFindingStatusRequestBody](docs/UpdateClientFindingStatusRequestBody.md)
 - [UpdateClientLegacyAssetStatusDto](docs/UpdateClientLegacyAssetStatusDto.md)
 - [UpdateClientNextGenAssetStatusDto](docs/UpdateClientNextGenAssetStatusDto.md)
 - [WhoisData](docs/WhoisData.md)
 - [WhoisDataObject](docs/WhoisDataObject.md)
 - [WhoisDataObjectEmails](docs/WhoisDataObjectEmails.md)
 - [WhoisDataObjectNameServers](docs/WhoisDataObjectNameServers.md)
 - [WhoisDataObjectStatus](docs/WhoisDataObjectStatus.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="bearer"></a>
### bearer

- **Type**: Bearer authentication (Hex string)


## Author




