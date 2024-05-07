# coding: utf-8

"""
    watchTowr Platform Client API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api.models.suspicious_domain import SuspiciousDomain

class TestSuspiciousDomain(unittest.TestCase):
    """SuspiciousDomain unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SuspiciousDomain:
        """Test SuspiciousDomain
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SuspiciousDomain`
        """
        model = SuspiciousDomain()
        if include_optional:
            return SuspiciousDomain(
                id = 1,
                name = 'example.com',
                discovery_reason = 'Example reason',
                status = 'legitimate',
                whois_data = [
                    watchtowr_api.models.whois_data.WhoisData(
                        id = 1, 
                        data = watchtowr_api.models.whois_data_object.WhoisDataObject(
                            org = 'ACME Corp', 
                            city = 'Singapore', 
                            name = 'John Doe', 
                            state = 'Singapore', 
                            dnssec = 'unsigned', 
                            emails = null, 
                            status = null, 
                            address = 'Singapore 123456', 
                            country = 'Singapore', 
                            zipcode = '123456', 
                            registrar = 'GoDaddy.com, LLC', 
                            domain_name = 'example.com', 
                            name_servers = null, 
                            referral_url = '', 
                            whois_server = 'whois.godaddy.com', 
                            creation_date = '1989-07-15T04:00:00', 
                            expiration_date = '2030-07-15T04:00:00', ), 
                        raw = 'Domain Name: example.com
Registry Domain ID: 5066842_DOMAIN_COM-VRSN
Registrar WHOIS Server: whois.godaddy.com
Registrar URL: http://www.example.com
Updated Date: 2023-04-13T19:03:58Z
Creation Date: 1997-06-18T04:00:00Z
Registrar Registration Expiration Date: 2027-06-17T04:00:00Z
            ...', )
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return SuspiciousDomain(
                id = 1,
                name = 'example.com',
                discovery_reason = 'Example reason',
                status = 'legitimate',
                whois_data = [
                    watchtowr_api.models.whois_data.WhoisData(
                        id = 1, 
                        data = watchtowr_api.models.whois_data_object.WhoisDataObject(
                            org = 'ACME Corp', 
                            city = 'Singapore', 
                            name = 'John Doe', 
                            state = 'Singapore', 
                            dnssec = 'unsigned', 
                            emails = null, 
                            status = null, 
                            address = 'Singapore 123456', 
                            country = 'Singapore', 
                            zipcode = '123456', 
                            registrar = 'GoDaddy.com, LLC', 
                            domain_name = 'example.com', 
                            name_servers = null, 
                            referral_url = '', 
                            whois_server = 'whois.godaddy.com', 
                            creation_date = '1989-07-15T04:00:00', 
                            expiration_date = '2030-07-15T04:00:00', ), 
                        raw = 'Domain Name: example.com
Registry Domain ID: 5066842_DOMAIN_COM-VRSN
Registrar WHOIS Server: whois.godaddy.com
Registrar URL: http://www.example.com
Updated Date: 2023-04-13T19:03:58Z
Creation Date: 1997-06-18T04:00:00Z
Registrar Registration Expiration Date: 2027-06-17T04:00:00Z
            ...', )
                    ],
        )
        """

    def testSuspiciousDomain(self):
        """Test SuspiciousDomain"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
