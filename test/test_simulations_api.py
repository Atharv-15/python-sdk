# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: 0.10.10
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pollination_sdk
from pollination_sdk.api.simulations_api import SimulationsApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestSimulationsApi(unittest.TestCase):
    """SimulationsApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.simulations_api.SimulationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_simulation(self):
        """Test case for create_simulation

        Schedule a simulation  # noqa: E501
        """
        pass

    def test_download_simulation_artifact(self):
        """Test case for download_simulation_artifact

        Download an artifact from the simulation folder  # noqa: E501
        """
        pass

    def test_get_simulation(self):
        """Test case for get_simulation

        Get a Simulation  # noqa: E501
        """
        pass

    def test_get_simulation_inputs(self):
        """Test case for get_simulation_inputs

        Get simulation inputs  # noqa: E501
        """
        pass

    def test_get_simulation_logs(self):
        """Test case for get_simulation_logs

        Get simulation logs  # noqa: E501
        """
        pass

    def test_get_simulation_output_artifact(self):
        """Test case for get_simulation_output_artifact

        Get simulation output artifact by name  # noqa: E501
        """
        pass

    def test_get_simulation_task_logs(self):
        """Test case for get_simulation_task_logs

        Get simulation logs  # noqa: E501
        """
        pass

    def test_list_simulation_artifacts(self):
        """Test case for list_simulation_artifacts

        List artifacts in a simulation folder  # noqa: E501
        """
        pass

    def test_list_simulations(self):
        """Test case for list_simulations

        List simulations  # noqa: E501
        """
        pass

    def test_resume_simulation(self):
        """Test case for resume_simulation

        resume a simulation  # noqa: E501
        """
        pass

    def test_stop_simulation(self):
        """Test case for stop_simulation

        Stop a simulation  # noqa: E501
        """
        pass

    def test_suspend_simulation(self):
        """Test case for suspend_simulation

        Suspend a simulation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
