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
from swagger_client.api.screening_groups_api import ScreeningGroupsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestScreeningGroupsApi(unittest.TestCase):
    """ScreeningGroupsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.screening_groups_api.ScreeningGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_screening_groups(self):
        """Test case for create_screening_groups

        Create a new screeningGroups  # noqa: E501
        """
        pass

    def test_disable_screening_group(self):
        """Test case for disable_screening_group

        Disable a specific screeningGroup  # noqa: E501
        """
        pass

    def test_getscreening_group(self):
        """Test case for getscreening_group

        Return a specific screeningGroup instance.  # noqa: E501
        """
        pass

    def test_getscreening_groups(self):
        """Test case for getscreening_groups

        List multiple screeningGroups resources.  # noqa: E501
        """
        pass

    def test_order_screening_groups(self):
        """Test case for order_screening_groups

        Order screeningGroups  # noqa: E501
        """
        pass

    def test_updatescreening_groups(self):
        """Test case for updatescreening_groups

        Update a specific screeningGroup instance.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
