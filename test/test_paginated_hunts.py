# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api.models.paginated_hunts import PaginatedHunts

class TestPaginatedHunts(unittest.TestCase):
    """PaginatedHunts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedHunts:
        """Test PaginatedHunts
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedHunts`
        """
        model = PaginatedHunts()
        if include_optional:
            return PaginatedHunts(
                data = [
                    watchtowr_api.models.hunt.Hunt(
                        id = 1, 
                        priority = 'high', 
                        type = 'bespoke', 
                        created_at = '2023-06-28T02:22:36Z', 
                        updated_at = '2023-06-28T02:22:36Z', 
                        total_findings = 1, 
                        total_assets = 10, 
                        hunt_request_type = 'Others', 
                        title = '...', 
                        status = 'completed', )
                    ],
                meta = watchtowr_api.models.meta.Meta(
                    pagination = {"total":20,"count":10,"per_page":10,"current_page":1,"total_pages":2,"links":{"previous":"url","next":"url"}}, )
            )
        else:
            return PaginatedHunts(
                data = [
                    watchtowr_api.models.hunt.Hunt(
                        id = 1, 
                        priority = 'high', 
                        type = 'bespoke', 
                        created_at = '2023-06-28T02:22:36Z', 
                        updated_at = '2023-06-28T02:22:36Z', 
                        total_findings = 1, 
                        total_assets = 10, 
                        hunt_request_type = 'Others', 
                        title = '...', 
                        status = 'completed', )
                    ],
                meta = watchtowr_api.models.meta.Meta(
                    pagination = {"total":20,"count":10,"per_page":10,"current_page":1,"total_pages":2,"links":{"previous":"url","next":"url"}}, ),
        )
        """

    def testPaginatedHunts(self):
        """Test PaginatedHunts"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()