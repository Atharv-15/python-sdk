# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: 0.10.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.input_artifact_reference import InputArtifactReference  # noqa: E501
from pollination_sdk.rest import ApiException

class TestInputArtifactReference(unittest.TestCase):
    """InputArtifactReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InputArtifactReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.input_artifact_reference.InputArtifactReference()  # noqa: E501
        if include_optional :
            return InputArtifactReference(
                type = 'inputs', 
                variable = '0'
            )
        else :
            return InputArtifactReference(
                variable = '0',
        )

    def testInputArtifactReference(self):
        """Test InputArtifactReference"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
