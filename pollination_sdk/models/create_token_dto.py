# coding: utf-8

"""
    Pollination Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class CreateTokenDto(object):
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
        'token_name': 'str',
        'email': 'str',
        'password': 'str'
    }

    attribute_map = {
        'token_name': 'token_name',
        'email': 'email',
        'password': 'password'
    }

    def __init__(self, token_name=None, email=None, password=None, local_vars_configuration=None):  # noqa: E501
        """CreateTokenDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._token_name = None
        self._email = None
        self._password = None
        self.discriminator = None

        self.token_name = token_name
        self.email = email
        self.password = password

    @property
    def token_name(self):
        """Gets the token_name of this CreateTokenDto.  # noqa: E501


        :return: The token_name of this CreateTokenDto.  # noqa: E501
        :rtype: str
        """
        return self._token_name

    @token_name.setter
    def token_name(self, token_name):
        """Sets the token_name of this CreateTokenDto.


        :param token_name: The token_name of this CreateTokenDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and token_name is None:  # noqa: E501
            raise ValueError("Invalid value for `token_name`, must not be `None`")  # noqa: E501

        self._token_name = token_name

    @property
    def email(self):
        """Gets the email of this CreateTokenDto.  # noqa: E501


        :return: The email of this CreateTokenDto.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateTokenDto.


        :param email: The email of this CreateTokenDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def password(self):
        """Gets the password of this CreateTokenDto.  # noqa: E501


        :return: The password of this CreateTokenDto.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateTokenDto.


        :param password: The password of this CreateTokenDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

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
        if not isinstance(other, CreateTokenDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateTokenDto):
            return True

        return self.to_dict() != other.to_dict()
