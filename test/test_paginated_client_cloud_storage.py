# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api.models.paginated_client_cloud_storage import PaginatedClientCloudStorage

class TestPaginatedClientCloudStorage(unittest.TestCase):
    """PaginatedClientCloudStorage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedClientCloudStorage:
        """Test PaginatedClientCloudStorage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedClientCloudStorage`
        """
        model = PaginatedClientCloudStorage()
        if include_optional:
            return PaginatedClientCloudStorage(
                data = [
                    watchtowr_api.models.client_cloud_storage.ClientCloudStorage(
                        type = 'cloudStorage', 
                        source = 'module-adversarysight-asset-discovery', 
                        status = 'verified', 
                        created_at = 2022-02-13T02:10:00.000000Z, 
                        updated_at = 2022-02-13T02:10:00.000000Z, 
                        deleted_at = 2022-02-13T02:10:00.000000Z, 
                        id = 123, 
                        name = 'CloudStorage 1234', 
                        platform = 'awss3', 
                        url = 'https://test.s3.amazonaws.com', 
                        business_units = [
                            watchtowr_api.models.client_business_unit.ClientBusinessUnit(
                                id = 1, 
                                name = 'Singapore Business Unit', )
                            ], )
                    ],
                meta = watchtowr_api.models.meta.Meta(
                    pagination = {"total":20,"count":10,"per_page":10,"current_page":1,"total_pages":2,"links":{"previous":"url","next":"url"}}, )
            )
        else:
            return PaginatedClientCloudStorage(
                data = [
                    watchtowr_api.models.client_cloud_storage.ClientCloudStorage(
                        type = 'cloudStorage', 
                        source = 'module-adversarysight-asset-discovery', 
                        status = 'verified', 
                        created_at = 2022-02-13T02:10:00.000000Z, 
                        updated_at = 2022-02-13T02:10:00.000000Z, 
                        deleted_at = 2022-02-13T02:10:00.000000Z, 
                        id = 123, 
                        name = 'CloudStorage 1234', 
                        platform = 'awss3', 
                        url = 'https://test.s3.amazonaws.com', 
                        business_units = [
                            watchtowr_api.models.client_business_unit.ClientBusinessUnit(
                                id = 1, 
                                name = 'Singapore Business Unit', )
                            ], )
                    ],
                meta = watchtowr_api.models.meta.Meta(
                    pagination = {"total":20,"count":10,"per_page":10,"current_page":1,"total_pages":2,"links":{"previous":"url","next":"url"}}, ),
        )
        """

    def testPaginatedClientCloudStorage(self):
        """Test PaginatedClientCloudStorage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
