# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api.models.client_service_information_response_data import ClientServiceInformationResponseData

class TestClientServiceInformationResponseData(unittest.TestCase):
    """ClientServiceInformationResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientServiceInformationResponseData:
        """Test ClientServiceInformationResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientServiceInformationResponseData`
        """
        model = ClientServiceInformationResponseData()
        if include_optional:
            return ClientServiceInformationResponseData(
                data = watchtowr_api.models.service_information_response.ServiceInformationResponse(
                    id = 1, 
                    response = 'example', 
                    certificate = watchtowr_api.models.service_information_certificate.ServiceInformationCertificate(
                        id = 1, 
                        subject_common_name = 'example.com', 
                        subject_organisation = 'example', 
                        subject_alt_names = ["example.com"], 
                        subject_country = 'SG', 
                        issuer_common_name = 'example', 
                        issuer_organisation = 'example', 
                        issuer_country = 'SG', 
                        fingerprint = 'example', 
                        public_key_info_alg = 'example', 
                        public_key_info_size = 'example', 
                        status = 'Expired', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    asset = watchtowr_api.models.service_information_asset.ServiceInformationAsset(
                        id = 1, 
                        name = '192.168.1.1', 
                        type = 'ip', 
                        business_units = [
                            watchtowr_api.models.client_business_unit.ClientBusinessUnit(
                                id = 1, 
                                name = 'Singapore Business Unit', )
                            ], ), )
            )
        else:
            return ClientServiceInformationResponseData(
                data = watchtowr_api.models.service_information_response.ServiceInformationResponse(
                    id = 1, 
                    response = 'example', 
                    certificate = watchtowr_api.models.service_information_certificate.ServiceInformationCertificate(
                        id = 1, 
                        subject_common_name = 'example.com', 
                        subject_organisation = 'example', 
                        subject_alt_names = ["example.com"], 
                        subject_country = 'SG', 
                        issuer_common_name = 'example', 
                        issuer_organisation = 'example', 
                        issuer_country = 'SG', 
                        fingerprint = 'example', 
                        public_key_info_alg = 'example', 
                        public_key_info_size = 'example', 
                        status = 'Expired', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    asset = watchtowr_api.models.service_information_asset.ServiceInformationAsset(
                        id = 1, 
                        name = '192.168.1.1', 
                        type = 'ip', 
                        business_units = [
                            watchtowr_api.models.client_business_unit.ClientBusinessUnit(
                                id = 1, 
                                name = 'Singapore Business Unit', )
                            ], ), ),
        )
        """

    def testClientServiceInformationResponseData(self):
        """Test ClientServiceInformationResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()