# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: 0.9.2
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.package_version import PackageVersion  # noqa: E501
from pollination_sdk.rest import ApiException

class TestPackageVersion(unittest.TestCase):
    """PackageVersion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PackageVersion
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.package_version.PackageVersion()  # noqa: E501
        if include_optional :
            return PackageVersion(
                app_version = null, 
                created = null, 
                deprecated = null, 
                description = null, 
                digest = null, 
                home = null, 
                icon = null, 
                keywords = null, 
                license = null, 
                maintainers = null, 
                manifest = null, 
                name = null, 
                readme = null, 
                slug = null, 
                sources = null, 
                tag = null, 
                type = null, 
                url = null
            )
        else :
            return PackageVersion(
                created = null,
                digest = null,
                name = null,
                tag = null,
                url = null,
        )

    def testPackageVersion(self):
        """Test PackageVersion"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
