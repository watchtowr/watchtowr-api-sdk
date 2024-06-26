# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api.models.client_subdomain_data import ClientSubdomainData

class TestClientSubdomainData(unittest.TestCase):
    """ClientSubdomainData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientSubdomainData:
        """Test ClientSubdomainData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientSubdomainData`
        """
        model = ClientSubdomainData()
        if include_optional:
            return ClientSubdomainData(
                data = watchtowr_api.models.client_subdomain.ClientSubdomain(
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
                    live = True, )
            )
        else:
            return ClientSubdomainData(
                data = watchtowr_api.models.client_subdomain.ClientSubdomain(
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
                    live = True, ),
        )
        """

    def testClientSubdomainData(self):
        """Test ClientSubdomainData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
