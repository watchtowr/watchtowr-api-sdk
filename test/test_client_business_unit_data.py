# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api.models.client_business_unit_data import ClientBusinessUnitData

class TestClientBusinessUnitData(unittest.TestCase):
    """ClientBusinessUnitData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientBusinessUnitData:
        """Test ClientBusinessUnitData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientBusinessUnitData`
        """
        model = ClientBusinessUnitData()
        if include_optional:
            return ClientBusinessUnitData(
                data = watchtowr_api.models.client_business_unit_detail.ClientBusinessUnitDetail(
                    id = 1, 
                    name = 'Singapore Business Unit', 
                    description = 'Singapore based assets', 
                    created_at = 2022-02-13T02:10:00.000000Z, )
            )
        else:
            return ClientBusinessUnitData(
                data = watchtowr_api.models.client_business_unit_detail.ClientBusinessUnitDetail(
                    id = 1, 
                    name = 'Singapore Business Unit', 
                    description = 'Singapore based assets', 
                    created_at = 2022-02-13T02:10:00.000000Z, ),
        )
        """

    def testClientBusinessUnitData(self):
        """Test ClientBusinessUnitData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()