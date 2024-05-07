# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api.models.paginated_client_activity_log import PaginatedClientActivityLog

class TestPaginatedClientActivityLog(unittest.TestCase):
    """PaginatedClientActivityLog unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedClientActivityLog:
        """Test PaginatedClientActivityLog
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedClientActivityLog`
        """
        model = PaginatedClientActivityLog()
        if include_optional:
            return PaginatedClientActivityLog(
                data = [{"id":128462,"description":"Successful login from 127.0.0.1","type":"Successful Login","properties":{"attributes":{"ip_address":"127.0.0.1","user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}},"created_at":"2024-01-02T09:19:12.000Z","caused_by":{"id":80,"name":"Example user name 1"}},{"id":128631,"description":"Executive Summary Report generated","type":"Report Generated","properties":{"attributes":{}},"created_at":"2024-01-23T07:53:58.000Z","caused_by":{"id":53,"name":"Example user name 2"}}],
                meta = watchtowr_api.models.meta.Meta(
                    pagination = {"total":20,"count":10,"per_page":10,"current_page":1,"total_pages":2,"links":{"previous":"url","next":"url"}}, )
            )
        else:
            return PaginatedClientActivityLog(
                data = [{"id":128462,"description":"Successful login from 127.0.0.1","type":"Successful Login","properties":{"attributes":{"ip_address":"127.0.0.1","user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}},"created_at":"2024-01-02T09:19:12.000Z","caused_by":{"id":80,"name":"Example user name 1"}},{"id":128631,"description":"Executive Summary Report generated","type":"Report Generated","properties":{"attributes":{}},"created_at":"2024-01-23T07:53:58.000Z","caused_by":{"id":53,"name":"Example user name 2"}}],
                meta = watchtowr_api.models.meta.Meta(
                    pagination = {"total":20,"count":10,"per_page":10,"current_page":1,"total_pages":2,"links":{"previous":"url","next":"url"}}, ),
        )
        """

    def testPaginatedClientActivityLog(self):
        """Test PaginatedClientActivityLog"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()