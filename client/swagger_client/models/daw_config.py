# coding: utf-8

"""
    dawpy server

    This is the daw server api  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DawConfig(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'config_name': 'str',
        'daw_config_path': 'str',
        'mrs_watson_64bit_path': 'str',
        'mrs_watson_32bit_path': 'str',
        'nano_host_64bit_path': 'str',
        'nano_host_32bit_path': 'str',
        'pattern_path': 'str',
        'plugin_path': 'str',
        'preset_path': 'str',
        'projects_path': 'str',
        'rendered_path': 'str'
    }

    attribute_map = {
        'config_name': 'config_name',
        'daw_config_path': 'daw_config_path',
        'mrs_watson_64bit_path': 'mrs_watson_64bit_path',
        'mrs_watson_32bit_path': 'mrs_watson_32bit_path',
        'nano_host_64bit_path': 'nano_host_64bit_path',
        'nano_host_32bit_path': 'nano_host_32bit_path',
        'pattern_path': 'pattern_path',
        'plugin_path': 'plugin_path',
        'preset_path': 'preset_path',
        'projects_path': 'projects_path',
        'rendered_path': 'rendered_path'
    }

    def __init__(self, config_name=None, daw_config_path=None, mrs_watson_64bit_path=None, mrs_watson_32bit_path=None, nano_host_64bit_path=None, nano_host_32bit_path=None, pattern_path=None, plugin_path=None, preset_path=None, projects_path=None, rendered_path=None):  # noqa: E501
        """DawConfig - a model defined in Swagger"""  # noqa: E501
        self._config_name = None
        self._daw_config_path = None
        self._mrs_watson_64bit_path = None
        self._mrs_watson_32bit_path = None
        self._nano_host_64bit_path = None
        self._nano_host_32bit_path = None
        self._pattern_path = None
        self._plugin_path = None
        self._preset_path = None
        self._projects_path = None
        self._rendered_path = None
        self.discriminator = None
        if config_name is not None:
            self.config_name = config_name
        if daw_config_path is not None:
            self.daw_config_path = daw_config_path
        if mrs_watson_64bit_path is not None:
            self.mrs_watson_64bit_path = mrs_watson_64bit_path
        if mrs_watson_32bit_path is not None:
            self.mrs_watson_32bit_path = mrs_watson_32bit_path
        if nano_host_64bit_path is not None:
            self.nano_host_64bit_path = nano_host_64bit_path
        if nano_host_32bit_path is not None:
            self.nano_host_32bit_path = nano_host_32bit_path
        if pattern_path is not None:
            self.pattern_path = pattern_path
        if plugin_path is not None:
            self.plugin_path = plugin_path
        if preset_path is not None:
            self.preset_path = preset_path
        if projects_path is not None:
            self.projects_path = projects_path
        if rendered_path is not None:
            self.rendered_path = rendered_path

    @property
    def config_name(self):
        """Gets the config_name of this DawConfig.  # noqa: E501


        :return: The config_name of this DawConfig.  # noqa: E501
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        """Sets the config_name of this DawConfig.


        :param config_name: The config_name of this DawConfig.  # noqa: E501
        :type: str
        """

        self._config_name = config_name

    @property
    def daw_config_path(self):
        """Gets the daw_config_path of this DawConfig.  # noqa: E501


        :return: The daw_config_path of this DawConfig.  # noqa: E501
        :rtype: str
        """
        return self._daw_config_path

    @daw_config_path.setter
    def daw_config_path(self, daw_config_path):
        """Sets the daw_config_path of this DawConfig.


        :param daw_config_path: The daw_config_path of this DawConfig.  # noqa: E501
        :type: str
        """

        self._daw_config_path = daw_config_path

    @property
    def mrs_watson_64bit_path(self):
        """Gets the mrs_watson_64bit_path of this DawConfig.  # noqa: E501


        :return: The mrs_watson_64bit_path of this DawConfig.  # noqa: E501
        :rtype: str
        """
        return self._mrs_watson_64bit_path

    @mrs_watson_64bit_path.setter
    def mrs_watson_64bit_path(self, mrs_watson_64bit_path):
        """Sets the mrs_watson_64bit_path of this DawConfig.


        :param mrs_watson_64bit_path: The mrs_watson_64bit_path of this DawConfig.  # noqa: E501
        :type: str
        """

        self._mrs_watson_64bit_path = mrs_watson_64bit_path

    @property
    def mrs_watson_32bit_path(self):
        """Gets the mrs_watson_32bit_path of this DawConfig.  # noqa: E501


        :return: The mrs_watson_32bit_path of this DawConfig.  # noqa: E501
        :rtype: str
        """
        return self._mrs_watson_32bit_path

    @mrs_watson_32bit_path.setter
    def mrs_watson_32bit_path(self, mrs_watson_32bit_path):
        """Sets the mrs_watson_32bit_path of this DawConfig.


        :param mrs_watson_32bit_path: The mrs_watson_32bit_path of this DawConfig.  # noqa: E501
        :type: str
        """

        self._mrs_watson_32bit_path = mrs_watson_32bit_path

    @property
    def nano_host_64bit_path(self):
        """Gets the nano_host_64bit_path of this DawConfig.  # noqa: E501


        :return: The nano_host_64bit_path of this DawConfig.  # noqa: E501
        :rtype: str
        """
        return self._nano_host_64bit_path

    @nano_host_64bit_path.setter
    def nano_host_64bit_path(self, nano_host_64bit_path):
        """Sets the nano_host_64bit_path of this DawConfig.


        :param nano_host_64bit_path: The nano_host_64bit_path of this DawConfig.  # noqa: E501
        :type: str
        """

        self._nano_host_64bit_path = nano_host_64bit_path

    @property
    def nano_host_32bit_path(self):
        """Gets the nano_host_32bit_path of this DawConfig.  # noqa: E501


        :return: The nano_host_32bit_path of this DawConfig.  # noqa: E501
        :rtype: str
        """
        return self._nano_host_32bit_path

    @nano_host_32bit_path.setter
    def nano_host_32bit_path(self, nano_host_32bit_path):
        """Sets the nano_host_32bit_path of this DawConfig.


        :param nano_host_32bit_path: The nano_host_32bit_path of this DawConfig.  # noqa: E501
        :type: str
        """

        self._nano_host_32bit_path = nano_host_32bit_path

    @property
    def pattern_path(self):
        """Gets the pattern_path of this DawConfig.  # noqa: E501


        :return: The pattern_path of this DawConfig.  # noqa: E501
        :rtype: str
        """
        return self._pattern_path

    @pattern_path.setter
    def pattern_path(self, pattern_path):
        """Sets the pattern_path of this DawConfig.


        :param pattern_path: The pattern_path of this DawConfig.  # noqa: E501
        :type: str
        """

        self._pattern_path = pattern_path

    @property
    def plugin_path(self):
        """Gets the plugin_path of this DawConfig.  # noqa: E501


        :return: The plugin_path of this DawConfig.  # noqa: E501
        :rtype: str
        """
        return self._plugin_path

    @plugin_path.setter
    def plugin_path(self, plugin_path):
        """Sets the plugin_path of this DawConfig.


        :param plugin_path: The plugin_path of this DawConfig.  # noqa: E501
        :type: str
        """

        self._plugin_path = plugin_path

    @property
    def preset_path(self):
        """Gets the preset_path of this DawConfig.  # noqa: E501


        :return: The preset_path of this DawConfig.  # noqa: E501
        :rtype: str
        """
        return self._preset_path

    @preset_path.setter
    def preset_path(self, preset_path):
        """Sets the preset_path of this DawConfig.


        :param preset_path: The preset_path of this DawConfig.  # noqa: E501
        :type: str
        """

        self._preset_path = preset_path

    @property
    def projects_path(self):
        """Gets the projects_path of this DawConfig.  # noqa: E501


        :return: The projects_path of this DawConfig.  # noqa: E501
        :rtype: str
        """
        return self._projects_path

    @projects_path.setter
    def projects_path(self, projects_path):
        """Sets the projects_path of this DawConfig.


        :param projects_path: The projects_path of this DawConfig.  # noqa: E501
        :type: str
        """

        self._projects_path = projects_path

    @property
    def rendered_path(self):
        """Gets the rendered_path of this DawConfig.  # noqa: E501


        :return: The rendered_path of this DawConfig.  # noqa: E501
        :rtype: str
        """
        return self._rendered_path

    @rendered_path.setter
    def rendered_path(self, rendered_path):
        """Sets the rendered_path of this DawConfig.


        :param rendered_path: The rendered_path of this DawConfig.  # noqa: E501
        :type: str
        """

        self._rendered_path = rendered_path

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(DawConfig, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DawConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
