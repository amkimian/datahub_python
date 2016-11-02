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
from datahub_client.apis.scheme_api import SchemeApi


class TestSchemeApi(unittest.TestCase):
    """ SchemeApi unit test stubs """

    def setUp(self):
        self.api = datahub_client.apis.scheme_api.SchemeApi()

    def tearDown(self):
        pass

    def test_create_scheme(self):
        """
        Test case for create_scheme

        
        """
        pass

    def test_delete_scheme(self):
        """
        Test case for delete_scheme

        Remove a scheme
        """
        pass

    def test_get_scheme(self):
        """
        Test case for get_scheme

        
        """
        pass

    def test_get_schemes(self):
        """
        Test case for get_schemes

        
        """
        pass

    def test_update_scheme(self):
        """
        Test case for update_scheme

        Update an existing scheme.
        """
        pass


if __name__ == '__main__':
    unittest.main()
