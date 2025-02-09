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

import pollination_sdk
from pollination_sdk.api.plugins_api import PluginsApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestPluginsApi(unittest.TestCase):
    """PluginsApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.plugins_api.PluginsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_plugin(self):
        """Test case for create_plugin

        Create a Plugin  # noqa: E501
        """
        pass

    def test_create_plugin_package(self):
        """Test case for create_plugin_package

        Create a new Plugin package  # noqa: E501
        """
        pass

    def test_delete_plugin(self):
        """Test case for delete_plugin

        Delete a Plugin  # noqa: E501
        """
        pass

    def test_delete_plugin_org_permission(self):
        """Test case for delete_plugin_org_permission

        Remove a Repository permissions  # noqa: E501
        """
        pass

    def test_get_plugin(self):
        """Test case for get_plugin

        Get a plugin  # noqa: E501
        """
        pass

    def test_get_plugin_access_permissions(self):
        """Test case for get_plugin_access_permissions

        Get plugin access permissions  # noqa: E501
        """
        pass

    def test_get_plugin_by_tag(self):
        """Test case for get_plugin_by_tag

        Get a plugin tag  # noqa: E501
        """
        pass

    def test_list_plugin_tags(self):
        """Test case for list_plugin_tags

        Get a plugin tags  # noqa: E501
        """
        pass

    def test_list_plugins(self):
        """Test case for list_plugins

        List plugins  # noqa: E501
        """
        pass

    def test_update_plugin(self):
        """Test case for update_plugin

        Update a Plugin  # noqa: E501
        """
        pass

    def test_upsert_plugin_permission(self):
        """Test case for upsert_plugin_permission

        Upsert a new permission to a plugin  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
