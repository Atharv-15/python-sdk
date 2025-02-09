# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.27.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class RunProgress(object):
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
        'completed': 'int',
        'running': 'int',
        'total': 'int'
    }

    attribute_map = {
        'completed': 'completed',
        'running': 'running',
        'total': 'total'
    }

    def __init__(self, completed=0, running=0, total=0, local_vars_configuration=None):  # noqa: E501
        """RunProgress - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._completed = None
        self._running = None
        self._total = None
        self.discriminator = None

        if completed is not None:
            self.completed = completed
        if running is not None:
            self.running = running
        if total is not None:
            self.total = total

    @property
    def completed(self):
        """Gets the completed of this RunProgress.  # noqa: E501


        :return: The completed of this RunProgress.  # noqa: E501
        :rtype: int
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this RunProgress.


        :param completed: The completed of this RunProgress.  # noqa: E501
        :type completed: int
        """

        self._completed = completed

    @property
    def running(self):
        """Gets the running of this RunProgress.  # noqa: E501


        :return: The running of this RunProgress.  # noqa: E501
        :rtype: int
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this RunProgress.


        :param running: The running of this RunProgress.  # noqa: E501
        :type running: int
        """

        self._running = running

    @property
    def total(self):
        """Gets the total of this RunProgress.  # noqa: E501


        :return: The total of this RunProgress.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this RunProgress.


        :param total: The total of this RunProgress.  # noqa: E501
        :type total: int
        """

        self._total = total

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
        if not isinstance(other, RunProgress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RunProgress):
            return True

        return self.to_dict() != other.to_dict()
