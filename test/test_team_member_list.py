# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.16.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.team_member_list import TeamMemberList  # noqa: E501
from pollination_sdk.rest import ApiException

class TestTeamMemberList(unittest.TestCase):
    """TeamMemberList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TeamMemberList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.team_member_list.TeamMemberList()  # noqa: E501
        if include_optional :
            return TeamMemberList(
                next_page = 56, 
                page = 56, 
                page_count = 56, 
                per_page = 56, 
                resources = [
                    pollination_sdk.models.team_member.TeamMember(
                        role = member, 
                        user = null, )
                    ], 
                total_count = 56
            )
        else :
            return TeamMemberList(
                page = 56,
                page_count = 56,
                per_page = 56,
                resources = [
                    pollination_sdk.models.team_member.TeamMember(
                        role = member, 
                        user = null, )
                    ],
                total_count = 56,
        )

    def testTeamMemberList(self):
        """Test TeamMemberList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
