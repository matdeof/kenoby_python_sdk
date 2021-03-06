# coding: utf-8

"""
    Kenoby

    Issues or Questions? <a href=\"mailto:devs@kenoby.com\" target=\"_blank\">Send us an e-mail</a>.<br>                      For better experience <a href=\"http://api.kenoby.com/swagger.json\" target=\"_blank\">Download our swagger.json</a>                      and use it on <a href=\"https://www.getpostman.com/\" target=\"_blank\">Postman</a>  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ApplicantRankdoneTestFinishApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def rankdonescreeningtestfinish(self, applicant_id, **kwargs):  # noqa: E501
        """Rankdone API sends a request to Kenoby informing a candidate that finished a test on their platform.  # noqa: E501

        Rankdone API sends a request to Kenoby informing a candidate that finished a test on their platform.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.rankdonescreeningtestfinish(applicant_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str applicant_id: The ID of the application that will be retrieved. (required)
        :return: ApplicantsscreeningTests
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.rankdonescreeningtestfinish_with_http_info(applicant_id, **kwargs)  # noqa: E501
        else:
            (data) = self.rankdonescreeningtestfinish_with_http_info(applicant_id, **kwargs)  # noqa: E501
            return data

    def rankdonescreeningtestfinish_with_http_info(self, applicant_id, **kwargs):  # noqa: E501
        """Rankdone API sends a request to Kenoby informing a candidate that finished a test on their platform.  # noqa: E501

        Rankdone API sends a request to Kenoby informing a candidate that finished a test on their platform.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.rankdonescreeningtestfinish_with_http_info(applicant_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str applicant_id: The ID of the application that will be retrieved. (required)
        :return: ApplicantsscreeningTests
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['applicant_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rankdonescreeningtestfinish" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'applicant_id' is set
        if ('applicant_id' not in params or
                params['applicant_id'] is None):
            raise ValueError("Missing the required parameter `applicant_id` when calling `rankdonescreeningtestfinish`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'applicant_id' in params:
            path_params['applicantId'] = params['applicant_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/screening-tests/rankdone/finish', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicantsscreeningTests',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
