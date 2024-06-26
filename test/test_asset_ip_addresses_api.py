# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api.api.asset_ip_addresses_api import AssetIPAddressesApi


class TestAssetIPAddressesApi(unittest.TestCase):
    """AssetIPAddressesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AssetIPAddressesApi()

    def tearDown(self) -> None:
        pass

    def test_get_asset_ip_details(self) -> None:
        """Test case for get_asset_ip_details

        Show the details of a specific IP Address asset.
        """
        pass

    def test_get_asset_ip_port_details(self) -> None:
        """Test case for get_asset_ip_port_details

        Show the details of a specific port asset belonging to an IP Address.
        """
        pass

    def test_get_asset_ip_ports(self) -> None:
        """Test case for get_asset_ip_ports

        List all discovered ports belonging to an IP Address, ordered by date identified.
        """
        pass

    def test_get_list_asset_ips(self) -> None:
        """Test case for get_list_asset_ips

        List all discovered IP Addresses, ordered by date identified.
        """
        pass

    def test_update_asset_ip_status(self) -> None:
        """Test case for update_asset_ip_status

        Update status of a specific IP Address asset.
        """
        pass


if __name__ == '__main__':
    unittest.main()
