# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.27.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.license_public import LicensePublic  # noqa: E501
from pollination_sdk.rest import ApiException

class TestLicensePublic(unittest.TestCase):
    """LicensePublic unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LicensePublic
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.license_public.LicensePublic()  # noqa: E501
        if include_optional :
            return LicensePublic(
                allowed_activations = 56, 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                id = '0', 
                key = '0', 
                lease_duration = 56, 
                metadata = [
                    pollination_sdk.models.metadata.Metadata(
                        id = '0', 
                        key = '0', 
                        value = '0', 
                        visible = True, )
                    ], 
                notes = '0', 
                product_id = '0', 
                revoked = True, 
                server_sync_grace_period = 56, 
                server_sync_interval = 56, 
                suspended = True, 
                total_activations = 56, 
                total_deactivations = 56, 
                type = 'node-locked', 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                validity = 56
            )
        else :
            return LicensePublic(
                allowed_activations = 56,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '0',
                key = '0',
                lease_duration = 56,
                metadata = [
                    pollination_sdk.models.metadata.Metadata(
                        id = '0', 
                        key = '0', 
                        value = '0', 
                        visible = True, )
                    ],
                product_id = '0',
                revoked = True,
                server_sync_grace_period = 56,
                server_sync_interval = 56,
                suspended = True,
                total_activations = 56,
                total_deactivations = 56,
                type = 'node-locked',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                validity = 56,
        )

    def testLicensePublic(self):
        """Test LicensePublic"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
