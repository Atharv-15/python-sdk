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


class Subscription(object):
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
        'billing_info': 'BillingInfo',
        'external_id': 'str',
        'id': 'str',
        'owner': 'AccountPublic',
        'period_end': 'datetime',
        'period_start': 'datetime',
        'plan_multiplier': 'int',
        'plan_slug': 'str',
        'type': 'PlanType'
    }

    attribute_map = {
        'billing_info': 'billing_info',
        'external_id': 'external_id',
        'id': 'id',
        'owner': 'owner',
        'period_end': 'period_end',
        'period_start': 'period_start',
        'plan_multiplier': 'plan_multiplier',
        'plan_slug': 'plan_slug',
        'type': 'type'
    }

    def __init__(self, billing_info=None, external_id=None, id=None, owner=None, period_end=None, period_start=None, plan_multiplier=1, plan_slug=None, type=None, local_vars_configuration=None):  # noqa: E501
        """Subscription - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._billing_info = None
        self._external_id = None
        self._id = None
        self._owner = None
        self._period_end = None
        self._period_start = None
        self._plan_multiplier = None
        self._plan_slug = None
        self._type = None
        self.discriminator = None

        if billing_info is not None:
            self.billing_info = billing_info
        if external_id is not None:
            self.external_id = external_id
        self.id = id
        self.owner = owner
        self.period_end = period_end
        self.period_start = period_start
        if plan_multiplier is not None:
            self.plan_multiplier = plan_multiplier
        self.plan_slug = plan_slug
        self.type = type

    @property
    def billing_info(self):
        """Gets the billing_info of this Subscription.  # noqa: E501

        The billing info for the subscription  # noqa: E501

        :return: The billing_info of this Subscription.  # noqa: E501
        :rtype: BillingInfo
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this Subscription.

        The billing info for the subscription  # noqa: E501

        :param billing_info: The billing_info of this Subscription.  # noqa: E501
        :type billing_info: BillingInfo
        """

        self._billing_info = billing_info

    @property
    def external_id(self):
        """Gets the external_id of this Subscription.  # noqa: E501

        The ID of this subscription  # noqa: E501

        :return: The external_id of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Subscription.

        The ID of this subscription  # noqa: E501

        :param external_id: The external_id of this Subscription.  # noqa: E501
        :type external_id: str
        """

        self._external_id = external_id

    @property
    def id(self):
        """Gets the id of this Subscription.  # noqa: E501

        The unique ID of this subscription  # noqa: E501

        :return: The id of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Subscription.

        The unique ID of this subscription  # noqa: E501

        :param id: The id of this Subscription.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def owner(self):
        """Gets the owner of this Subscription.  # noqa: E501

        The owner of the repository  # noqa: E501

        :return: The owner of this Subscription.  # noqa: E501
        :rtype: AccountPublic
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Subscription.

        The owner of the repository  # noqa: E501

        :param owner: The owner of this Subscription.  # noqa: E501
        :type owner: AccountPublic
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def period_end(self):
        """Gets the period_end of this Subscription.  # noqa: E501

        The end of the current subscription period  # noqa: E501

        :return: The period_end of this Subscription.  # noqa: E501
        :rtype: datetime
        """
        return self._period_end

    @period_end.setter
    def period_end(self, period_end):
        """Sets the period_end of this Subscription.

        The end of the current subscription period  # noqa: E501

        :param period_end: The period_end of this Subscription.  # noqa: E501
        :type period_end: datetime
        """
        if self.local_vars_configuration.client_side_validation and period_end is None:  # noqa: E501
            raise ValueError("Invalid value for `period_end`, must not be `None`")  # noqa: E501

        self._period_end = period_end

    @property
    def period_start(self):
        """Gets the period_start of this Subscription.  # noqa: E501

        The start of the current subscription period  # noqa: E501

        :return: The period_start of this Subscription.  # noqa: E501
        :rtype: datetime
        """
        return self._period_start

    @period_start.setter
    def period_start(self, period_start):
        """Sets the period_start of this Subscription.

        The start of the current subscription period  # noqa: E501

        :param period_start: The period_start of this Subscription.  # noqa: E501
        :type period_start: datetime
        """
        if self.local_vars_configuration.client_side_validation and period_start is None:  # noqa: E501
            raise ValueError("Invalid value for `period_start`, must not be `None`")  # noqa: E501

        self._period_start = period_start

    @property
    def plan_multiplier(self):
        """Gets the plan_multiplier of this Subscription.  # noqa: E501

        The number of times to multiply the plan limit by  # noqa: E501

        :return: The plan_multiplier of this Subscription.  # noqa: E501
        :rtype: int
        """
        return self._plan_multiplier

    @plan_multiplier.setter
    def plan_multiplier(self, plan_multiplier):
        """Sets the plan_multiplier of this Subscription.

        The number of times to multiply the plan limit by  # noqa: E501

        :param plan_multiplier: The plan_multiplier of this Subscription.  # noqa: E501
        :type plan_multiplier: int
        """

        self._plan_multiplier = plan_multiplier

    @property
    def plan_slug(self):
        """Gets the plan_slug of this Subscription.  # noqa: E501

        The slug of the plan used to create this subscription  # noqa: E501

        :return: The plan_slug of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._plan_slug

    @plan_slug.setter
    def plan_slug(self, plan_slug):
        """Sets the plan_slug of this Subscription.

        The slug of the plan used to create this subscription  # noqa: E501

        :param plan_slug: The plan_slug of this Subscription.  # noqa: E501
        :type plan_slug: str
        """
        if self.local_vars_configuration.client_side_validation and plan_slug is None:  # noqa: E501
            raise ValueError("Invalid value for `plan_slug`, must not be `None`")  # noqa: E501

        self._plan_slug = plan_slug

    @property
    def type(self):
        """Gets the type of this Subscription.  # noqa: E501

        The type of subscription  # noqa: E501

        :return: The type of this Subscription.  # noqa: E501
        :rtype: PlanType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Subscription.

        The type of subscription  # noqa: E501

        :param type: The type of this Subscription.  # noqa: E501
        :type type: PlanType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, Subscription):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Subscription):
            return True

        return self.to_dict() != other.to_dict()
