# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api.models.causer import Causer

class TestCauser(unittest.TestCase):
    """Causer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Causer:
        """Test Causer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Causer`
        """
        model = Causer()
        if include_optional:
            return Causer(
                id = 1,
                name = Example
            )
        else:
            return Causer(
                id = 1,
                name = Example,
        )
        """

    def testCauser(self):
        """Test Causer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
