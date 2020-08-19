# coding: utf-8

"""
    Pollination Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.7.5
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class QueenbeeRecipeMetadataMetaData(object):
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
        'tag': 'str',
        'keywords': 'list[str]',
        'maintainers': 'list[QueenbeeRecipeMetadataMaintainer]',
        'home': 'str',
        'sources': 'list[str]',
        'icon': 'str',
        'deprecated': 'bool',
        'description': 'str',
        'license': 'License'
    }

    attribute_map = {
        'name': 'name',
        'tag': 'tag',
        'keywords': 'keywords',
        'maintainers': 'maintainers',
        'home': 'home',
        'sources': 'sources',
        'icon': 'icon',
        'deprecated': 'deprecated',
        'description': 'description',
        'license': 'license'
    }

    def __init__(self, name=None, tag=None, keywords=None, maintainers=None, home=None, sources=None, icon=None, deprecated=None, description=None, license=None, local_vars_configuration=None):  # noqa: E501
        """QueenbeeRecipeMetadataMetaData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._tag = None
        self._keywords = None
        self._maintainers = None
        self._home = None
        self._sources = None
        self._icon = None
        self._deprecated = None
        self._description = None
        self._license = None
        self.discriminator = None

        self.name = name
        self.tag = tag
        if keywords is not None:
            self.keywords = keywords
        if maintainers is not None:
            self.maintainers = maintainers
        if home is not None:
            self.home = home
        if sources is not None:
            self.sources = sources
        if icon is not None:
            self.icon = icon
        if deprecated is not None:
            self.deprecated = deprecated
        if description is not None:
            self.description = description
        if license is not None:
            self.license = license

    @property
    def name(self):
        """Gets the name of this QueenbeeRecipeMetadataMetaData.  # noqa: E501

        Recipe name. Make it descriptive and helpful ;)  # noqa: E501

        :return: The name of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueenbeeRecipeMetadataMetaData.

        Recipe name. Make it descriptive and helpful ;)  # noqa: E501

        :param name: The name of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def tag(self):
        """Gets the tag of this QueenbeeRecipeMetadataMetaData.  # noqa: E501

        The tag of the recipe  # noqa: E501

        :return: The tag of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this QueenbeeRecipeMetadataMetaData.

        The tag of the recipe  # noqa: E501

        :param tag: The tag of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tag is None:  # noqa: E501
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

    @property
    def keywords(self):
        """Gets the keywords of this QueenbeeRecipeMetadataMetaData.  # noqa: E501

        A list of keywords to search the recipe by  # noqa: E501

        :return: The keywords of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this QueenbeeRecipeMetadataMetaData.

        A list of keywords to search the recipe by  # noqa: E501

        :param keywords: The keywords of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def maintainers(self):
        """Gets the maintainers of this QueenbeeRecipeMetadataMetaData.  # noqa: E501

        A list of maintainers for the recipe  # noqa: E501

        :return: The maintainers of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :rtype: list[QueenbeeRecipeMetadataMaintainer]
        """
        return self._maintainers

    @maintainers.setter
    def maintainers(self, maintainers):
        """Sets the maintainers of this QueenbeeRecipeMetadataMetaData.

        A list of maintainers for the recipe  # noqa: E501

        :param maintainers: The maintainers of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :type: list[QueenbeeRecipeMetadataMaintainer]
        """

        self._maintainers = maintainers

    @property
    def home(self):
        """Gets the home of this QueenbeeRecipeMetadataMetaData.  # noqa: E501

        The URL of this recipe's home page  # noqa: E501

        :return: The home of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :rtype: str
        """
        return self._home

    @home.setter
    def home(self, home):
        """Sets the home of this QueenbeeRecipeMetadataMetaData.

        The URL of this recipe's home page  # noqa: E501

        :param home: The home of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :type: str
        """

        self._home = home

    @property
    def sources(self):
        """Gets the sources of this QueenbeeRecipeMetadataMetaData.  # noqa: E501

        A list of URLs to source code for this project  # noqa: E501

        :return: The sources of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :rtype: list[str]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this QueenbeeRecipeMetadataMetaData.

        A list of URLs to source code for this project  # noqa: E501

        :param sources: The sources of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :type: list[str]
        """

        self._sources = sources

    @property
    def icon(self):
        """Gets the icon of this QueenbeeRecipeMetadataMetaData.  # noqa: E501

        A URL to an SVG or PNG image to be used as an icon  # noqa: E501

        :return: The icon of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this QueenbeeRecipeMetadataMetaData.

        A URL to an SVG or PNG image to be used as an icon  # noqa: E501

        :param icon: The icon of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def deprecated(self):
        """Gets the deprecated of this QueenbeeRecipeMetadataMetaData.  # noqa: E501

        Whether this recipe is deprecated  # noqa: E501

        :return: The deprecated of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this QueenbeeRecipeMetadataMetaData.

        Whether this recipe is deprecated  # noqa: E501

        :param deprecated: The deprecated of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def description(self):
        """Gets the description of this QueenbeeRecipeMetadataMetaData.  # noqa: E501

        A description of what this recipe does  # noqa: E501

        :return: The description of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QueenbeeRecipeMetadataMetaData.

        A description of what this recipe does  # noqa: E501

        :param description: The description of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def license(self):
        """Gets the license of this QueenbeeRecipeMetadataMetaData.  # noqa: E501

        The license information.  # noqa: E501

        :return: The license of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :rtype: License
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this QueenbeeRecipeMetadataMetaData.

        The license information.  # noqa: E501

        :param license: The license of this QueenbeeRecipeMetadataMetaData.  # noqa: E501
        :type: License
        """

        self._license = license

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
        if not isinstance(other, QueenbeeRecipeMetadataMetaData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueenbeeRecipeMetadataMetaData):
            return True

        return self.to_dict() != other.to_dict()
