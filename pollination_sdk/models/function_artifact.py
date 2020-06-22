# coding: utf-8

"""
    Pollination Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.5.25
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class FunctionArtifact(object):
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
        'name': 'str',
        'description': 'str',
        'path': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'path': 'path'
    }

    def __init__(self, name=None, description=None, path=None, local_vars_configuration=None):  # noqa: E501
        """FunctionArtifact - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._path = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.path = path

    @property
    def name(self):
        """Gets the name of this FunctionArtifact.  # noqa: E501

        Name of the artifact. Must be unique within a task's inputs / outputs.  # noqa: E501

        :return: The name of this FunctionArtifact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FunctionArtifact.

        Name of the artifact. Must be unique within a task's inputs / outputs.  # noqa: E501

        :param name: The name of this FunctionArtifact.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this FunctionArtifact.  # noqa: E501

        Optional description for input parameter.  # noqa: E501

        :return: The description of this FunctionArtifact.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FunctionArtifact.

        Optional description for input parameter.  # noqa: E501

        :param description: The description of this FunctionArtifact.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def path(self):
        """Gets the path of this FunctionArtifact.  # noqa: E501

        Path to the artifact relative to the working directory where the command is executed.  # noqa: E501

        :return: The path of this FunctionArtifact.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this FunctionArtifact.

        Path to the artifact relative to the working directory where the command is executed.  # noqa: E501

        :param path: The path of this FunctionArtifact.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

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
        if not isinstance(other, FunctionArtifact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FunctionArtifact):
            return True

        return self.to_dict() != other.to_dict()
