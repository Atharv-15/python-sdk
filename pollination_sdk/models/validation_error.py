# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: 0.10.10
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class ValidationError(object):
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
        'loc': 'list[str]',
        'msg': 'str',
        'type': 'str'
    }

    attribute_map = {
        'loc': 'loc',
        'msg': 'msg',
        'type': 'type'
    }

    def __init__(self, loc=None, msg=None, type=None, local_vars_configuration=None):  # noqa: E501
        """ValidationError - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._loc = None
        self._msg = None
        self._type = None
        self.discriminator = None

        self.loc = loc
        self.msg = msg
        self.type = type

    @property
    def loc(self):
        """Gets the loc of this ValidationError.  # noqa: E501


        :return: The loc of this ValidationError.  # noqa: E501
        :rtype: list[str]
        """
        return self._loc

    @loc.setter
    def loc(self, loc):
        """Sets the loc of this ValidationError.


        :param loc: The loc of this ValidationError.  # noqa: E501
        :type loc: list[str]
        """
        if self.local_vars_configuration.client_side_validation and loc is None:  # noqa: E501
            raise ValueError("Invalid value for `loc`, must not be `None`")  # noqa: E501

        self._loc = loc

    @property
    def msg(self):
        """Gets the msg of this ValidationError.  # noqa: E501


        :return: The msg of this ValidationError.  # noqa: E501
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this ValidationError.


        :param msg: The msg of this ValidationError.  # noqa: E501
        :type msg: str
        """
        if self.local_vars_configuration.client_side_validation and msg is None:  # noqa: E501
            raise ValueError("Invalid value for `msg`, must not be `None`")  # noqa: E501

        self._msg = msg

    @property
    def type(self):
        """Gets the type of this ValidationError.  # noqa: E501


        :return: The type of this ValidationError.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ValidationError.


        :param type: The type of this ValidationError.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, ValidationError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValidationError):
            return True

        return self.to_dict() != other.to_dict()
