# coding: utf-8

"""
    LAAWS Metadata Service API

    API of Metadata Service for LAAWS  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@lockss.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ItemMetadata(object):
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
        'scalar_map': 'dict(str, str)',
        'list_map': 'dict(str, list[str])',
        'map_map': 'dict(str, dict(str, str))'
    }

    attribute_map = {
        'scalar_map': 'scalarMap',
        'list_map': 'listMap',
        'map_map': 'mapMap'
    }

    def __init__(self, scalar_map=None, list_map=None, map_map=None):  # noqa: E501
        """ItemMetadata - a model defined in Swagger"""  # noqa: E501

        self._scalar_map = None
        self._list_map = None
        self._map_map = None
        self.discriminator = None

        if scalar_map is not None:
            self.scalar_map = scalar_map
        if list_map is not None:
            self.list_map = list_map
        if map_map is not None:
            self.map_map = map_map

    @property
    def scalar_map(self):
        """Gets the scalar_map of this ItemMetadata.  # noqa: E501

        The map of scalar metadata elements for this item  # noqa: E501

        :return: The scalar_map of this ItemMetadata.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._scalar_map

    @scalar_map.setter
    def scalar_map(self, scalar_map):
        """Sets the scalar_map of this ItemMetadata.

        The map of scalar metadata elements for this item  # noqa: E501

        :param scalar_map: The scalar_map of this ItemMetadata.  # noqa: E501
        :type: dict(str, str)
        """

        self._scalar_map = scalar_map

    @property
    def list_map(self):
        """Gets the list_map of this ItemMetadata.  # noqa: E501

        The map of listed metadata elements for this item  # noqa: E501

        :return: The list_map of this ItemMetadata.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._list_map

    @list_map.setter
    def list_map(self, list_map):
        """Sets the list_map of this ItemMetadata.

        The map of listed metadata elements for this item  # noqa: E501

        :param list_map: The list_map of this ItemMetadata.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._list_map = list_map

    @property
    def map_map(self):
        """Gets the map_map of this ItemMetadata.  # noqa: E501

        The map of mapped metadata elements for this item  # noqa: E501

        :return: The map_map of this ItemMetadata.  # noqa: E501
        :rtype: dict(str, dict(str, str))
        """
        return self._map_map

    @map_map.setter
    def map_map(self, map_map):
        """Sets the map_map of this ItemMetadata.

        The map of mapped metadata elements for this item  # noqa: E501

        :param map_map: The map_map of this ItemMetadata.  # noqa: E501
        :type: dict(str, dict(str, str))
        """

        self._map_map = map_map

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
        if issubclass(ItemMetadata, dict):
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
        if not isinstance(other, ItemMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other