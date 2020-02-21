# coding: utf-8

"""
    Pollination Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.2.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class SubmitSimulationDto(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'workflow_slug': 'str',
        'inputs': 'Arguments'
    }

    attribute_map = {
        'workflow_slug': 'workflow_slug',
        'inputs': 'inputs'
    }

    def __init__(self, workflow_slug=None, inputs=None, local_vars_configuration=None):  # noqa: E501
        """SubmitSimulationDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._workflow_slug = None
        self._inputs = None
        self.discriminator = None

        self.workflow_slug = workflow_slug
        if inputs is not None:
            self.inputs = inputs

    @property
    def workflow_slug(self):
        """Gets the workflow_slug of this SubmitSimulationDto.  # noqa: E501

        The workflow slug in format {owner}:{workflow_name}  # noqa: E501

        :return: The workflow_slug of this SubmitSimulationDto.  # noqa: E501
        :rtype: str
        """
        return self._workflow_slug

    @workflow_slug.setter
    def workflow_slug(self, workflow_slug):
        """Sets the workflow_slug of this SubmitSimulationDto.

        The workflow slug in format {owner}:{workflow_name}  # noqa: E501

        :param workflow_slug: The workflow_slug of this SubmitSimulationDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and workflow_slug is None:  # noqa: E501
            raise ValueError("Invalid value for `workflow_slug`, must not be `None`")  # noqa: E501

        self._workflow_slug = workflow_slug

    @property
    def inputs(self):
        """Gets the inputs of this SubmitSimulationDto.  # noqa: E501

        Simulation inputs  # noqa: E501

        :return: The inputs of this SubmitSimulationDto.  # noqa: E501
        :rtype: Arguments
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this SubmitSimulationDto.

        Simulation inputs  # noqa: E501

        :param inputs: The inputs of this SubmitSimulationDto.  # noqa: E501
        :type: Arguments
        """

        self._inputs = inputs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SubmitSimulationDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubmitSimulationDto):
            return True

        return self.to_dict() != other.to_dict()
