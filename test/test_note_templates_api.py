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
from swagger_client.api.note_templates_api import NoteTemplatesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestNoteTemplatesApi(unittest.TestCase):
    """NoteTemplatesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.note_templates_api.NoteTemplatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_createnote_templates(self):
        """Test case for createnote_templates

        Create a new note-templates  # noqa: E501
        """
        pass

    def test_deletenote_templates(self):
        """Test case for deletenote_templates

        Delete a specific note-template instance.  # noqa: E501
        """
        pass

    def test_getnote_templates(self):
        """Test case for getnote_templates

        Return a specific note-template instance.  # noqa: E501
        """
        pass

    def test_getnote_templatess(self):
        """Test case for getnote_templatess

        List multiple note-templates resources.  # noqa: E501
        """
        pass

    def test_updatenote_templates(self):
        """Test case for updatenote_templates

        Update a specific note-template instance.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()