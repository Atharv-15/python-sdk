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


class FileMeta(object):
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
        'key': 'str',
        'type': 'str',
        'file_name': 'str',
        'last_modified': 'datetime',
        'size': 'int'
    }

    attribute_map = {
        'key': 'key',
        'type': 'type',
        'file_name': 'file_name',
        'last_modified': 'last_modified',
        'size': 'size'
    }

    def __init__(self, key=None, type=None, file_name=None, last_modified=None, size=None, local_vars_configuration=None):  # noqa: E501
        """FileMeta - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._type = None
        self._file_name = None
        self._last_modified = None
        self._size = None
        self.discriminator = None

        self.key = key
        self.type = type
        self.file_name = file_name
        if last_modified is not None:
            self.last_modified = last_modified
        if size is not None:
            self.size = size

    @property
    def key(self):
        """Gets the key of this FileMeta.  # noqa: E501


        :return: The key of this FileMeta.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this FileMeta.


        :param key: The key of this FileMeta.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def type(self):
        """Gets the type of this FileMeta.  # noqa: E501


        :return: The type of this FileMeta.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FileMeta.


        :param type: The type of this FileMeta.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def file_name(self):
        """Gets the file_name of this FileMeta.  # noqa: E501


        :return: The file_name of this FileMeta.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this FileMeta.


        :param file_name: The file_name of this FileMeta.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and file_name is None:  # noqa: E501
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501

        self._file_name = file_name

    @property
    def last_modified(self):
        """Gets the last_modified of this FileMeta.  # noqa: E501


        :return: The last_modified of this FileMeta.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this FileMeta.


        :param last_modified: The last_modified of this FileMeta.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def size(self):
        """Gets the size of this FileMeta.  # noqa: E501


        :return: The size of this FileMeta.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FileMeta.


        :param size: The size of this FileMeta.  # noqa: E501
        :type: int
        """

        self._size = size

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
        if not isinstance(other, FileMeta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileMeta):
            return True

        return self.to_dict() != other.to_dict()
