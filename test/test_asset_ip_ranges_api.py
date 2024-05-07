# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api.api.asset_ip_ranges_api import AssetIPRangesApi


class TestAssetIPRangesApi(unittest.TestCase):
    """AssetIPRangesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AssetIPRangesApi()

    def tearDown(self) -> None:
        pass

    def test_get_asset_iprange_details(self) -> None:
        """Test case for get_asset_iprange_details

        Show the details of a specific IP Range.
        """
        pass

    def test_get_list_asset_ipranges(self) -> None:
        """Test case for get_list_asset_ipranges

        List all discovered IP Ranges, ordered by date identified.
        """
        pass

    def test_update_asset_ip_range_status(self) -> None:
        """Test case for update_asset_ip_range_status

        Update status of a specific IP range asset.
        """
        pass


if __name__ == '__main__':
    unittest.main()