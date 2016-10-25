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

from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """ UserApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.user_api.UserApi()

    def tearDown(self):
        pass

    def test_delete_user(self):
        """
        Test case for delete_user

        
        """
        pass

    def test_get_user(self):
        """
        Test case for get_user

        
        """
        pass

    def test_get_user_by_email(self):
        """
        Test case for get_user_by_email

        
        """
        pass

    def test_get_user_by_tag(self):
        """
        Test case for get_user_by_tag

        
        """
        pass

    def test_get_user_by_token(self):
        """
        Test case for get_user_by_token

        
        """
        pass

    def test_put_user(self):
        """
        Test case for put_user

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
