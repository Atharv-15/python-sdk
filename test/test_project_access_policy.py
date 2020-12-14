# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.10.11
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.project_access_policy import ProjectAccessPolicy  # noqa: E501
from pollination_sdk.rest import ApiException

class TestProjectAccessPolicy(unittest.TestCase):
    """ProjectAccessPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectAccessPolicy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.project_access_policy.ProjectAccessPolicy()  # noqa: E501
        if include_optional :
            return ProjectAccessPolicy(
                permission = 'write', 
                subject = null
            )
        else :
            return ProjectAccessPolicy(
                permission = 'write',
                subject = null,
        )

    def testProjectAccessPolicy(self):
        """Test ProjectAccessPolicy"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
