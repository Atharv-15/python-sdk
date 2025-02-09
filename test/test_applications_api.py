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
from pollination_sdk.api.applications_api import ApplicationsApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestApplicationsApi(unittest.TestCase):
    """ApplicationsApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.applications_api.ApplicationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_application(self):
        """Test case for create_application

        Create an Application  # noqa: E501
        """
        pass

    def test_delete_application(self):
        """Test case for delete_application

        Delete a Application  # noqa: E501
        """
        pass

    def test_delete_application_org_permission(self):
        """Test case for delete_application_org_permission

        Remove a Application permissions  # noqa: E501
        """
        pass

    def test_delete_application_version(self):
        """Test case for delete_application_version

        Remove a Application version  # noqa: E501
        """
        pass

    def test_get_application(self):
        """Test case for get_application

        Get an application  # noqa: E501
        """
        pass

    def test_get_application_access_permissions(self):
        """Test case for get_application_access_permissions

        Get application access permissions  # noqa: E501
        """
        pass

    def test_get_application_deployment(self):
        """Test case for get_application_deployment

        Get application deployment  # noqa: E501
        """
        pass

    def test_get_application_versions(self):
        """Test case for get_application_versions

        Get application versions  # noqa: E501
        """
        pass

    def test_list_applications(self):
        """Test case for list_applications

        List Applications  # noqa: E501
        """
        pass

    def test_update_application(self):
        """Test case for update_application

        Update a Application  # noqa: E501
        """
        pass

    def test_upsert_application_permission(self):
        """Test case for upsert_application_permission

        Upsert a new permission to a application  # noqa: E501
        """
        pass

    def test_upsert_application_version(self):
        """Test case for upsert_application_version

        Upsert a new version to a application  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
