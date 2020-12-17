# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.10.13
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.job_argument import JobArgument  # noqa: E501
from pollination_sdk.rest import ApiException

class TestJobArgument(unittest.TestCase):
    """JobArgument unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobArgument
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.job_argument.JobArgument()  # noqa: E501
        if include_optional :
            return JobArgument(
                annotations = {
                    'key' : '0'
                    }, 
                name = '0', 
                type = 'JobArgument', 
                value = '0'
            )
        else :
            return JobArgument(
                name = '0',
                value = '0',
        )

    def testJobArgument(self):
        """Test JobArgument"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
