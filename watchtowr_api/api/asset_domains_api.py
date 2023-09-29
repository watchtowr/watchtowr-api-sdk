# coding: utf-8

"""
    watchTowr Platform Client API SDK

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from datetime import datetime

from pydantic import Field, StrictFloat, StrictInt, StrictStr, conlist

from typing import Optional, Union

from watchtowr_api.models.client_domain_data import ClientDomainData
from watchtowr_api.models.paginated_client_domain import PaginatedClientDomain

from watchtowr_api.api_client import ApiClient
from watchtowr_api.api_response import ApiResponse
from watchtowr_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AssetDomainsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_asset_domain_details(self, api_token : StrictStr, **kwargs) -> ClientDomainData:  # noqa: E501
        """Show the details of a specific domain asset.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_asset_domain_details(api_token, async_req=True)
        >>> result = thread.get()

        :param api_token: (required)
        :type api_token: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ClientDomainData
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_asset_domain_details_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_asset_domain_details_with_http_info(api_token, **kwargs)  # noqa: E501

    @validate_arguments
    def get_asset_domain_details_with_http_info(self, api_token : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """Show the details of a specific domain asset.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_asset_domain_details_with_http_info(api_token, async_req=True)
        >>> result = thread.get()

        :param api_token: (required)
        :type api_token: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ClientDomainData, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'api_token'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_asset_domain_details" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('api_token') is not None:  # noqa: E501
            _query_params.append(('api_token', _params['api_token']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['bearer']  # noqa: E501

        _response_types_map = {
            '200': "ClientDomainData",
            '401': "Unauthorized",
            '404': "NotFound",
        }

        return self.api_client.call_api(
            '/api/client/assets/domain/show/{id}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_list_asset_domains(self, asset_name : Annotated[Optional[StrictStr], Field(description="Asset name/SaaS URL/IP/IP Range/Port")] = None, statuses : Annotated[Optional[conlist(StrictStr)], Field(description="Asset statuses")] = None, business_unit_ids : Annotated[Optional[StrictStr], Field(description="Comma separated list of business unit IDs")] = None, page : Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Pagination page")] = None, created_from : Annotated[Optional[datetime], Field(description="created_at Date Range Beginning")] = None, created_to : Annotated[Optional[datetime], Field(description="created_at Date Range Ending")] = None, updated_from : Annotated[Optional[datetime], Field(description="updated_at Date Range Beginning")] = None, updated_to : Annotated[Optional[datetime], Field(description="updated_at Date Range Ending")] = None, **kwargs) -> PaginatedClientDomain:  # noqa: E501
        """List all discovered domains, ordered by date identified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_list_asset_domains(asset_name, statuses, business_unit_ids, page, created_from, created_to, updated_from, updated_to, async_req=True)
        >>> result = thread.get()

        :param asset_name: Asset name/SaaS URL/IP/IP Range/Port
        :type asset_name: str
        :param statuses: Asset statuses
        :type statuses: List[str]
        :param business_unit_ids: Comma separated list of business unit IDs
        :type business_unit_ids: str
        :param page: Pagination page
        :type page: float
        :param created_from: created_at Date Range Beginning
        :type created_from: datetime
        :param created_to: created_at Date Range Ending
        :type created_to: datetime
        :param updated_from: updated_at Date Range Beginning
        :type updated_from: datetime
        :param updated_to: updated_at Date Range Ending
        :type updated_to: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PaginatedClientDomain
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_list_asset_domains_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_list_asset_domains_with_http_info(asset_name, statuses, business_unit_ids, page, created_from, created_to, updated_from, updated_to, **kwargs)  # noqa: E501

    @validate_arguments
    def get_list_asset_domains_with_http_info(self, asset_name : Annotated[Optional[StrictStr], Field(description="Asset name/SaaS URL/IP/IP Range/Port")] = None, statuses : Annotated[Optional[conlist(StrictStr)], Field(description="Asset statuses")] = None, business_unit_ids : Annotated[Optional[StrictStr], Field(description="Comma separated list of business unit IDs")] = None, page : Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Pagination page")] = None, created_from : Annotated[Optional[datetime], Field(description="created_at Date Range Beginning")] = None, created_to : Annotated[Optional[datetime], Field(description="created_at Date Range Ending")] = None, updated_from : Annotated[Optional[datetime], Field(description="updated_at Date Range Beginning")] = None, updated_to : Annotated[Optional[datetime], Field(description="updated_at Date Range Ending")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List all discovered domains, ordered by date identified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_list_asset_domains_with_http_info(asset_name, statuses, business_unit_ids, page, created_from, created_to, updated_from, updated_to, async_req=True)
        >>> result = thread.get()

        :param asset_name: Asset name/SaaS URL/IP/IP Range/Port
        :type asset_name: str
        :param statuses: Asset statuses
        :type statuses: List[str]
        :param business_unit_ids: Comma separated list of business unit IDs
        :type business_unit_ids: str
        :param page: Pagination page
        :type page: float
        :param created_from: created_at Date Range Beginning
        :type created_from: datetime
        :param created_to: created_at Date Range Ending
        :type created_to: datetime
        :param updated_from: updated_at Date Range Beginning
        :type updated_from: datetime
        :param updated_to: updated_at Date Range Ending
        :type updated_to: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PaginatedClientDomain, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'asset_name',
            'statuses',
            'business_unit_ids',
            'page',
            'created_from',
            'created_to',
            'updated_from',
            'updated_to'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_list_asset_domains" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('asset_name') is not None:  # noqa: E501
            _query_params.append(('assetName', _params['asset_name']))

        if _params.get('statuses') is not None:  # noqa: E501
            _query_params.append(('statuses', _params['statuses']))
            _collection_formats['statuses'] = 'multi'

        if _params.get('business_unit_ids') is not None:  # noqa: E501
            _query_params.append(('businessUnitIds', _params['business_unit_ids']))

        if _params.get('page') is not None:  # noqa: E501
            _query_params.append(('page', _params['page']))

        if _params.get('created_from') is not None:  # noqa: E501
            if isinstance(_params['created_from'], datetime):
                _query_params.append(('created_from', _params['created_from'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('created_from', _params['created_from']))

        if _params.get('created_to') is not None:  # noqa: E501
            if isinstance(_params['created_to'], datetime):
                _query_params.append(('created_to', _params['created_to'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('created_to', _params['created_to']))

        if _params.get('updated_from') is not None:  # noqa: E501
            if isinstance(_params['updated_from'], datetime):
                _query_params.append(('updated_from', _params['updated_from'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('updated_from', _params['updated_from']))

        if _params.get('updated_to') is not None:  # noqa: E501
            if isinstance(_params['updated_to'], datetime):
                _query_params.append(('updated_to', _params['updated_to'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('updated_to', _params['updated_to']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['bearer']  # noqa: E501

        _response_types_map = {
            '200': "PaginatedClientDomain",
            '401': "Unauthorized",
        }

        return self.api_client.call_api(
            '/api/client/assets/domain/list', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
