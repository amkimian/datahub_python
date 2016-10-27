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


class User(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, email=None, gravatar=None, api_key=None, password=None, password_reset_token=None, password_reset_expires=None, twitter=None, google=None, github=None, linkedin=None, tokens=None, profile=None):
        """
        User - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'email': 'str',
            'gravatar': 'str',
            'api_key': 'str',
            'password': 'str',
            'password_reset_token': 'str',
            'password_reset_expires': 'date',
            'twitter': 'str',
            'google': 'str',
            'github': 'str',
            'linkedin': 'str',
            'tokens': 'list[UserTokens]',
            'profile': 'UserProfile'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'email': 'email',
            'gravatar': 'gravatar',
            'api_key': 'apiKey',
            'password': 'password',
            'password_reset_token': 'passwordResetToken',
            'password_reset_expires': 'passwordResetExpires',
            'twitter': 'twitter',
            'google': 'google',
            'github': 'github',
            'linkedin': 'linkedin',
            'tokens': 'tokens',
            'profile': 'profile'
        }

        self._id = id
        self._name = name
        self._email = email
        self._gravatar = gravatar
        self._api_key = api_key
        self._password = password
        self._password_reset_token = password_reset_token
        self._password_reset_expires = password_reset_expires
        self._twitter = twitter
        self._google = google
        self._github = github
        self._linkedin = linkedin
        self._tokens = tokens
        self._profile = profile

    @property
    def id(self):
        """
        Gets the id of this User.


        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.


        :param id: The id of this User.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this User.


        :return: The name of this User.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this User.


        :param name: The name of this User.
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """
        Gets the email of this User.


        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this User.


        :param email: The email of this User.
        :type: str
        """

        self._email = email

    @property
    def gravatar(self):
        """
        Gets the gravatar of this User.


        :return: The gravatar of this User.
        :rtype: str
        """
        return self._gravatar

    @gravatar.setter
    def gravatar(self, gravatar):
        """
        Sets the gravatar of this User.


        :param gravatar: The gravatar of this User.
        :type: str
        """

        self._gravatar = gravatar

    @property
    def api_key(self):
        """
        Gets the api_key of this User.
        The api key that can be used to impersonate this user

        :return: The api_key of this User.
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """
        Sets the api_key of this User.
        The api key that can be used to impersonate this user

        :param api_key: The api_key of this User.
        :type: str
        """

        self._api_key = api_key

    @property
    def password(self):
        """
        Gets the password of this User.


        :return: The password of this User.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this User.


        :param password: The password of this User.
        :type: str
        """

        self._password = password

    @property
    def password_reset_token(self):
        """
        Gets the password_reset_token of this User.


        :return: The password_reset_token of this User.
        :rtype: str
        """
        return self._password_reset_token

    @password_reset_token.setter
    def password_reset_token(self, password_reset_token):
        """
        Sets the password_reset_token of this User.


        :param password_reset_token: The password_reset_token of this User.
        :type: str
        """

        self._password_reset_token = password_reset_token

    @property
    def password_reset_expires(self):
        """
        Gets the password_reset_expires of this User.


        :return: The password_reset_expires of this User.
        :rtype: date
        """
        return self._password_reset_expires

    @password_reset_expires.setter
    def password_reset_expires(self, password_reset_expires):
        """
        Sets the password_reset_expires of this User.


        :param password_reset_expires: The password_reset_expires of this User.
        :type: date
        """

        self._password_reset_expires = password_reset_expires

    @property
    def twitter(self):
        """
        Gets the twitter of this User.


        :return: The twitter of this User.
        :rtype: str
        """
        return self._twitter

    @twitter.setter
    def twitter(self, twitter):
        """
        Sets the twitter of this User.


        :param twitter: The twitter of this User.
        :type: str
        """

        self._twitter = twitter

    @property
    def google(self):
        """
        Gets the google of this User.


        :return: The google of this User.
        :rtype: str
        """
        return self._google

    @google.setter
    def google(self, google):
        """
        Sets the google of this User.


        :param google: The google of this User.
        :type: str
        """

        self._google = google

    @property
    def github(self):
        """
        Gets the github of this User.


        :return: The github of this User.
        :rtype: str
        """
        return self._github

    @github.setter
    def github(self, github):
        """
        Sets the github of this User.


        :param github: The github of this User.
        :type: str
        """

        self._github = github

    @property
    def linkedin(self):
        """
        Gets the linkedin of this User.


        :return: The linkedin of this User.
        :rtype: str
        """
        return self._linkedin

    @linkedin.setter
    def linkedin(self, linkedin):
        """
        Sets the linkedin of this User.


        :param linkedin: The linkedin of this User.
        :type: str
        """

        self._linkedin = linkedin

    @property
    def tokens(self):
        """
        Gets the tokens of this User.


        :return: The tokens of this User.
        :rtype: list[UserTokens]
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        """
        Sets the tokens of this User.


        :param tokens: The tokens of this User.
        :type: list[UserTokens]
        """

        self._tokens = tokens

    @property
    def profile(self):
        """
        Gets the profile of this User.


        :return: The profile of this User.
        :rtype: UserProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """
        Sets the profile of this User.


        :param profile: The profile of this User.
        :type: UserProfile
        """

        self._profile = profile

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
