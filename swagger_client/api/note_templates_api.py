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


class NoteTemplatesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def createnote_templates(self, authorization, x_tenant, x_version, body, **kwargs):  # noqa: E501
        """Create a new note-templates  # noqa: E501

        Create a new note-templates  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.createnote_templates(authorization, x_tenant, x_version, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: Basic Authentication. (required)
        :param str x_tenant: The tenant id. (required)
        :param str x_version: The API version. (required)
        :param NoteTemplates body: Data used to create a new note-templates (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.createnote_templates_with_http_info(authorization, x_tenant, x_version, body, **kwargs)  # noqa: E501
        else:
            (data) = self.createnote_templates_with_http_info(authorization, x_tenant, x_version, body, **kwargs)  # noqa: E501
            return data

    def createnote_templates_with_http_info(self, authorization, x_tenant, x_version, body, **kwargs):  # noqa: E501
        """Create a new note-templates  # noqa: E501

        Create a new note-templates  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.createnote_templates_with_http_info(authorization, x_tenant, x_version, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: Basic Authentication. (required)
        :param str x_tenant: The tenant id. (required)
        :param str x_version: The API version. (required)
        :param NoteTemplates body: Data used to create a new note-templates (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'x_tenant', 'x_version', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method createnote_templates" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `createnote_templates`")  # noqa: E501
        # verify the required parameter 'x_tenant' is set
        if ('x_tenant' not in params or
                params['x_tenant'] is None):
            raise ValueError("Missing the required parameter `x_tenant` when calling `createnote_templates`")  # noqa: E501
        # verify the required parameter 'x_version' is set
        if ('x_version' not in params or
                params['x_version'] is None):
            raise ValueError("Missing the required parameter `x_version` when calling `createnote_templates`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `createnote_templates`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_tenant' in params:
            header_params['x-tenant'] = params['x_tenant']  # noqa: E501
        if 'x_version' in params:
            header_params['x-version'] = params['x_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/note-templates', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def deletenote_templates(self, authorization, x_tenant, x_version, note_templates_id, body, **kwargs):  # noqa: E501
        """Delete a specific note-template instance.  # noqa: E501

        Delete a specific note-template instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.deletenote_templates(authorization, x_tenant, x_version, note_templates_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: Basic Authentication. (required)
        :param str x_tenant: The tenant id. (required)
        :param str x_version: The API version. (required)
        :param str note_templates_id: The ID of the note-templates that will be deleted. (required)
        :param NoteTemplates body: Data used to delete note-templates (required)
        :return: NoteTemplates
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.deletenote_templates_with_http_info(authorization, x_tenant, x_version, note_templates_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.deletenote_templates_with_http_info(authorization, x_tenant, x_version, note_templates_id, body, **kwargs)  # noqa: E501
            return data

    def deletenote_templates_with_http_info(self, authorization, x_tenant, x_version, note_templates_id, body, **kwargs):  # noqa: E501
        """Delete a specific note-template instance.  # noqa: E501

        Delete a specific note-template instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.deletenote_templates_with_http_info(authorization, x_tenant, x_version, note_templates_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: Basic Authentication. (required)
        :param str x_tenant: The tenant id. (required)
        :param str x_version: The API version. (required)
        :param str note_templates_id: The ID of the note-templates that will be deleted. (required)
        :param NoteTemplates body: Data used to delete note-templates (required)
        :return: NoteTemplates
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'x_tenant', 'x_version', 'note_templates_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deletenote_templates" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `deletenote_templates`")  # noqa: E501
        # verify the required parameter 'x_tenant' is set
        if ('x_tenant' not in params or
                params['x_tenant'] is None):
            raise ValueError("Missing the required parameter `x_tenant` when calling `deletenote_templates`")  # noqa: E501
        # verify the required parameter 'x_version' is set
        if ('x_version' not in params or
                params['x_version'] is None):
            raise ValueError("Missing the required parameter `x_version` when calling `deletenote_templates`")  # noqa: E501
        # verify the required parameter 'note_templates_id' is set
        if ('note_templates_id' not in params or
                params['note_templates_id'] is None):
            raise ValueError("Missing the required parameter `note_templates_id` when calling `deletenote_templates`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `deletenote_templates`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'note_templates_id' in params:
            path_params['note-templatesId'] = params['note_templates_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_tenant' in params:
            header_params['x-tenant'] = params['x_tenant']  # noqa: E501
        if 'x_version' in params:
            header_params['x-version'] = params['x_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/note-templates/{note-templatesId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NoteTemplates',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getnote_templates(self, authorization, x_tenant, x_version, note_templates_id, **kwargs):  # noqa: E501
        """Return a specific note-template instance.  # noqa: E501

        Return a specific note-template instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.getnote_templates(authorization, x_tenant, x_version, note_templates_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: Basic Authentication. (required)
        :param str x_tenant: The tenant id. (required)
        :param str x_version: The API version. (required)
        :param str note_templates_id: The ID of the note-templates that will be retrieved. (required)
        :return: NoteTemplates
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.getnote_templates_with_http_info(authorization, x_tenant, x_version, note_templates_id, **kwargs)  # noqa: E501
        else:
            (data) = self.getnote_templates_with_http_info(authorization, x_tenant, x_version, note_templates_id, **kwargs)  # noqa: E501
            return data

    def getnote_templates_with_http_info(self, authorization, x_tenant, x_version, note_templates_id, **kwargs):  # noqa: E501
        """Return a specific note-template instance.  # noqa: E501

        Return a specific note-template instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.getnote_templates_with_http_info(authorization, x_tenant, x_version, note_templates_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: Basic Authentication. (required)
        :param str x_tenant: The tenant id. (required)
        :param str x_version: The API version. (required)
        :param str note_templates_id: The ID of the note-templates that will be retrieved. (required)
        :return: NoteTemplates
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'x_tenant', 'x_version', 'note_templates_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getnote_templates" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `getnote_templates`")  # noqa: E501
        # verify the required parameter 'x_tenant' is set
        if ('x_tenant' not in params or
                params['x_tenant'] is None):
            raise ValueError("Missing the required parameter `x_tenant` when calling `getnote_templates`")  # noqa: E501
        # verify the required parameter 'x_version' is set
        if ('x_version' not in params or
                params['x_version'] is None):
            raise ValueError("Missing the required parameter `x_version` when calling `getnote_templates`")  # noqa: E501
        # verify the required parameter 'note_templates_id' is set
        if ('note_templates_id' not in params or
                params['note_templates_id'] is None):
            raise ValueError("Missing the required parameter `note_templates_id` when calling `getnote_templates`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'note_templates_id' in params:
            path_params['note-templatesId'] = params['note_templates_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_tenant' in params:
            header_params['x-tenant'] = params['x_tenant']  # noqa: E501
        if 'x_version' in params:
            header_params['x-version'] = params['x_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/note-templates/{note-templatesId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NoteTemplates',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getnote_templatess(self, authorization, x_tenant, x_version, **kwargs):  # noqa: E501
        """List multiple note-templates resources.  # noqa: E501

        This operation allows you to list and search for note-templates resources provided query arguments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.getnote_templatess(authorization, x_tenant, x_version, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: Basic Authentication. (required)
        :param str x_tenant: The tenant id. (required)
        :param str x_version: The API version. (required)
        :param int page: The page of records. Used for pagination.
        :param int page_size: How many records to limit the output.
        :param str order_by: Which fields to sort the records on. You can use minus sign to have a reverse order. Ex.: orderBy=-name
        :param str select_0: Select which fields will be returned by the query.
        :param str select_1: Select which fields will be returned by the query. One select for each field
        :param str filter_by_name_like: Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value
        :param str filter_by_subject_like: Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value
        :param str filter_by_message_like: Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value
        :param str filter_by_created_at_from: Filter the results greatter than a given date
        :param str filter_by_created_at_to: Filter the results lower than a given date
        :param str filter_by_or_0_name_like: Filter the results associating more than one parameter. This is just a sample using 'or' sintax.
        :param str filter_by_or_1_subject_like: Filter the results associating more than one parameter. This is just a sample using 'or' sintax.
        :param str count_0_filter_by_name_like: Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]=Ricardo
        :param str count_1_filter_by_created_at_from: Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]=2015-01-01T02:00:00.000Z
        :return: NoteTemplatesList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.getnote_templatess_with_http_info(authorization, x_tenant, x_version, **kwargs)  # noqa: E501
        else:
            (data) = self.getnote_templatess_with_http_info(authorization, x_tenant, x_version, **kwargs)  # noqa: E501
            return data

    def getnote_templatess_with_http_info(self, authorization, x_tenant, x_version, **kwargs):  # noqa: E501
        """List multiple note-templates resources.  # noqa: E501

        This operation allows you to list and search for note-templates resources provided query arguments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.getnote_templatess_with_http_info(authorization, x_tenant, x_version, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: Basic Authentication. (required)
        :param str x_tenant: The tenant id. (required)
        :param str x_version: The API version. (required)
        :param int page: The page of records. Used for pagination.
        :param int page_size: How many records to limit the output.
        :param str order_by: Which fields to sort the records on. You can use minus sign to have a reverse order. Ex.: orderBy=-name
        :param str select_0: Select which fields will be returned by the query.
        :param str select_1: Select which fields will be returned by the query. One select for each field
        :param str filter_by_name_like: Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value
        :param str filter_by_subject_like: Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value
        :param str filter_by_message_like: Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value
        :param str filter_by_created_at_from: Filter the results greatter than a given date
        :param str filter_by_created_at_to: Filter the results lower than a given date
        :param str filter_by_or_0_name_like: Filter the results associating more than one parameter. This is just a sample using 'or' sintax.
        :param str filter_by_or_1_subject_like: Filter the results associating more than one parameter. This is just a sample using 'or' sintax.
        :param str count_0_filter_by_name_like: Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]=Ricardo
        :param str count_1_filter_by_created_at_from: Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]=2015-01-01T02:00:00.000Z
        :return: NoteTemplatesList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'x_tenant', 'x_version', 'page', 'page_size', 'order_by', 'select_0', 'select_1', 'filter_by_name_like', 'filter_by_subject_like', 'filter_by_message_like', 'filter_by_created_at_from', 'filter_by_created_at_to', 'filter_by_or_0_name_like', 'filter_by_or_1_subject_like', 'count_0_filter_by_name_like', 'count_1_filter_by_created_at_from']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getnote_templatess" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `getnote_templatess`")  # noqa: E501
        # verify the required parameter 'x_tenant' is set
        if ('x_tenant' not in params or
                params['x_tenant'] is None):
            raise ValueError("Missing the required parameter `x_tenant` when calling `getnote_templatess`")  # noqa: E501
        # verify the required parameter 'x_version' is set
        if ('x_version' not in params or
                params['x_version'] is None):
            raise ValueError("Missing the required parameter `x_version` when calling `getnote_templatess`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('orderBy', params['order_by']))  # noqa: E501
        if 'select_0' in params:
            query_params.append(('select[0]', params['select_0']))  # noqa: E501
        if 'select_1' in params:
            query_params.append(('select[1]', params['select_1']))  # noqa: E501
        if 'filter_by_name_like' in params:
            query_params.append(('filterBy[name][like]', params['filter_by_name_like']))  # noqa: E501
        if 'filter_by_subject_like' in params:
            query_params.append(('filterBy[subject][like]', params['filter_by_subject_like']))  # noqa: E501
        if 'filter_by_message_like' in params:
            query_params.append(('filterBy[message][like]', params['filter_by_message_like']))  # noqa: E501
        if 'filter_by_created_at_from' in params:
            query_params.append(('filterBy[createdAt][from]', params['filter_by_created_at_from']))  # noqa: E501
        if 'filter_by_created_at_to' in params:
            query_params.append(('filterBy[createdAt][to]', params['filter_by_created_at_to']))  # noqa: E501
        if 'filter_by_or_0_name_like' in params:
            query_params.append(('filterBy[or][0][name][like]', params['filter_by_or_0_name_like']))  # noqa: E501
        if 'filter_by_or_1_subject_like' in params:
            query_params.append(('filterBy[or][1][subject][like]', params['filter_by_or_1_subject_like']))  # noqa: E501
        if 'count_0_filter_by_name_like' in params:
            query_params.append(('count[0][filterBy][name][like]', params['count_0_filter_by_name_like']))  # noqa: E501
        if 'count_1_filter_by_created_at_from' in params:
            query_params.append(('count[1][filterBy][createdAt][from]', params['count_1_filter_by_created_at_from']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_tenant' in params:
            header_params['x-tenant'] = params['x_tenant']  # noqa: E501
        if 'x_version' in params:
            header_params['x-version'] = params['x_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/note-templates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NoteTemplatesList',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def updatenote_templates(self, authorization, x_tenant, x_version, note_templates_id, body, **kwargs):  # noqa: E501
        """Update a specific note-template instance.  # noqa: E501

        Update a specific note-template instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.updatenote_templates(authorization, x_tenant, x_version, note_templates_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: Basic Authentication. (required)
        :param str x_tenant: The tenant id. (required)
        :param str x_version: The API version. (required)
        :param str note_templates_id: The ID of the note-templates that will be updated. (required)
        :param NoteTemplates body: Data used to update note-templates (required)
        :return: NoteTemplates
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.updatenote_templates_with_http_info(authorization, x_tenant, x_version, note_templates_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.updatenote_templates_with_http_info(authorization, x_tenant, x_version, note_templates_id, body, **kwargs)  # noqa: E501
            return data

    def updatenote_templates_with_http_info(self, authorization, x_tenant, x_version, note_templates_id, body, **kwargs):  # noqa: E501
        """Update a specific note-template instance.  # noqa: E501

        Update a specific note-template instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.updatenote_templates_with_http_info(authorization, x_tenant, x_version, note_templates_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: Basic Authentication. (required)
        :param str x_tenant: The tenant id. (required)
        :param str x_version: The API version. (required)
        :param str note_templates_id: The ID of the note-templates that will be updated. (required)
        :param NoteTemplates body: Data used to update note-templates (required)
        :return: NoteTemplates
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'x_tenant', 'x_version', 'note_templates_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method updatenote_templates" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `updatenote_templates`")  # noqa: E501
        # verify the required parameter 'x_tenant' is set
        if ('x_tenant' not in params or
                params['x_tenant'] is None):
            raise ValueError("Missing the required parameter `x_tenant` when calling `updatenote_templates`")  # noqa: E501
        # verify the required parameter 'x_version' is set
        if ('x_version' not in params or
                params['x_version'] is None):
            raise ValueError("Missing the required parameter `x_version` when calling `updatenote_templates`")  # noqa: E501
        # verify the required parameter 'note_templates_id' is set
        if ('note_templates_id' not in params or
                params['note_templates_id'] is None):
            raise ValueError("Missing the required parameter `note_templates_id` when calling `updatenote_templates`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `updatenote_templates`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'note_templates_id' in params:
            path_params['note-templatesId'] = params['note_templates_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_tenant' in params:
            header_params['x-tenant'] = params['x_tenant']  # noqa: E501
        if 'x_version' in params:
            header_params['x-version'] = params['x_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/note-templates/{note-templatesId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NoteTemplates',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
