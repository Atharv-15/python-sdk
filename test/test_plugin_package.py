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
from pollination_sdk.models.plugin_package import PluginPackage  # noqa: E501
from pollination_sdk.rest import ApiException

class TestPluginPackage(unittest.TestCase):
    """PluginPackage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PluginPackage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.plugin_package.PluginPackage()  # noqa: E501
        if include_optional :
            return PluginPackage(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                description = '0', 
                digest = '0', 
                icon = '0', 
                keywords = [
                    '0'
                    ], 
                manifest = pollination_sdk.models.plugin.Plugin(
                    annotations = {
                        'key' : '0'
                        }, 
                    api_version = 'v1beta1', 
                    config = null, 
                    functions = [
                        pollination_sdk.models.function.Function(
                            annotations = {
                                'key' : '0'
                                }, 
                            command = '0', 
                            description = '0', 
                            inputs = [
                                null
                                ], 
                            name = '0', 
                            outputs = [
                                null
                                ], 
                            type = 'Function', )
                        ], 
                    metadata = null, 
                    type = 'Plugin', ), 
                readme = '# Daylight Factor 
 This recipe runs a daylight factor simulation.', 
                tag = '0'
            )
        else :
            return PluginPackage(
                digest = '0',
                manifest = pollination_sdk.models.plugin.Plugin(
                    annotations = {
                        'key' : '0'
                        }, 
                    api_version = 'v1beta1', 
                    config = null, 
                    functions = [
                        pollination_sdk.models.function.Function(
                            annotations = {
                                'key' : '0'
                                }, 
                            command = '0', 
                            description = '0', 
                            inputs = [
                                null
                                ], 
                            name = '0', 
                            outputs = [
                                null
                                ], 
                            type = 'Function', )
                        ], 
                    metadata = null, 
                    type = 'Plugin', ),
                tag = '0',
        )

    def testPluginPackage(self):
        """Test PluginPackage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
