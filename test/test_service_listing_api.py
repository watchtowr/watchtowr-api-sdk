# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api.api.service_listing_api import ServiceListingApi


class TestServiceListingApi(unittest.TestCase):
    """ServiceListingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ServiceListingApi()

    def tearDown(self) -> None:
        pass

    def test_get_list_service_listing(self) -> None:
        """Test case for get_list_service_listing

        List all discovered services.
        """
        pass


if __name__ == '__main__':
    unittest.main()