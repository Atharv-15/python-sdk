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


class DockerConfig(object):
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
        'annotations': 'dict(str, str)',
        'image': 'str',
        'registry': 'str',
        'type': 'str',
        'workdir': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'image': 'image',
        'registry': 'registry',
        'type': 'type',
        'workdir': 'workdir'
    }

    def __init__(self, annotations=None, image=None, registry=None, type='DockerConfig', workdir=None, local_vars_configuration=None):  # noqa: E501
        """DockerConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._image = None
        self._registry = None
        self._type = None
        self._workdir = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        self.image = image
        if registry is not None:
            self.registry = registry
        if type is not None:
            self.type = type
        self.workdir = workdir

    @property
    def annotations(self):
        """Gets the annotations of this DockerConfig.  # noqa: E501

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :return: The annotations of this DockerConfig.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this DockerConfig.

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :param annotations: The annotations of this DockerConfig.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def image(self):
        """Gets the image of this DockerConfig.  # noqa: E501

        Docker image name. Must include tag.  # noqa: E501

        :return: The image of this DockerConfig.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this DockerConfig.

        Docker image name. Must include tag.  # noqa: E501

        :param image: The image of this DockerConfig.  # noqa: E501
        :type image: str
        """
        if self.local_vars_configuration.client_side_validation and image is None:  # noqa: E501
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

    @property
    def registry(self):
        """Gets the registry of this DockerConfig.  # noqa: E501

        The container registry URLs that this container should be pulled from. Will default to Dockerhub if none is specified.  # noqa: E501

        :return: The registry of this DockerConfig.  # noqa: E501
        :rtype: str
        """
        return self._registry

    @registry.setter
    def registry(self, registry):
        """Sets the registry of this DockerConfig.

        The container registry URLs that this container should be pulled from. Will default to Dockerhub if none is specified.  # noqa: E501

        :param registry: The registry of this DockerConfig.  # noqa: E501
        :type registry: str
        """

        self._registry = registry

    @property
    def type(self):
        """Gets the type of this DockerConfig.  # noqa: E501


        :return: The type of this DockerConfig.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DockerConfig.


        :param type: The type of this DockerConfig.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^DockerConfig', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^DockerConfig/`")  # noqa: E501

        self._type = type

    @property
    def workdir(self):
        """Gets the workdir of this DockerConfig.  # noqa: E501

        The working directory the entrypoint command of the container runsin. This is used to determine where to load artifacts when running in the container.  # noqa: E501

        :return: The workdir of this DockerConfig.  # noqa: E501
        :rtype: str
        """
        return self._workdir

    @workdir.setter
    def workdir(self, workdir):
        """Sets the workdir of this DockerConfig.

        The working directory the entrypoint command of the container runsin. This is used to determine where to load artifacts when running in the container.  # noqa: E501

        :param workdir: The workdir of this DockerConfig.  # noqa: E501
        :type workdir: str
        """
        if self.local_vars_configuration.client_side_validation and workdir is None:  # noqa: E501
            raise ValueError("Invalid value for `workdir`, must not be `None`")  # noqa: E501

        self._workdir = workdir

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
        if not isinstance(other, DockerConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerConfig):
            return True

        return self.to_dict() != other.to_dict()
