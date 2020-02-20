# coding: utf-8

"""
    Pollination Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.1.0-5-g8af5d0f
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class HTTPLocation(object):
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
        'type': 'str',
        'name': 'str',
        'root': 'str',
        'headers': 'dict(str, str)',
        'verb': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'root': 'root',
        'headers': 'headers',
        'verb': 'verb'
    }

    def __init__(self, type=None, name=None, root=None, headers=None, verb='GET', local_vars_configuration=None):  # noqa: E501
        """HTTPLocation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._root = None
        self._headers = None
        self._verb = None
        self.discriminator = None

        self.type = type
        self.name = name
        self.root = root
        if headers is not None:
            self.headers = headers
        if verb is not None:
            self.verb = verb

    @property
    def type(self):
        """Gets the type of this HTTPLocation.  # noqa: E501


        :return: The type of this HTTPLocation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HTTPLocation.


        :param type: The type of this HTTPLocation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^http$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^http$/`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this HTTPLocation.  # noqa: E501

        Name is a unique identifier for this particular Artifact Location  # noqa: E501

        :return: The name of this HTTPLocation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HTTPLocation.

        Name is a unique identifier for this particular Artifact Location  # noqa: E501

        :param name: The name of this HTTPLocation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def root(self):
        """Gets the root of this HTTPLocation.  # noqa: E501

        For a HTTP endpoint this can be http://climate.onebuilding.org.  # noqa: E501

        :return: The root of this HTTPLocation.  # noqa: E501
        :rtype: str
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this HTTPLocation.

        For a HTTP endpoint this can be http://climate.onebuilding.org.  # noqa: E501

        :param root: The root of this HTTPLocation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and root is None:  # noqa: E501
            raise ValueError("Invalid value for `root`, must not be `None`")  # noqa: E501

        self._root = root

    @property
    def headers(self):
        """Gets the headers of this HTTPLocation.  # noqa: E501

        An object with Key Value pairs of HTTP headers  # noqa: E501

        :return: The headers of this HTTPLocation.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this HTTPLocation.

        An object with Key Value pairs of HTTP headers  # noqa: E501

        :param headers: The headers of this HTTPLocation.  # noqa: E501
        :type: dict(str, str)
        """

        self._headers = headers

    @property
    def verb(self):
        """Gets the verb of this HTTPLocation.  # noqa: E501

        The HTTP verb to use when making the request.  # noqa: E501

        :return: The verb of this HTTPLocation.  # noqa: E501
        :rtype: str
        """
        return self._verb

    @verb.setter
    def verb(self, verb):
        """Sets the verb of this HTTPLocation.

        The HTTP verb to use when making the request.  # noqa: E501

        :param verb: The verb of this HTTPLocation.  # noqa: E501
        :type: str
        """
        allowed_values = ["GET", "POST", "PUT", "PATCH", "DELETE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and verb not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `verb` ({0}), must be one of {1}"  # noqa: E501
                .format(verb, allowed_values)
            )

        self._verb = verb

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
        if not isinstance(other, HTTPLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HTTPLocation):
            return True

        return self.to_dict() != other.to_dict()
