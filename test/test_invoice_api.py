# coding: utf-8

"""
    DataHub API

    DataHub API

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

from __future__ import absolute_import

import os
import sys
import unittest

import datahub_client
from datahub_client.rest import ApiException
from datahub_client.apis.invoice_api import InvoiceApi


class TestInvoiceApi(unittest.TestCase):
    """ InvoiceApi unit test stubs """

    def setUp(self):
        self.api = datahub_client.apis.invoice_api.InvoiceApi()

    def tearDown(self):
        pass

    def test_add_subscription_to_invoice(self):
        """
        Test case for add_subscription_to_invoice

        
        """
        pass

    def test_get_cart(self):
        """
        Test case for get_cart

        
        """
        pass

    def test_get_invoices(self):
        """
        Test case for get_invoices

        
        """
        pass

    def test_process_cart(self):
        """
        Test case for process_cart

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
