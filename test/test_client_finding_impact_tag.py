# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api.models.client_finding_impact_tag import ClientFindingImpactTag

class TestClientFindingImpactTag(unittest.TestCase):
    """ClientFindingImpactTag unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientFindingImpactTag:
        """Test ClientFindingImpactTag
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientFindingImpactTag`
        """
        model = ClientFindingImpactTag()
        if include_optional:
            return ClientFindingImpactTag(
                id = 1,
                name = 'CISA-KEV'
            )
        else:
            return ClientFindingImpactTag(
                id = 1,
                name = 'CISA-KEV',
        )
        """

    def testClientFindingImpactTag(self):
        """Test ClientFindingImpactTag"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()