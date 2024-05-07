# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api.models.retest import Retest

class TestRetest(unittest.TestCase):
    """Retest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Retest:
        """Test Retest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Retest`
        """
        model = Retest()
        if include_optional:
            return Retest(
                retest_remaining = 1,
                current_retest = watchtowr_api.models.finding_retest_response_dto.FindingRetestResponseDto(
                    requested_by = 'Requested by user', 
                    requested_at = '2024-01-29T08:05:09Z', 
                    retest_status = 'success', 
                    status_occurred_at = '2024-01-29T08:05:09Z', 
                    completed_at = '2024-01-29T08:05:09Z', 
                    evidence = 'Evidence for retest', )
            )
        else:
            return Retest(
                current_retest = watchtowr_api.models.finding_retest_response_dto.FindingRetestResponseDto(
                    requested_by = 'Requested by user', 
                    requested_at = '2024-01-29T08:05:09Z', 
                    retest_status = 'success', 
                    status_occurred_at = '2024-01-29T08:05:09Z', 
                    completed_at = '2024-01-29T08:05:09Z', 
                    evidence = 'Evidence for retest', ),
        )
        """

    def testRetest(self):
        """Test Retest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()