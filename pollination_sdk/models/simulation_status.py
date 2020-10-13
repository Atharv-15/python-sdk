# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: 0.10.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class SimulationStatus(object):
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
        'account_id': 'str',
        'entrypoint': 'str',
        'finished_at': 'datetime',
        'id': 'str',
        'message': 'str',
        'parallelism': 'int',
        'project_id': 'str',
        'recipe_account_id': 'str',
        'recipe_id': 'str',
        'recipe_package_id': 'str',
        'started_at': 'datetime',
        'status': 'str',
        'tasks': 'dict(str, TaskStatus)'
    }

    attribute_map = {
        'account_id': 'account_id',
        'entrypoint': 'entrypoint',
        'finished_at': 'finished_at',
        'id': 'id',
        'message': 'message',
        'parallelism': 'parallelism',
        'project_id': 'project_id',
        'recipe_account_id': 'recipe_account_id',
        'recipe_id': 'recipe_id',
        'recipe_package_id': 'recipe_package_id',
        'started_at': 'started_at',
        'status': 'status',
        'tasks': 'tasks'
    }

    def __init__(self, account_id=None, entrypoint=None, finished_at=None, id=None, message=None, parallelism=None, project_id=None, recipe_account_id=None, recipe_id=None, recipe_package_id=None, started_at=None, status=None, tasks=None, local_vars_configuration=None):  # noqa: E501
        """SimulationStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._entrypoint = None
        self._finished_at = None
        self._id = None
        self._message = None
        self._parallelism = None
        self._project_id = None
        self._recipe_account_id = None
        self._recipe_id = None
        self._recipe_package_id = None
        self._started_at = None
        self._status = None
        self._tasks = None
        self.discriminator = None

        self.account_id = account_id
        if entrypoint is not None:
            self.entrypoint = entrypoint
        if finished_at is not None:
            self.finished_at = finished_at
        self.id = id
        if message is not None:
            self.message = message
        if parallelism is not None:
            self.parallelism = parallelism
        self.project_id = project_id
        self.recipe_account_id = recipe_account_id
        self.recipe_id = recipe_id
        self.recipe_package_id = recipe_package_id
        self.started_at = started_at
        self.status = status
        if tasks is not None:
            self.tasks = tasks

    @property
    def account_id(self):
        """Gets the account_id of this SimulationStatus.  # noqa: E501

        ID of the account the simulation is running for.  # noqa: E501

        :return: The account_id of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this SimulationStatus.

        ID of the account the simulation is running for.  # noqa: E501

        :param account_id: The account_id of this SimulationStatus.  # noqa: E501
        :type account_id: str
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def entrypoint(self):
        """Gets the entrypoint of this SimulationStatus.  # noqa: E501

        The ID of the first task in the workflow  # noqa: E501

        :return: The entrypoint of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint):
        """Sets the entrypoint of this SimulationStatus.

        The ID of the first task in the workflow  # noqa: E501

        :param entrypoint: The entrypoint of this SimulationStatus.  # noqa: E501
        :type entrypoint: str
        """

        self._entrypoint = entrypoint

    @property
    def finished_at(self):
        """Gets the finished_at of this SimulationStatus.  # noqa: E501

        The time at which the task was completed  # noqa: E501

        :return: The finished_at of this SimulationStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this SimulationStatus.

        The time at which the task was completed  # noqa: E501

        :param finished_at: The finished_at of this SimulationStatus.  # noqa: E501
        :type finished_at: datetime
        """

        self._finished_at = finished_at

    @property
    def id(self):
        """Gets the id of this SimulationStatus.  # noqa: E501

        The ID of the individual workflow run.  # noqa: E501

        :return: The id of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimulationStatus.

        The ID of the individual workflow run.  # noqa: E501

        :param id: The id of this SimulationStatus.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def message(self):
        """Gets the message of this SimulationStatus.  # noqa: E501

        Any message produced by the task. Usually error/debugging hints.  # noqa: E501

        :return: The message of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SimulationStatus.

        Any message produced by the task. Usually error/debugging hints.  # noqa: E501

        :param message: The message of this SimulationStatus.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def parallelism(self):
        """Gets the parallelism of this SimulationStatus.  # noqa: E501

        The max number of parallel tasks running for this simulation  # noqa: E501

        :return: The parallelism of this SimulationStatus.  # noqa: E501
        :rtype: int
        """
        return self._parallelism

    @parallelism.setter
    def parallelism(self, parallelism):
        """Sets the parallelism of this SimulationStatus.

        The max number of parallel tasks running for this simulation  # noqa: E501

        :param parallelism: The parallelism of this SimulationStatus.  # noqa: E501
        :type parallelism: int
        """

        self._parallelism = parallelism

    @property
    def project_id(self):
        """Gets the project_id of this SimulationStatus.  # noqa: E501

        ID of the project the simulation belongs to  # noqa: E501

        :return: The project_id of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SimulationStatus.

        ID of the project the simulation belongs to  # noqa: E501

        :param project_id: The project_id of this SimulationStatus.  # noqa: E501
        :type project_id: str
        """
        if self.local_vars_configuration.client_side_validation and project_id is None:  # noqa: E501
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def recipe_account_id(self):
        """Gets the recipe_account_id of this SimulationStatus.  # noqa: E501

        ID of the recipe owner  # noqa: E501

        :return: The recipe_account_id of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._recipe_account_id

    @recipe_account_id.setter
    def recipe_account_id(self, recipe_account_id):
        """Sets the recipe_account_id of this SimulationStatus.

        ID of the recipe owner  # noqa: E501

        :param recipe_account_id: The recipe_account_id of this SimulationStatus.  # noqa: E501
        :type recipe_account_id: str
        """
        if self.local_vars_configuration.client_side_validation and recipe_account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `recipe_account_id`, must not be `None`")  # noqa: E501

        self._recipe_account_id = recipe_account_id

    @property
    def recipe_id(self):
        """Gets the recipe_id of this SimulationStatus.  # noqa: E501

        ID of the recipe repository used to create the workflow  # noqa: E501

        :return: The recipe_id of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._recipe_id

    @recipe_id.setter
    def recipe_id(self, recipe_id):
        """Sets the recipe_id of this SimulationStatus.

        ID of the recipe repository used to create the workflow  # noqa: E501

        :param recipe_id: The recipe_id of this SimulationStatus.  # noqa: E501
        :type recipe_id: str
        """
        if self.local_vars_configuration.client_side_validation and recipe_id is None:  # noqa: E501
            raise ValueError("Invalid value for `recipe_id`, must not be `None`")  # noqa: E501

        self._recipe_id = recipe_id

    @property
    def recipe_package_id(self):
        """Gets the recipe_package_id of this SimulationStatus.  # noqa: E501

        ID of the specific recipe package used to create the workflow  # noqa: E501

        :return: The recipe_package_id of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._recipe_package_id

    @recipe_package_id.setter
    def recipe_package_id(self, recipe_package_id):
        """Sets the recipe_package_id of this SimulationStatus.

        ID of the specific recipe package used to create the workflow  # noqa: E501

        :param recipe_package_id: The recipe_package_id of this SimulationStatus.  # noqa: E501
        :type recipe_package_id: str
        """
        if self.local_vars_configuration.client_side_validation and recipe_package_id is None:  # noqa: E501
            raise ValueError("Invalid value for `recipe_package_id`, must not be `None`")  # noqa: E501

        self._recipe_package_id = recipe_package_id

    @property
    def started_at(self):
        """Gets the started_at of this SimulationStatus.  # noqa: E501

        The time at which the task was started  # noqa: E501

        :return: The started_at of this SimulationStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this SimulationStatus.

        The time at which the task was started  # noqa: E501

        :param started_at: The started_at of this SimulationStatus.  # noqa: E501
        :type started_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and started_at is None:  # noqa: E501
            raise ValueError("Invalid value for `started_at`, must not be `None`")  # noqa: E501

        self._started_at = started_at

    @property
    def status(self):
        """Gets the status of this SimulationStatus.  # noqa: E501

        The status of this task. Can be \"Running\", \"Succeeded\", \"Failed\" or \"Error\"  # noqa: E501

        :return: The status of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SimulationStatus.

        The status of this task. Can be \"Running\", \"Succeeded\", \"Failed\" or \"Error\"  # noqa: E501

        :param status: The status of this SimulationStatus.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def tasks(self):
        """Gets the tasks of this SimulationStatus.  # noqa: E501


        :return: The tasks of this SimulationStatus.  # noqa: E501
        :rtype: dict(str, TaskStatus)
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this SimulationStatus.


        :param tasks: The tasks of this SimulationStatus.  # noqa: E501
        :type tasks: dict(str, TaskStatus)
        """

        self._tasks = tasks

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
        if not isinstance(other, SimulationStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimulationStatus):
            return True

        return self.to_dict() != other.to_dict()
