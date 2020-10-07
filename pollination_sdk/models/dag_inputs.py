# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: 0.9.2
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class DAGInputs(object):
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
        'artifacts': 'list[DAGInputArtifact]',
        'parameters': 'list[DAGInputParameter]'
    }

    attribute_map = {
        'artifacts': 'artifacts',
        'parameters': 'parameters'
    }

    def __init__(self, artifacts=[], parameters=[], local_vars_configuration=None):  # noqa: E501
        """DAGInputs - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._artifacts = None
        self._parameters = None
        self.discriminator = None

        if artifacts is not None:
            self.artifacts = artifacts
        if parameters is not None:
            self.parameters = parameters

    @property
    def artifacts(self):
        """Gets the artifacts of this DAGInputs.  # noqa: E501

        A list of artifacts the DAG will use  # noqa: E501

        :return: The artifacts of this DAGInputs.  # noqa: E501
        :rtype: list[DAGInputArtifact]
        """
        return self._artifacts

    @artifacts.setter
    def artifacts(self, artifacts):
        """Sets the artifacts of this DAGInputs.

        A list of artifacts the DAG will use  # noqa: E501

        :param artifacts: The artifacts of this DAGInputs.  # noqa: E501
        :type artifacts: list[DAGInputArtifact]
        """

        self._artifacts = artifacts

    @property
    def parameters(self):
        """Gets the parameters of this DAGInputs.  # noqa: E501

        A list of parameters the DAG will use as input values  # noqa: E501

        :return: The parameters of this DAGInputs.  # noqa: E501
        :rtype: list[DAGInputParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this DAGInputs.

        A list of parameters the DAG will use as input values  # noqa: E501

        :param parameters: The parameters of this DAGInputs.  # noqa: E501
        :type parameters: list[DAGInputParameter]
        """

        self._parameters = parameters

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
        if not isinstance(other, DAGInputs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DAGInputs):
            return True

        return self.to_dict() != other.to_dict()
