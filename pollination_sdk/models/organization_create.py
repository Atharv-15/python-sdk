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


class OrganizationCreate(object):
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
        'account_name': 'str',
        'contact_email': 'str',
        'description': 'str',
        'name': 'str',
        'picture_url': 'str'
    }

    attribute_map = {
        'account_name': 'account_name',
        'contact_email': 'contact_email',
        'description': 'description',
        'name': 'name',
        'picture_url': 'picture_url'
    }

    def __init__(self, account_name=None, contact_email=None, description=None, name=None, picture_url=None, local_vars_configuration=None):  # noqa: E501
        """OrganizationCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_name = None
        self._contact_email = None
        self._description = None
        self._name = None
        self._picture_url = None
        self.discriminator = None

        if account_name is not None:
            self.account_name = account_name
        if contact_email is not None:
            self.contact_email = contact_email
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if picture_url is not None:
            self.picture_url = picture_url

    @property
    def account_name(self):
        """Gets the account_name of this OrganizationCreate.  # noqa: E501

        The unique name of the org in small case without spaces  # noqa: E501

        :return: The account_name of this OrganizationCreate.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this OrganizationCreate.

        The unique name of the org in small case without spaces  # noqa: E501

        :param account_name: The account_name of this OrganizationCreate.  # noqa: E501
        :type account_name: str
        """

        self._account_name = account_name

    @property
    def contact_email(self):
        """Gets the contact_email of this OrganizationCreate.  # noqa: E501

        The contact email for the Organization  # noqa: E501

        :return: The contact_email of this OrganizationCreate.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this OrganizationCreate.

        The contact email for the Organization  # noqa: E501

        :param contact_email: The contact_email of this OrganizationCreate.  # noqa: E501
        :type contact_email: str
        """

        self._contact_email = contact_email

    @property
    def description(self):
        """Gets the description of this OrganizationCreate.  # noqa: E501

        A description of the org  # noqa: E501

        :return: The description of this OrganizationCreate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OrganizationCreate.

        A description of the org  # noqa: E501

        :param description: The description of this OrganizationCreate.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this OrganizationCreate.  # noqa: E501

        The display name for this org  # noqa: E501

        :return: The name of this OrganizationCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationCreate.

        The display name for this org  # noqa: E501

        :param name: The name of this OrganizationCreate.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def picture_url(self):
        """Gets the picture_url of this OrganizationCreate.  # noqa: E501

        URL to the picture associated with this org  # noqa: E501

        :return: The picture_url of this OrganizationCreate.  # noqa: E501
        :rtype: str
        """
        return self._picture_url

    @picture_url.setter
    def picture_url(self, picture_url):
        """Sets the picture_url of this OrganizationCreate.

        URL to the picture associated with this org  # noqa: E501

        :param picture_url: The picture_url of this OrganizationCreate.  # noqa: E501
        :type picture_url: str
        """

        self._picture_url = picture_url

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
        if not isinstance(other, OrganizationCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationCreate):
            return True

        return self.to_dict() != other.to_dict()
