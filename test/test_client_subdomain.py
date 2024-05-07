# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api.models.client_subdomain import ClientSubdomain

class TestClientSubdomain(unittest.TestCase):
    """ClientSubdomain unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientSubdomain:
        """Test ClientSubdomain
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientSubdomain`
        """
        model = ClientSubdomain()
        if include_optional:
            return ClientSubdomain(
                type = 'subdomain',
                source = 'test',
                status = 'verified',
                created_at = 2022-02-13T02:10:00.000000Z,
                updated_at = 2022-02-13T02:10:00.000000Z,
                deleted_at = 2022-02-13T02:10:00.000000Z,
                id = 123,
                name = 'nc.koepp.com',
                business_units = [
                    watchtowr_api.models.client_business_unit.ClientBusinessUnit(
                        id = 1, 
                        name = 'Singapore Business Unit', )
                    ],
                live = True
            )
        else:
            return ClientSubdomain(
                type = 'subdomain',
                source = 'test',
                status = 'verified',
                created_at = 2022-02-13T02:10:00.000000Z,
                updated_at = 2022-02-13T02:10:00.000000Z,
                deleted_at = 2022-02-13T02:10:00.000000Z,
                id = 123,
                name = 'nc.koepp.com',
                business_units = [
                    watchtowr_api.models.client_business_unit.ClientBusinessUnit(
                        id = 1, 
                        name = 'Singapore Business Unit', )
                    ],
                live = True,
        )
        """

    def testClientSubdomain(self):
        """Test ClientSubdomain"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()