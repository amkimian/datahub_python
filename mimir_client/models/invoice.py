# coding: utf-8

"""
    Mimir DataHub API

    Mimir DataHub API

    OpenAPI spec version: 0.0.10
    
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


class Invoice(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, user=None, number=None, oneoff=None, invoice_date=None, year=None, month=None, status=None, entries=None, tax=None, total=None):
        """
        Invoice - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user': 'str',
            'number': 'str',
            'oneoff': 'bool',
            'invoice_date': 'date',
            'year': 'int',
            'month': 'int',
            'status': 'str',
            'entries': 'list[InvoiceEntry]',
            'tax': 'int',
            'total': 'int'
        }

        self.attribute_map = {
            'user': 'user',
            'number': 'number',
            'oneoff': 'oneoff',
            'invoice_date': 'invoiceDate',
            'year': 'year',
            'month': 'month',
            'status': 'status',
            'entries': 'entries',
            'tax': 'tax',
            'total': 'total'
        }

        self._user = user
        self._number = number
        self._oneoff = oneoff
        self._invoice_date = invoice_date
        self._year = year
        self._month = month
        self._status = status
        self._entries = entries
        self._tax = tax
        self._total = total

    @property
    def user(self):
        """
        Gets the user of this Invoice.
        The user this invoice relates to

        :return: The user of this Invoice.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this Invoice.
        The user this invoice relates to

        :param user: The user of this Invoice.
        :type: str
        """

        self._user = user

    @property
    def number(self):
        """
        Gets the number of this Invoice.
        The invoice id

        :return: The number of this Invoice.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this Invoice.
        The invoice id

        :param number: The number of this Invoice.
        :type: str
        """

        self._number = number

    @property
    def oneoff(self):
        """
        Gets the oneoff of this Invoice.
        Whether this is an out of cycle (not monthly) invoice

        :return: The oneoff of this Invoice.
        :rtype: bool
        """
        return self._oneoff

    @oneoff.setter
    def oneoff(self, oneoff):
        """
        Sets the oneoff of this Invoice.
        Whether this is an out of cycle (not monthly) invoice

        :param oneoff: The oneoff of this Invoice.
        :type: bool
        """

        self._oneoff = oneoff

    @property
    def invoice_date(self):
        """
        Gets the invoice_date of this Invoice.
        The date of this invoice

        :return: The invoice_date of this Invoice.
        :rtype: date
        """
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, invoice_date):
        """
        Sets the invoice_date of this Invoice.
        The date of this invoice

        :param invoice_date: The invoice_date of this Invoice.
        :type: date
        """

        self._invoice_date = invoice_date

    @property
    def year(self):
        """
        Gets the year of this Invoice.


        :return: The year of this Invoice.
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """
        Sets the year of this Invoice.


        :param year: The year of this Invoice.
        :type: int
        """

        self._year = year

    @property
    def month(self):
        """
        Gets the month of this Invoice.
        The month this invoice applies to (the cycle)

        :return: The month of this Invoice.
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """
        Sets the month of this Invoice.
        The month this invoice applies to (the cycle)

        :param month: The month of this Invoice.
        :type: int
        """

        self._month = month

    @property
    def status(self):
        """
        Gets the status of this Invoice.
        The status of this invoice (open, paid, cancelled)

        :return: The status of this Invoice.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Invoice.
        The status of this invoice (open, paid, cancelled)

        :param status: The status of this Invoice.
        :type: str
        """

        self._status = status

    @property
    def entries(self):
        """
        Gets the entries of this Invoice.
        The entries of this invoice

        :return: The entries of this Invoice.
        :rtype: list[InvoiceEntry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """
        Sets the entries of this Invoice.
        The entries of this invoice

        :param entries: The entries of this Invoice.
        :type: list[InvoiceEntry]
        """

        self._entries = entries

    @property
    def tax(self):
        """
        Gets the tax of this Invoice.
        Any tax due on this invoice in cents

        :return: The tax of this Invoice.
        :rtype: int
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """
        Sets the tax of this Invoice.
        Any tax due on this invoice in cents

        :param tax: The tax of this Invoice.
        :type: int
        """

        self._tax = tax

    @property
    def total(self):
        """
        Gets the total of this Invoice.
        The total amount of the invoice (in cents in case the tax)

        :return: The total of this Invoice.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this Invoice.
        The total amount of the invoice (in cents in case the tax)

        :param total: The total of this Invoice.
        :type: int
        """

        self._total = total

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
