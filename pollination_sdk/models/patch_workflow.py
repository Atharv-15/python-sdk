# coding: utf-8

"""
    Pollination Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class PatchWorkflow(object):
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
        'type': 'str',
        'name': 'str',
        'id': 'str',
        'inputs': 'Arguments',
        'operators': 'list[Operator]',
        'templates': 'list[AnyOfFunctionDAGWorkflow]',
        'flow': 'DAG',
        'outputs': 'Arguments',
        'artifact_locations': 'list[AnyOfRunFolderLocationInputFolderLocationHTTPLocationS3Location]',
        'public': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'id': 'id',
        'inputs': 'inputs',
        'operators': 'operators',
        'templates': 'templates',
        'flow': 'flow',
        'outputs': 'outputs',
        'artifact_locations': 'artifact_locations',
        'public': 'public'
    }

    def __init__(self, type=None, name=None, id='9c1692f8-d8c3-43df-9704-bb529f9aebb8', inputs=None, operators=None, templates=None, flow=None, outputs=None, artifact_locations=None, public=None, local_vars_configuration=None):  # noqa: E501
        """PatchWorkflow - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._id = None
        self._inputs = None
        self._operators = None
        self._templates = None
        self._flow = None
        self._outputs = None
        self._artifact_locations = None
        self._public = None
        self.discriminator = None

        self.type = type
        self.name = name
        if id is not None:
            self.id = id
        if inputs is not None:
            self.inputs = inputs
        self.operators = operators
        self.templates = templates
        self.flow = flow
        if outputs is not None:
            self.outputs = outputs
        if artifact_locations is not None:
            self.artifact_locations = artifact_locations
        self.public = public

    @property
    def type(self):
        """Gets the type of this PatchWorkflow.  # noqa: E501


        :return: The type of this PatchWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PatchWorkflow.


        :param type: The type of this PatchWorkflow.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^workflow$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^workflow$/`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this PatchWorkflow.  # noqa: E501


        :return: The name of this PatchWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchWorkflow.


        :param name: The name of this PatchWorkflow.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this PatchWorkflow.  # noqa: E501


        :return: The id of this PatchWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PatchWorkflow.


        :param id: The id of this PatchWorkflow.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def inputs(self):
        """Gets the inputs of this PatchWorkflow.  # noqa: E501


        :return: The inputs of this PatchWorkflow.  # noqa: E501
        :rtype: Arguments
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this PatchWorkflow.


        :param inputs: The inputs of this PatchWorkflow.  # noqa: E501
        :type: Arguments
        """

        self._inputs = inputs

    @property
    def operators(self):
        """Gets the operators of this PatchWorkflow.  # noqa: E501


        :return: The operators of this PatchWorkflow.  # noqa: E501
        :rtype: list[Operator]
        """
        return self._operators

    @operators.setter
    def operators(self, operators):
        """Sets the operators of this PatchWorkflow.


        :param operators: The operators of this PatchWorkflow.  # noqa: E501
        :type: list[Operator]
        """
        if self.local_vars_configuration.client_side_validation and operators is None:  # noqa: E501
            raise ValueError("Invalid value for `operators`, must not be `None`")  # noqa: E501

        self._operators = operators

    @property
    def templates(self):
        """Gets the templates of this PatchWorkflow.  # noqa: E501

        A list of templates. Templates can be Function, DAG or a Workflow.  # noqa: E501

        :return: The templates of this PatchWorkflow.  # noqa: E501
        :rtype: list[AnyOfFunctionDAGWorkflow]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this PatchWorkflow.

        A list of templates. Templates can be Function, DAG or a Workflow.  # noqa: E501

        :param templates: The templates of this PatchWorkflow.  # noqa: E501
        :type: list[AnyOfFunctionDAGWorkflow]
        """
        if self.local_vars_configuration.client_side_validation and templates is None:  # noqa: E501
            raise ValueError("Invalid value for `templates`, must not be `None`")  # noqa: E501

        self._templates = templates

    @property
    def flow(self):
        """Gets the flow of this PatchWorkflow.  # noqa: E501

        A list of tasks to create a DAG workflow.  # noqa: E501

        :return: The flow of this PatchWorkflow.  # noqa: E501
        :rtype: DAG
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this PatchWorkflow.

        A list of tasks to create a DAG workflow.  # noqa: E501

        :param flow: The flow of this PatchWorkflow.  # noqa: E501
        :type: DAG
        """
        if self.local_vars_configuration.client_side_validation and flow is None:  # noqa: E501
            raise ValueError("Invalid value for `flow`, must not be `None`")  # noqa: E501

        self._flow = flow

    @property
    def outputs(self):
        """Gets the outputs of this PatchWorkflow.  # noqa: E501


        :return: The outputs of this PatchWorkflow.  # noqa: E501
        :rtype: Arguments
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this PatchWorkflow.


        :param outputs: The outputs of this PatchWorkflow.  # noqa: E501
        :type: Arguments
        """

        self._outputs = outputs

    @property
    def artifact_locations(self):
        """Gets the artifact_locations of this PatchWorkflow.  # noqa: E501

        A list of artifact locations which can be used by flow objects.  # noqa: E501

        :return: The artifact_locations of this PatchWorkflow.  # noqa: E501
        :rtype: list[AnyOfRunFolderLocationInputFolderLocationHTTPLocationS3Location]
        """
        return self._artifact_locations

    @artifact_locations.setter
    def artifact_locations(self, artifact_locations):
        """Sets the artifact_locations of this PatchWorkflow.

        A list of artifact locations which can be used by flow objects.  # noqa: E501

        :param artifact_locations: The artifact_locations of this PatchWorkflow.  # noqa: E501
        :type: list[AnyOfRunFolderLocationInputFolderLocationHTTPLocationS3Location]
        """

        self._artifact_locations = artifact_locations

    @property
    def public(self):
        """Gets the public of this PatchWorkflow.  # noqa: E501

        A boolean indicator of whether workflow is public or not  # noqa: E501

        :return: The public of this PatchWorkflow.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this PatchWorkflow.

        A boolean indicator of whether workflow is public or not  # noqa: E501

        :param public: The public of this PatchWorkflow.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and public is None:  # noqa: E501
            raise ValueError("Invalid value for `public`, must not be `None`")  # noqa: E501

        self._public = public

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
        if not isinstance(other, PatchWorkflow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchWorkflow):
            return True

        return self.to_dict() != other.to_dict()
