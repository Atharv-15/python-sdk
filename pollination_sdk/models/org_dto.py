# coding: utf-8

"""
    Pollination Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.3.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class OrgDto(object):
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
        'picture': 'str',
        'contact_email': 'str',
        'description': 'str',
        'account_name': 'str',
        'id': 'str',
        'member_count': 'int',
        'team_count': 'int'
    }

    attribute_map = {
        'name': 'name',
        'picture': 'picture',
        'contact_email': 'contact_email',
        'description': 'description',
        'account_name': 'account_name',
        'id': 'id',
        'member_count': 'member_count',
        'team_count': 'team_count'
    }

    def __init__(self, name=None, picture=None, contact_email=None, description='', account_name=None, id=None, member_count=0, team_count=0, local_vars_configuration=None):  # noqa: E501
        """OrgDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._picture = None
        self._contact_email = None
        self._description = None
        self._account_name = None
        self._id = None
        self._member_count = None
        self._team_count = None
        self.discriminator = None

        self.name = name
        self.picture = picture
        self.contact_email = contact_email
        if description is not None:
            self.description = description
        self.account_name = account_name
        self.id = id
        if member_count is not None:
            self.member_count = member_count
        if team_count is not None:
            self.team_count = team_count

    @property
    def name(self):
        """Gets the name of this OrgDto.  # noqa: E501

        The pretty name of the org  # noqa: E501

        :return: The name of this OrgDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrgDto.

        The pretty name of the org  # noqa: E501

        :param name: The name of this OrgDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def picture(self):
        """Gets the picture of this OrgDto.  # noqa: E501

        The avatar picture for the Org  # noqa: E501

        :return: The picture of this OrgDto.  # noqa: E501
        :rtype: str
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        """Sets the picture of this OrgDto.

        The avatar picture for the Org  # noqa: E501

        :param picture: The picture of this OrgDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and picture is None:  # noqa: E501
            raise ValueError("Invalid value for `picture`, must not be `None`")  # noqa: E501

        self._picture = picture

    @property
    def contact_email(self):
        """Gets the contact_email of this OrgDto.  # noqa: E501

        The contact email for the organisation  # noqa: E501

        :return: The contact_email of this OrgDto.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this OrgDto.

        The contact email for the organisation  # noqa: E501

        :param contact_email: The contact_email of this OrgDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and contact_email is None:  # noqa: E501
            raise ValueError("Invalid value for `contact_email`, must not be `None`")  # noqa: E501

        self._contact_email = contact_email

    @property
    def description(self):
        """Gets the description of this OrgDto.  # noqa: E501

        A description of the org  # noqa: E501

        :return: The description of this OrgDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OrgDto.

        A description of the org  # noqa: E501

        :param description: The description of this OrgDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def account_name(self):
        """Gets the account_name of this OrgDto.  # noqa: E501

        The unique name of the org in small case without spaces  # noqa: E501

        :return: The account_name of this OrgDto.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this OrgDto.

        The unique name of the org in small case without spaces  # noqa: E501

        :param account_name: The account_name of this OrgDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and account_name is None:  # noqa: E501
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def id(self):
        """Gets the id of this OrgDto.  # noqa: E501

        The org ID  # noqa: E501

        :return: The id of this OrgDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrgDto.

        The org ID  # noqa: E501

        :param id: The id of this OrgDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def member_count(self):
        """Gets the member_count of this OrgDto.  # noqa: E501

        The number of members that are part of this org  # noqa: E501

        :return: The member_count of this OrgDto.  # noqa: E501
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """Sets the member_count of this OrgDto.

        The number of members that are part of this org  # noqa: E501

        :param member_count: The member_count of this OrgDto.  # noqa: E501
        :type: int
        """

        self._member_count = member_count

    @property
    def team_count(self):
        """Gets the team_count of this OrgDto.  # noqa: E501

        The number of teams that are part of this org  # noqa: E501

        :return: The team_count of this OrgDto.  # noqa: E501
        :rtype: int
        """
        return self._team_count

    @team_count.setter
    def team_count(self, team_count):
        """Sets the team_count of this OrgDto.

        The number of teams that are part of this org  # noqa: E501

        :param team_count: The team_count of this OrgDto.  # noqa: E501
        :type: int
        """

        self._team_count = team_count

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
        if not isinstance(other, OrgDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrgDto):
            return True

        return self.to_dict() != other.to_dict()
