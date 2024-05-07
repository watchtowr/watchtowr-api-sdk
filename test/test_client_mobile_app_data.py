# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api.models.client_mobile_app_data import ClientMobileAppData

class TestClientMobileAppData(unittest.TestCase):
    """ClientMobileAppData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientMobileAppData:
        """Test ClientMobileAppData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientMobileAppData`
        """
        model = ClientMobileAppData()
        if include_optional:
            return ClientMobileAppData(
                data = watchtowr_api.models.client_mobile_app.ClientMobileApp(
                    type = 'mobileApp', 
                    source = 'test', 
                    status = 'verified', 
                    created_at = 2022-02-13T02:10:00.000000Z, 
                    updated_at = 2022-02-13T02:10:00.000000Z, 
                    deleted_at = 2022-02-13T02:10:00.000000Z, 
                    id = 123, 
                    name = 'Internet Banking', 
                    publisher = 'Example Bank Ltd', 
                    platform = 'ios', 
                    app_id = 'com.example.myapp.free.0c0d08db-4d14-3369-ad3d-26e8aa21bcd9', 
                    url = 'https://appstore.apple.com/aaa', 
                    s3path = 'https://s3.amazonaws.com', 
                    business_units = [
                        watchtowr_api.models.client_business_unit.ClientBusinessUnit(
                            id = 1, 
                            name = 'Singapore Business Unit', )
                        ], )
            )
        else:
            return ClientMobileAppData(
                data = watchtowr_api.models.client_mobile_app.ClientMobileApp(
                    type = 'mobileApp', 
                    source = 'test', 
                    status = 'verified', 
                    created_at = 2022-02-13T02:10:00.000000Z, 
                    updated_at = 2022-02-13T02:10:00.000000Z, 
                    deleted_at = 2022-02-13T02:10:00.000000Z, 
                    id = 123, 
                    name = 'Internet Banking', 
                    publisher = 'Example Bank Ltd', 
                    platform = 'ios', 
                    app_id = 'com.example.myapp.free.0c0d08db-4d14-3369-ad3d-26e8aa21bcd9', 
                    url = 'https://appstore.apple.com/aaa', 
                    s3path = 'https://s3.amazonaws.com', 
                    business_units = [
                        watchtowr_api.models.client_business_unit.ClientBusinessUnit(
                            id = 1, 
                            name = 'Singapore Business Unit', )
                        ], ),
        )
        """

    def testClientMobileAppData(self):
        """Test ClientMobileAppData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
