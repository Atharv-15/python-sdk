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


class DAGTaskParameterArgument(object):
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
        '_from': 'object',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        '_from': 'from',
        'value': 'value'
    }

    def __init__(self, name=None, _from=None, value=None, local_vars_configuration=None):  # noqa: E501
        """DAGTaskParameterArgument - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self.__from = None
        self._value = None
        self.discriminator = None

        self.name = name
        if _from is not None:
            self._from = _from
        if value is not None:
            self.value = value

    @property
    def name(self):
        """Gets the name of this DAGTaskParameterArgument.  # noqa: E501

        Name of the argument variable  # noqa: E501

        :return: The name of this DAGTaskParameterArgument.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DAGTaskParameterArgument.

        Name of the argument variable  # noqa: E501

        :param name: The name of this DAGTaskParameterArgument.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def _from(self):
        """Gets the _from of this DAGTaskParameterArgument.  # noqa: E501


        :return: The _from of this DAGTaskParameterArgument.  # noqa: E501
        :rtype: object
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this DAGTaskParameterArgument.


        :param _from: The _from of this DAGTaskParameterArgument.  # noqa: E501
        :type: object
        """

        self.__from = _from

    @property
    def value(self):
        """Gets the value of this DAGTaskParameterArgument.  # noqa: E501

        The fixed value for this task argument  # noqa: E501

        :return: The value of this DAGTaskParameterArgument.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DAGTaskParameterArgument.

        The fixed value for this task argument  # noqa: E501

        :param value: The value of this DAGTaskParameterArgument.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if not isinstance(other, DAGTaskParameterArgument):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DAGTaskParameterArgument):
            return True

        return self.to_dict() != other.to_dict()
