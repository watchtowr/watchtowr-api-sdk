# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api.api.asset_saa_s_platforms_api import AssetSaaSPlatformsApi


class TestAssetSaaSPlatformsApi(unittest.TestCase):
    """AssetSaaSPlatformsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AssetSaaSPlatformsApi()

    def tearDown(self) -> None:
        pass

    def test_get_asset_saas_platform_details(self) -> None:
        """Test case for get_asset_saas_platform_details

        Show the details of a specific SaaS Platform.
        """
        pass

    def test_get_list_asset_saas_platforms(self) -> None:
        """Test case for get_list_asset_saas_platforms

        List all discovered SaaS Platforms, ordered by date identified.
        """
        pass

    def test_update_asset_saas_platform_status(self) -> None:
        """Test case for update_asset_saas_platform_status

        Update status of a specific SaaS platform asset.
        """
        pass


if __name__ == '__main__':
    unittest.main()