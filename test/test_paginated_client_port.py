# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api.models.paginated_client_port import PaginatedClientPort

class TestPaginatedClientPort(unittest.TestCase):
    """PaginatedClientPort unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedClientPort:
        """Test PaginatedClientPort
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedClientPort`
        """
        model = PaginatedClientPort()
        if include_optional:
            return PaginatedClientPort(
                data = [
                    watchtowr_api.models.client_port.ClientPort(
                        type = 'TCP', 
                        status = 'verified', 
                        created_at = 2022-02-13T02:10:00.000000Z, 
                        updated_at = 2022-02-13T02:10:00.000000Z, 
                        deleted_at = 2022-02-13T02:10:00.000000Z, 
                        id = 123, 
                        ip = '45.33.32.156', 
                        ip_id = 333, 
                        port = 22, 
                        banner = 'OpenSSH6.6.1p1 Ubuntu 2ubuntu2.13Ubuntu Linux; protocol 2.0', 
                        service = 'ssh', 
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
            return PaginatedClientPort(
                data = [
                    watchtowr_api.models.client_port.ClientPort(
                        type = 'TCP', 
                        status = 'verified', 
                        created_at = 2022-02-13T02:10:00.000000Z, 
                        updated_at = 2022-02-13T02:10:00.000000Z, 
                        deleted_at = 2022-02-13T02:10:00.000000Z, 
                        id = 123, 
                        ip = '45.33.32.156', 
                        ip_id = 333, 
                        port = 22, 
                        banner = 'OpenSSH6.6.1p1 Ubuntu 2ubuntu2.13Ubuntu Linux; protocol 2.0', 
                        service = 'ssh', 
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

    def testPaginatedClientPort(self):
        """Test PaginatedClientPort"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
