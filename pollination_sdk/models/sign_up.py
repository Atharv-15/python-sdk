# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: 0.10.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class SignUp(object):
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
        'email': 'str',
        'metadata': 'UserMetadata',
        'password': 'str',
        'username': 'str'
    }

    attribute_map = {
        'email': 'email',
        'metadata': 'metadata',
        'password': 'password',
        'username': 'username'
    }

    def __init__(self, email=None, metadata=None, password=None, username=None, local_vars_configuration=None):  # noqa: E501
        """SignUp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._metadata = None
        self._password = None
        self._username = None
        self.discriminator = None

        self.email = email
        self.metadata = metadata
        self.password = password
        self.username = username

    @property
    def email(self):
        """Gets the email of this SignUp.  # noqa: E501

        An email address  # noqa: E501

        :return: The email of this SignUp.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SignUp.

        An email address  # noqa: E501

        :param email: The email of this SignUp.  # noqa: E501
        :type email: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def metadata(self):
        """Gets the metadata of this SignUp.  # noqa: E501

        Some information about the user  # noqa: E501

        :return: The metadata of this SignUp.  # noqa: E501
        :rtype: UserMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this SignUp.

        Some information about the user  # noqa: E501

        :param metadata: The metadata of this SignUp.  # noqa: E501
        :type metadata: UserMetadata
        """
        if self.local_vars_configuration.client_side_validation and metadata is None:  # noqa: E501
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def password(self):
        """Gets the password of this SignUp.  # noqa: E501

        A password for the user  # noqa: E501

        :return: The password of this SignUp.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SignUp.

        A password for the user  # noqa: E501

        :param password: The password of this SignUp.  # noqa: E501
        :type password: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def username(self):
        """Gets the username of this SignUp.  # noqa: E501

        A lower case username without spaces  # noqa: E501

        :return: The username of this SignUp.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SignUp.

        A lower case username without spaces  # noqa: E501

        :param username: The username of this SignUp.  # noqa: E501
        :type username: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

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
        if not isinstance(other, SignUp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignUp):
            return True

        return self.to_dict() != other.to_dict()
