# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.16.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class RepositoryUpdate(object):
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
        'description': 'str',
        'icon': 'str',
        'keywords': 'list[str]',
        'public': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'icon': 'icon',
        'keywords': 'keywords',
        'public': 'public'
    }

    def __init__(self, description=None, icon=None, keywords=None, public=None, local_vars_configuration=None):  # noqa: E501
        """RepositoryUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._icon = None
        self._keywords = None
        self._public = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if icon is not None:
            self.icon = icon
        if keywords is not None:
            self.keywords = keywords
        if public is not None:
            self.public = public

    @property
    def description(self):
        """Gets the description of this RepositoryUpdate.  # noqa: E501

        A description of the repository  # noqa: E501

        :return: The description of this RepositoryUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RepositoryUpdate.

        A description of the repository  # noqa: E501

        :param description: The description of this RepositoryUpdate.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def icon(self):
        """Gets the icon of this RepositoryUpdate.  # noqa: E501

        An icon to represent this repository  # noqa: E501

        :return: The icon of this RepositoryUpdate.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this RepositoryUpdate.

        An icon to represent this repository  # noqa: E501

        :param icon: The icon of this RepositoryUpdate.  # noqa: E501
        :type icon: str
        """

        self._icon = icon

    @property
    def keywords(self):
        """Gets the keywords of this RepositoryUpdate.  # noqa: E501

        A list of keywords to index the repository by  # noqa: E501

        :return: The keywords of this RepositoryUpdate.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this RepositoryUpdate.

        A list of keywords to index the repository by  # noqa: E501

        :param keywords: The keywords of this RepositoryUpdate.  # noqa: E501
        :type keywords: list[str]
        """

        self._keywords = keywords

    @property
    def public(self):
        """Gets the public of this RepositoryUpdate.  # noqa: E501

        Whether or not a repository is publicly viewable  # noqa: E501

        :return: The public of this RepositoryUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this RepositoryUpdate.

        Whether or not a repository is publicly viewable  # noqa: E501

        :param public: The public of this RepositoryUpdate.  # noqa: E501
        :type public: bool
        """

        self._public = public

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
        if not isinstance(other, RepositoryUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepositoryUpdate):
            return True

        return self.to_dict() != other.to_dict()
