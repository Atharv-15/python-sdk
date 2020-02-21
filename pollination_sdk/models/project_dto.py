# coding: utf-8

"""
    Pollination Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.2.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class ProjectDto(object):
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
        'description': 'str',
        'public': 'bool',
        'id': 'str',
        'owner': 'AccountPublic',
        'permissions': 'ProjectPermissions',
        'slug': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'public': 'public',
        'id': 'id',
        'owner': 'owner',
        'permissions': 'permissions',
        'slug': 'slug'
    }

    def __init__(self, name=None, description='', public=True, id=None, owner=None, permissions=None, slug=None, local_vars_configuration=None):  # noqa: E501
        """ProjectDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._public = None
        self._id = None
        self._owner = None
        self._permissions = None
        self._slug = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if public is not None:
            self.public = public
        self.id = id
        self.owner = owner
        self.permissions = permissions
        self.slug = slug

    @property
    def name(self):
        """Gets the name of this ProjectDto.  # noqa: E501

        The name of the project. Must be unique to a given owner  # noqa: E501

        :return: The name of this ProjectDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectDto.

        The name of the project. Must be unique to a given owner  # noqa: E501

        :param name: The name of this ProjectDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ProjectDto.  # noqa: E501

        A description of the project  # noqa: E501

        :return: The description of this ProjectDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectDto.

        A description of the project  # noqa: E501

        :param description: The description of this ProjectDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def public(self):
        """Gets the public of this ProjectDto.  # noqa: E501

        Whether or not a project is publicly viewable  # noqa: E501

        :return: The public of this ProjectDto.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this ProjectDto.

        Whether or not a project is publicly viewable  # noqa: E501

        :param public: The public of this ProjectDto.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def id(self):
        """Gets the id of this ProjectDto.  # noqa: E501

        The project ID  # noqa: E501

        :return: The id of this ProjectDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectDto.

        The project ID  # noqa: E501

        :param id: The id of this ProjectDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def owner(self):
        """Gets the owner of this ProjectDto.  # noqa: E501


        :return: The owner of this ProjectDto.  # noqa: E501
        :rtype: AccountPublic
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ProjectDto.


        :param owner: The owner of this ProjectDto.  # noqa: E501
        :type: AccountPublic
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def permissions(self):
        """Gets the permissions of this ProjectDto.  # noqa: E501


        :return: The permissions of this ProjectDto.  # noqa: E501
        :rtype: ProjectPermissions
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this ProjectDto.


        :param permissions: The permissions of this ProjectDto.  # noqa: E501
        :type: ProjectPermissions
        """
        if self.local_vars_configuration.client_side_validation and permissions is None:  # noqa: E501
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501

        self._permissions = permissions

    @property
    def slug(self):
        """Gets the slug of this ProjectDto.  # noqa: E501

        The project name in slug format  # noqa: E501

        :return: The slug of this ProjectDto.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this ProjectDto.

        The project name in slug format  # noqa: E501

        :param slug: The slug of this ProjectDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and slug is None:  # noqa: E501
            raise ValueError("Invalid value for `slug`, must not be `None`")  # noqa: E501

        self._slug = slug

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
        if not isinstance(other, ProjectDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectDto):
            return True

        return self.to_dict() != other.to_dict()
