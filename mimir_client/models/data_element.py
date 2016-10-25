# coding: utf-8

"""
    Mimir DataHub API

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.0.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class DataElement(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, dataset=None, owner=None, release=None, mime_type=None, description=None, type=None, schema=None, state=None, storage=None, content=None, block_id=None, key_field=None, display_info=None, csv_info=None):
        """
        DataElement - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'dataset': 'str',
            'owner': 'str',
            'release': 'str',
            'mime_type': 'str',
            'description': 'str',
            'type': 'str',
            'schema': 'str',
            'state': 'str',
            'storage': 'str',
            'content': 'str',
            'block_id': 'int',
            'key_field': 'str',
            'display_info': 'DataElementDisplayInfo',
            'csv_info': 'DataElementCsvInfo'
        }

        self.attribute_map = {
            'id': 'id',
            'dataset': 'dataset',
            'owner': 'owner',
            'release': 'release',
            'mime_type': 'mimeType',
            'description': 'description',
            'type': 'type',
            'schema': 'schema',
            'state': 'state',
            'storage': 'storage',
            'content': 'content',
            'block_id': 'blockId',
            'key_field': 'keyField',
            'display_info': 'displayInfo',
            'csv_info': 'csvInfo'
        }

        self._id = id
        self._dataset = dataset
        self._owner = owner
        self._release = release
        self._mime_type = mime_type
        self._description = description
        self._type = type
        self._schema = schema
        self._state = state
        self._storage = storage
        self._content = content
        self._block_id = block_id
        self._key_field = key_field
        self._display_info = display_info
        self._csv_info = csv_info

    @property
    def id(self):
        """
        Gets the id of this DataElement.
        The id of this data element

        :return: The id of this DataElement.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DataElement.
        The id of this data element

        :param id: The id of this DataElement.
        :type: str
        """

        self._id = id

    @property
    def dataset(self):
        """
        Gets the dataset of this DataElement.
        The data set this element relates to

        :return: The dataset of this DataElement.
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """
        Sets the dataset of this DataElement.
        The data set this element relates to

        :param dataset: The dataset of this DataElement.
        :type: str
        """

        self._dataset = dataset

    @property
    def owner(self):
        """
        Gets the owner of this DataElement.
        The user this element relates to

        :return: The owner of this DataElement.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this DataElement.
        The user this element relates to

        :param owner: The owner of this DataElement.
        :type: str
        """

        self._owner = owner

    @property
    def release(self):
        """
        Gets the release of this DataElement.
        The release this element relates to

        :return: The release of this DataElement.
        :rtype: str
        """
        return self._release

    @release.setter
    def release(self, release):
        """
        Sets the release of this DataElement.
        The release this element relates to

        :param release: The release of this DataElement.
        :type: str
        """

        self._release = release

    @property
    def mime_type(self):
        """
        Gets the mime_type of this DataElement.
        The mime type of the data element

        :return: The mime_type of this DataElement.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """
        Sets the mime_type of this DataElement.
        The mime type of the data element

        :param mime_type: The mime_type of this DataElement.
        :type: str
        """

        self._mime_type = mime_type

    @property
    def description(self):
        """
        Gets the description of this DataElement.
        Some information about this element

        :return: The description of this DataElement.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DataElement.
        Some information about this element

        :param description: The description of this DataElement.
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """
        Gets the type of this DataElement.
        The underlying data type of this element

        :return: The type of this DataElement.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DataElement.
        The underlying data type of this element

        :param type: The type of this DataElement.
        :type: str
        """

        self._type = type

    @property
    def schema(self):
        """
        Gets the schema of this DataElement.
        The underlying format of the data

        :return: The schema of this DataElement.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this DataElement.
        The underlying format of the data

        :param schema: The schema of this DataElement.
        :type: str
        """

        self._schema = schema

    @property
    def state(self):
        """
        Gets the state of this DataElement.
        The state of this element (is it published?)

        :return: The state of this DataElement.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this DataElement.
        The state of this element (is it published?)

        :param state: The state of this DataElement.
        :type: str
        """

        self._state = state

    @property
    def storage(self):
        """
        Gets the storage of this DataElement.
        Where blocks are stored for this element

        :return: The storage of this DataElement.
        :rtype: str
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """
        Sets the storage of this DataElement.
        Where blocks are stored for this element

        :param storage: The storage of this DataElement.
        :type: str
        """

        self._storage = storage

    @property
    def content(self):
        """
        Gets the content of this DataElement.
        If the type is text, this is the text

        :return: The content of this DataElement.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this DataElement.
        If the type is text, this is the text

        :param content: The content of this DataElement.
        :type: str
        """

        self._content = content

    @property
    def block_id(self):
        """
        Gets the block_id of this DataElement.
        If the type is csv, this is the next block when added

        :return: The block_id of this DataElement.
        :rtype: int
        """
        return self._block_id

    @block_id.setter
    def block_id(self, block_id):
        """
        Sets the block_id of this DataElement.
        If the type is csv, this is the next block when added

        :param block_id: The block_id of this DataElement.
        :type: int
        """

        self._block_id = block_id

    @property
    def key_field(self):
        """
        Gets the key_field of this DataElement.
        If the type is keyed, this is the key field that represents the unique key

        :return: The key_field of this DataElement.
        :rtype: str
        """
        return self._key_field

    @key_field.setter
    def key_field(self, key_field):
        """
        Sets the key_field of this DataElement.
        If the type is keyed, this is the key field that represents the unique key

        :param key_field: The key_field of this DataElement.
        :type: str
        """

        self._key_field = key_field

    @property
    def display_info(self):
        """
        Gets the display_info of this DataElement.


        :return: The display_info of this DataElement.
        :rtype: DataElementDisplayInfo
        """
        return self._display_info

    @display_info.setter
    def display_info(self, display_info):
        """
        Sets the display_info of this DataElement.


        :param display_info: The display_info of this DataElement.
        :type: DataElementDisplayInfo
        """

        self._display_info = display_info

    @property
    def csv_info(self):
        """
        Gets the csv_info of this DataElement.


        :return: The csv_info of this DataElement.
        :rtype: DataElementCsvInfo
        """
        return self._csv_info

    @csv_info.setter
    def csv_info(self, csv_info):
        """
        Sets the csv_info of this DataElement.


        :param csv_info: The csv_info of this DataElement.
        :type: DataElementCsvInfo
        """

        self._csv_info = csv_info

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other