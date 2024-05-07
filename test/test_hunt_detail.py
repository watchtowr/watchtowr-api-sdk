# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api.models.hunt_detail import HuntDetail

class TestHuntDetail(unittest.TestCase):
    """HuntDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HuntDetail:
        """Test HuntDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HuntDetail`
        """
        model = HuntDetail()
        if include_optional:
            return HuntDetail(
                id = 1,
                priority = 'high',
                type = 'bespoke',
                created_at = '2023-06-28T02:22:36Z',
                updated_at = '2023-06-28T02:22:36Z',
                total_findings = 1,
                total_assets = 10,
                hunt_request_type = 'Others',
                title = 'Title of hunt',
                description = 'Description of hunt',
                hypothesis = 'Hypothesis of hunt',
                references = ["Ref1Link","Ref2Link","Ref3Link"],
                completed_at = '2023-06-28T02:22:36Z',
                completed_by = 'By someone',
                requested_by = 'Test Name',
                status = 'completed'
            )
        else:
            return HuntDetail(
                id = 1,
                priority = 'high',
                type = 'bespoke',
                created_at = '2023-06-28T02:22:36Z',
                updated_at = '2023-06-28T02:22:36Z',
                total_findings = 1,
                total_assets = 10,
                hunt_request_type = 'Others',
                title = 'Title of hunt',
                description = 'Description of hunt',
                hypothesis = 'Hypothesis of hunt',
                references = ["Ref1Link","Ref2Link","Ref3Link"],
                completed_at = '2023-06-28T02:22:36Z',
                completed_by = 'By someone',
                requested_by = 'Test Name',
                status = 'completed',
        )
        """

    def testHuntDetail(self):
        """Test HuntDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
