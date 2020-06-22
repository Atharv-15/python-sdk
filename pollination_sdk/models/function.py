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


class Function(object):
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
        'inputs': 'FunctionInputs',
        'command': 'str',
        'outputs': 'FunctionOutputs'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'inputs': 'inputs',
        'command': 'command',
        'outputs': 'outputs'
    }

    def __init__(self, name=None, description=None, inputs=None, command=None, outputs=None, local_vars_configuration=None):  # noqa: E501
        """Function - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._inputs = None
        self._command = None
        self._outputs = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if inputs is not None:
            self.inputs = inputs
        self.command = command
        if outputs is not None:
            self.outputs = outputs

    @property
    def name(self):
        """Gets the name of this Function.  # noqa: E501

        Function name. Must be unique within an operator.  # noqa: E501

        :return: The name of this Function.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Function.

        Function name. Must be unique within an operator.  # noqa: E501

        :param name: The name of this Function.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Function.  # noqa: E501

        Function description. A short human readable description for this function.  # noqa: E501

        :return: The description of this Function.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Function.

        Function description. A short human readable description for this function.  # noqa: E501

        :param description: The description of this Function.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def inputs(self):
        """Gets the inputs of this Function.  # noqa: E501

        Input arguments for this function.  # noqa: E501

        :return: The inputs of this Function.  # noqa: E501
        :rtype: FunctionInputs
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this Function.

        Input arguments for this function.  # noqa: E501

        :param inputs: The inputs of this Function.  # noqa: E501
        :type: FunctionInputs
        """

        self._inputs = inputs

    @property
    def command(self):
        """Gets the command of this Function.  # noqa: E501

        Full shell command for this function. Each function accepts only one command. The command will be executed as a shell command in operator. For running several commands after each other use && between the commands or pipe data from one to another using |  # noqa: E501

        :return: The command of this Function.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this Function.

        Full shell command for this function. Each function accepts only one command. The command will be executed as a shell command in operator. For running several commands after each other use && between the commands or pipe data from one to another using |  # noqa: E501

        :param command: The command of this Function.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and command is None:  # noqa: E501
            raise ValueError("Invalid value for `command`, must not be `None`")  # noqa: E501

        self._command = command

    @property
    def outputs(self):
        """Gets the outputs of this Function.  # noqa: E501

        List of output arguments.  # noqa: E501

        :return: The outputs of this Function.  # noqa: E501
        :rtype: FunctionOutputs
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this Function.

        List of output arguments.  # noqa: E501

        :param outputs: The outputs of this Function.  # noqa: E501
        :type: FunctionOutputs
        """

        self._outputs = outputs

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
        if not isinstance(other, Function):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Function):
            return True

        return self.to_dict() != other.to_dict()
