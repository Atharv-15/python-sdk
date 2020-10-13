# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: 0.10.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class DAGTaskLoop(object):
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
        '_from': 'AnyOfInputParameterReferenceTaskParameterReference',
        'value': 'list[AnyOfstringintegernumberobject]'
    }

    attribute_map = {
        '_from': 'from',
        'value': 'value'
    }

    def __init__(self, _from=None, value=None, local_vars_configuration=None):  # noqa: E501
        """DAGTaskLoop - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self.__from = None
        self._value = None
        self.discriminator = None

        if _from is not None:
            self._from = _from
        if value is not None:
            self.value = value

    @property
    def _from(self):
        """Gets the _from of this DAGTaskLoop.  # noqa: E501

        The task or DAG parameter to loop over (must be iterable).  # noqa: E501

        :return: The _from of this DAGTaskLoop.  # noqa: E501
        :rtype: AnyOfInputParameterReferenceTaskParameterReference
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this DAGTaskLoop.

        The task or DAG parameter to loop over (must be iterable).  # noqa: E501

        :param _from: The _from of this DAGTaskLoop.  # noqa: E501
        :type _from: AnyOfInputParameterReferenceTaskParameterReference
        """

        self.__from = _from

    @property
    def value(self):
        """Gets the value of this DAGTaskLoop.  # noqa: E501

        A list of values or JSON objects to loop over.  # noqa: E501

        :return: The value of this DAGTaskLoop.  # noqa: E501
        :rtype: list[AnyOfstringintegernumberobject]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DAGTaskLoop.

        A list of values or JSON objects to loop over.  # noqa: E501

        :param value: The value of this DAGTaskLoop.  # noqa: E501
        :type value: list[AnyOfstringintegernumberobject]
        """

        self._value = value

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
        if not isinstance(other, DAGTaskLoop):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DAGTaskLoop):
            return True

        return self.to_dict() != other.to_dict()
