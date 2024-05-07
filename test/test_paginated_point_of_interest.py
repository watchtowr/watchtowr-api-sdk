# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api.models.paginated_point_of_interest import PaginatedPointOfInterest

class TestPaginatedPointOfInterest(unittest.TestCase):
    """PaginatedPointOfInterest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedPointOfInterest:
        """Test PaginatedPointOfInterest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedPointOfInterest`
        """
        model = PaginatedPointOfInterest()
        if include_optional:
            return PaginatedPointOfInterest(
                data = [
                    watchtowr_api.models.points_of_interest.PointsOfInterest(
                        id = 1, 
                        name = 'phpMyAdmin', 
                        type = 'admin-panel', 
                        url = 'http://example.com/phpmyadmin', 
                        discovery_tool_id = 'test-id', 
                        discovery_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        asset_id = 1, 
                        asset_name = '192.168.1.1', 
                        asset_type = 'ip', 
                        business_units = [
                            watchtowr_api.models.client_business_unit.ClientBusinessUnit(
                                id = 1, 
                                name = 'Singapore Business Unit', )
                            ], 
                        last_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                meta = watchtowr_api.models.meta.Meta(
                    pagination = {"total":20,"count":10,"per_page":10,"current_page":1,"total_pages":2,"links":{"previous":"url","next":"url"}}, )
            )
        else:
            return PaginatedPointOfInterest(
                data = [
                    watchtowr_api.models.points_of_interest.PointsOfInterest(
                        id = 1, 
                        name = 'phpMyAdmin', 
                        type = 'admin-panel', 
                        url = 'http://example.com/phpmyadmin', 
                        discovery_tool_id = 'test-id', 
                        discovery_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        asset_id = 1, 
                        asset_name = '192.168.1.1', 
                        asset_type = 'ip', 
                        business_units = [
                            watchtowr_api.models.client_business_unit.ClientBusinessUnit(
                                id = 1, 
                                name = 'Singapore Business Unit', )
                            ], 
                        last_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                meta = watchtowr_api.models.meta.Meta(
                    pagination = {"total":20,"count":10,"per_page":10,"current_page":1,"total_pages":2,"links":{"previous":"url","next":"url"}}, ),
        )
        """

    def testPaginatedPointOfInterest(self):
        """Test PaginatedPointOfInterest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
