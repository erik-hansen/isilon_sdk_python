# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class ClusterTimeError(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ClusterTimeError - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'code': 'str',
            'lnn': 'int',
            'message': 'str',
            'status': 'int'
        }

        self.attribute_map = {
            'code': 'code',
            'lnn': 'lnn',
            'message': 'message',
            'status': 'status'
        }

        self._code = None
        self._lnn = None
        self._message = None
        self._status = None

    @property
    def code(self):
        """
        Gets the code of this ClusterTimeError.
        The general meaning of the status code.

        :return: The code of this ClusterTimeError.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ClusterTimeError.
        The general meaning of the status code.

        :param code: The code of this ClusterTimeError.
        :type: str
        """
        
        self._code = code

    @property
    def lnn(self):
        """
        Gets the lnn of this ClusterTimeError.
        Logical node number of the node reporting this error.

        :return: The lnn of this ClusterTimeError.
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """
        Sets the lnn of this ClusterTimeError.
        Logical node number of the node reporting this error.

        :param lnn: The lnn of this ClusterTimeError.
        :type: int
        """
        
        if not lnn:
            raise ValueError("Invalid value for `lnn`, must not be `None`")
        if lnn > 4.294967295E9: 
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `4.294967295E9`")
        if lnn < 0.0: 
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `0.0`")

        self._lnn = lnn

    @property
    def message(self):
        """
        Gets the message of this ClusterTimeError.
        More detailed description of the error.

        :return: The message of this ClusterTimeError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ClusterTimeError.
        More detailed description of the error.

        :param message: The message of this ClusterTimeError.
        :type: str
        """
        
        self._message = message

    @property
    def status(self):
        """
        Gets the status of this ClusterTimeError.
        HTTP Status code returned by this node.

        :return: The status of this ClusterTimeError.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ClusterTimeError.
        HTTP Status code returned by this node.

        :param status: The status of this ClusterTimeError.
        :type: int
        """
        
        if not status:
            raise ValueError("Invalid value for `status`, must not be `None`")
        if status > 4.294967295E9: 
            raise ValueError("Invalid value for `status`, must be a value less than or equal to `4.294967295E9`")
        if status < 0.0: 
            raise ValueError("Invalid value for `status`, must be a value greater than or equal to `0.0`")

        self._status = status

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
