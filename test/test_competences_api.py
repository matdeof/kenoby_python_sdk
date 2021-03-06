# coding: utf-8

"""
    Kenoby

    Issues or Questions? <a href=\"mailto:devs@kenoby.com\" target=\"_blank\">Send us an e-mail</a>.<br>                      For better experience <a href=\"http://api.kenoby.com/swagger.json\" target=\"_blank\">Download our swagger.json</a>                      and use it on <a href=\"https://www.getpostman.com/\" target=\"_blank\">Postman</a>  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.competences_api import CompetencesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCompetencesApi(unittest.TestCase):
    """CompetencesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.competences_api.CompetencesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_competences(self):
        """Test case for create_competences

        Create a new competences  # noqa: E501
        """
        pass

    def test_deletecompetences(self):
        """Test case for deletecompetences

        Delete a specific competences  # noqa: E501
        """
        pass

    def test_getcompetences(self):
        """Test case for getcompetences

        Return a specific competence instance.  # noqa: E501
        """
        pass

    def test_getcompetencess(self):
        """Test case for getcompetencess

        List multiple competences resources.  # noqa: E501
        """
        pass

    def test_updatecompetences(self):
        """Test case for updatecompetences

        Update a specific competence instance.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
