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


class RecipeSelection(object):
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
        'owner': 'str',
        'name': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'owner': 'owner',
        'name': 'name',
        'tag': 'tag'
    }

    def __init__(self, owner=None, name=None, tag='latest', local_vars_configuration=None):  # noqa: E501
        """RecipeSelection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._owner = None
        self._name = None
        self._tag = None
        self.discriminator = None

        self.owner = owner
        self.name = name
        if tag is not None:
            self.tag = tag

    @property
    def owner(self):
        """Gets the owner of this RecipeSelection.  # noqa: E501

        Name of the owner of the recipe  # noqa: E501

        :return: The owner of this RecipeSelection.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this RecipeSelection.

        Name of the owner of the recipe  # noqa: E501

        :param owner: The owner of this RecipeSelection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def name(self):
        """Gets the name of this RecipeSelection.  # noqa: E501

        Name of the recipe  # noqa: E501

        :return: The name of this RecipeSelection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RecipeSelection.

        Name of the recipe  # noqa: E501

        :param name: The name of this RecipeSelection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def tag(self):
        """Gets the tag of this RecipeSelection.  # noqa: E501

        The specific tag of the recipe to use  # noqa: E501

        :return: The tag of this RecipeSelection.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this RecipeSelection.

        The specific tag of the recipe to use  # noqa: E501

        :param tag: The tag of this RecipeSelection.  # noqa: E501
        :type: str
        """

        self._tag = tag

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
        if not isinstance(other, RecipeSelection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecipeSelection):
            return True

        return self.to_dict() != other.to_dict()
