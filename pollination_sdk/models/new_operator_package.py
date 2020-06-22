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


class NewOperatorPackage(object):
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
        'manifest': 'Operator',
        'readme': 'str',
        'license': 'str'
    }

    attribute_map = {
        'manifest': 'manifest',
        'readme': 'readme',
        'license': 'license'
    }

    def __init__(self, manifest=None, readme='', license='', local_vars_configuration=None):  # noqa: E501
        """NewOperatorPackage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._manifest = None
        self._readme = None
        self._license = None
        self.discriminator = None

        self.manifest = manifest
        if readme is not None:
            self.readme = readme
        if license is not None:
            self.license = license

    @property
    def manifest(self):
        """Gets the manifest of this NewOperatorPackage.  # noqa: E501

        The Operator manifest to be created  # noqa: E501

        :return: The manifest of this NewOperatorPackage.  # noqa: E501
        :rtype: Operator
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """Sets the manifest of this NewOperatorPackage.

        The Operator manifest to be created  # noqa: E501

        :param manifest: The manifest of this NewOperatorPackage.  # noqa: E501
        :type: Operator
        """
        if self.local_vars_configuration.client_side_validation and manifest is None:  # noqa: E501
            raise ValueError("Invalid value for `manifest`, must not be `None`")  # noqa: E501

        self._manifest = manifest

    @property
    def readme(self):
        """Gets the readme of this NewOperatorPackage.  # noqa: E501

        The README file to attach to this package  # noqa: E501

        :return: The readme of this NewOperatorPackage.  # noqa: E501
        :rtype: str
        """
        return self._readme

    @readme.setter
    def readme(self, readme):
        """Sets the readme of this NewOperatorPackage.

        The README file to attach to this package  # noqa: E501

        :param readme: The readme of this NewOperatorPackage.  # noqa: E501
        :type: str
        """

        self._readme = readme

    @property
    def license(self):
        """Gets the license of this NewOperatorPackage.  # noqa: E501

        The license file to attach to this package  # noqa: E501

        :return: The license of this NewOperatorPackage.  # noqa: E501
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this NewOperatorPackage.

        The license file to attach to this package  # noqa: E501

        :param license: The license of this NewOperatorPackage.  # noqa: E501
        :type: str
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
        if not isinstance(other, NewOperatorPackage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewOperatorPackage):
            return True

        return self.to_dict() != other.to_dict()
