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


class RepositoryIndex(object):
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
        'generated': 'datetime',
        'operator': 'dict(str, list[OperatorVersion])',
        'recipe': 'dict(str, list[RecipeVersion])'
    }

    attribute_map = {
        'generated': 'generated',
        'operator': 'operator',
        'recipe': 'recipe'
    }

    def __init__(self, generated=None, operator=None, recipe=None, local_vars_configuration=None):  # noqa: E501
        """RepositoryIndex - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._generated = None
        self._operator = None
        self._recipe = None
        self.discriminator = None

        if generated is not None:
            self.generated = generated
        if operator is not None:
            self.operator = operator
        if recipe is not None:
            self.recipe = recipe

    @property
    def generated(self):
        """Gets the generated of this RepositoryIndex.  # noqa: E501

        The timestamp at which the index was generated  # noqa: E501

        :return: The generated of this RepositoryIndex.  # noqa: E501
        :rtype: datetime
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this RepositoryIndex.

        The timestamp at which the index was generated  # noqa: E501

        :param generated: The generated of this RepositoryIndex.  # noqa: E501
        :type: datetime
        """

        self._generated = generated

    @property
    def operator(self):
        """Gets the operator of this RepositoryIndex.  # noqa: E501

        A dict of operators accessible by name. Each name key points to a list of operator versions  # noqa: E501

        :return: The operator of this RepositoryIndex.  # noqa: E501
        :rtype: dict(str, list[OperatorVersion])
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this RepositoryIndex.

        A dict of operators accessible by name. Each name key points to a list of operator versions  # noqa: E501

        :param operator: The operator of this RepositoryIndex.  # noqa: E501
        :type: dict(str, list[OperatorVersion])
        """

        self._operator = operator

    @property
    def recipe(self):
        """Gets the recipe of this RepositoryIndex.  # noqa: E501

        A dict of recipes accessible by name. Each name key points to a list of recipesversions  # noqa: E501

        :return: The recipe of this RepositoryIndex.  # noqa: E501
        :rtype: dict(str, list[RecipeVersion])
        """
        return self._recipe

    @recipe.setter
    def recipe(self, recipe):
        """Sets the recipe of this RepositoryIndex.

        A dict of recipes accessible by name. Each name key points to a list of recipesversions  # noqa: E501

        :param recipe: The recipe of this RepositoryIndex.  # noqa: E501
        :type: dict(str, list[RecipeVersion])
        """

        self._recipe = recipe

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
        if not isinstance(other, RepositoryIndex):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepositoryIndex):
            return True

        return self.to_dict() != other.to_dict()
