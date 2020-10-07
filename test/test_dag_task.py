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
from pollination_sdk.models.dag_task import DAGTask  # noqa: E501
from pollination_sdk.rest import ApiException

class TestDAGTask(unittest.TestCase):
    """DAGTask unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DAGTask
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.dag_task.DAGTask()  # noqa: E501
        if include_optional :
            return DAGTask(
                arguments = null, 
                dependencies = null, 
                loop = null, 
                name = null, 
                outputs = null, 
                sub_folder = null, 
                template = null
            )
        else :
            return DAGTask(
                name = null,
                template = null,
        )

    def testDAGTask(self):
        """Test DAGTask"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
