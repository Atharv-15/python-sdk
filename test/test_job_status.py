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
from pollination_sdk.models.job_status import JobStatus  # noqa: E501
from pollination_sdk.rest import ApiException

class TestJobStatus(unittest.TestCase):
    """JobStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.job_status.JobStatus()  # noqa: E501
        if include_optional :
            return JobStatus(
                annotations = {
                    'key' : '0'
                    }, 
                api_version = 'v1beta1', 
                finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                id = '0', 
                message = '0', 
                runs_cancelled = 56, 
                runs_completed = 56, 
                runs_failed = 56, 
                runs_pending = 56, 
                runs_running = 56, 
                source = '0', 
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                status = null, 
                type = 'JobStatus'
            )
        else :
            return JobStatus(
                id = '0',
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )

    def testJobStatus(self):
        """Test JobStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
