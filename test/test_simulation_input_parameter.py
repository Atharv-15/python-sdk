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
from pollination_sdk.models.simulation_input_parameter import SimulationInputParameter  # noqa: E501
from pollination_sdk.rest import ApiException

class TestSimulationInputParameter(unittest.TestCase):
    """SimulationInputParameter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SimulationInputParameter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.simulation_input_parameter.SimulationInputParameter()  # noqa: E501
        if include_optional :
            return SimulationInputParameter(
                name = null, 
                value = null
            )
        else :
            return SimulationInputParameter(
                name = null,
                value = null,
        )

    def testSimulationInputParameter(self):
        """Test SimulationInputParameter"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
