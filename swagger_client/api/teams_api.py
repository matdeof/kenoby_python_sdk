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


class TeamsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def createteams(self, authorization, x_tenant, x_version, body, **kwargs):  # noqa: E501
        """Create a new teams  # noqa: E501

        Create a new teams  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.createteams(authorization, x_tenant, x_version, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: Basic Authentication. (required)
        :param str x_tenant: The tenant id. (required)
        :param str x_version: The API version. (required)
        :param Teams body: Data used to create a new teams (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.createteams_with_http_info(authorization, x_tenant, x_version, body, **kwargs)  # noqa: E501
        else:
            (data) = self.createteams_with_http_info(authorization, x_tenant, x_version, body, **kwargs)  # noqa: E501
            return data

    def createteams_with_http_info(self, authorization, x_tenant, x_version, body, **kwargs):  # noqa: E501
        """Create a new teams  # noqa: E501

        Create a new teams  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.createteams_with_http_info(authorization, x_tenant, x_version, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: Basic Authentication. (required)
        :param str x_tenant: The tenant id. (required)
        :param str x_version: The API version. (required)
        :param Teams body: Data used to create a new teams (required)
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
                    " to method createteams" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `createteams`")  # noqa: E501
        # verify the required parameter 'x_tenant' is set
        if ('x_tenant' not in params or
                params['x_tenant'] is None):
            raise ValueError("Missing the required parameter `x_tenant` when calling `createteams`")  # noqa: E501
        # verify the required parameter 'x_version' is set
        if ('x_version' not in params or
                params['x_version'] is None):
            raise ValueError("Missing the required parameter `x_version` when calling `createteams`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `createteams`")  # noqa: E501

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
            '/teams', 'POST',
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

    def getteams(self, authorization, x_tenant, x_version, teams_id, **kwargs):  # noqa: E501
        """Return a specific team instance.  # noqa: E501

        Return a specific team instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.getteams(authorization, x_tenant, x_version, teams_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: Basic Authentication. (required)
        :param str x_tenant: The tenant id. (required)
        :param str x_version: The API version. (required)
        :param str teams_id: The ID of the teams that will be retrieved. (required)
        :return: Teams
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.getteams_with_http_info(authorization, x_tenant, x_version, teams_id, **kwargs)  # noqa: E501
        else:
            (data) = self.getteams_with_http_info(authorization, x_tenant, x_version, teams_id, **kwargs)  # noqa: E501
            return data

    def getteams_with_http_info(self, authorization, x_tenant, x_version, teams_id, **kwargs):  # noqa: E501
        """Return a specific team instance.  # noqa: E501

        Return a specific team instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.getteams_with_http_info(authorization, x_tenant, x_version, teams_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: Basic Authentication. (required)
        :param str x_tenant: The tenant id. (required)
        :param str x_version: The API version. (required)
        :param str teams_id: The ID of the teams that will be retrieved. (required)
        :return: Teams
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'x_tenant', 'x_version', 'teams_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getteams" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `getteams`")  # noqa: E501
        # verify the required parameter 'x_tenant' is set
        if ('x_tenant' not in params or
                params['x_tenant'] is None):
            raise ValueError("Missing the required parameter `x_tenant` when calling `getteams`")  # noqa: E501
        # verify the required parameter 'x_version' is set
        if ('x_version' not in params or
                params['x_version'] is None):
            raise ValueError("Missing the required parameter `x_version` when calling `getteams`")  # noqa: E501
        # verify the required parameter 'teams_id' is set
        if ('teams_id' not in params or
                params['teams_id'] is None):
            raise ValueError("Missing the required parameter `teams_id` when calling `getteams`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'teams_id' in params:
            path_params['teamsId'] = params['teams_id']  # noqa: E501

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
            '/teams/{teamsId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Teams',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getteamss(self, authorization, x_tenant, x_version, **kwargs):  # noqa: E501
        """List multiple teams resources.  # noqa: E501

        This operation allows you to list and search for teams resources provided query arguments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.getteamss(authorization, x_tenant, x_version, async=True)
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
        :param str filter_by_owner: Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value
        :param str filter_by_members: Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value
        :param str filter_by_created_at_from: Filter the results greatter than a given date
        :param str filter_by_created_at_to: Filter the results lower than a given date
        :param str filter_by_or_0_members: Filter the results associating more than one parameter. This is just a sample using 'or' sintax.
        :param str filter_by_or_1_members: Filter the results associating more than one parameter. This is just a sample using 'or' sintax.
        :param str count_0_filter_by_name_like: Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]=Ricardo
        :param str count_1_filter_by_created_at_from: Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]=2015-01-01T02:00:00.000Z
        :param str search_by: Make a text search on main fields. Name and e-mail have higher scores.
        :return: TeamsList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.getteamss_with_http_info(authorization, x_tenant, x_version, **kwargs)  # noqa: E501
        else:
            (data) = self.getteamss_with_http_info(authorization, x_tenant, x_version, **kwargs)  # noqa: E501
            return data

    def getteamss_with_http_info(self, authorization, x_tenant, x_version, **kwargs):  # noqa: E501
        """List multiple teams resources.  # noqa: E501

        This operation allows you to list and search for teams resources provided query arguments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.getteamss_with_http_info(authorization, x_tenant, x_version, async=True)
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
        :param str filter_by_owner: Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value
        :param str filter_by_members: Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value
        :param str filter_by_created_at_from: Filter the results greatter than a given date
        :param str filter_by_created_at_to: Filter the results lower than a given date
        :param str filter_by_or_0_members: Filter the results associating more than one parameter. This is just a sample using 'or' sintax.
        :param str filter_by_or_1_members: Filter the results associating more than one parameter. This is just a sample using 'or' sintax.
        :param str count_0_filter_by_name_like: Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]=Ricardo
        :param str count_1_filter_by_created_at_from: Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]=2015-01-01T02:00:00.000Z
        :param str search_by: Make a text search on main fields. Name and e-mail have higher scores.
        :return: TeamsList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'x_tenant', 'x_version', 'page', 'page_size', 'order_by', 'select_0', 'select_1', 'filter_by_name_like', 'filter_by_owner', 'filter_by_members', 'filter_by_created_at_from', 'filter_by_created_at_to', 'filter_by_or_0_members', 'filter_by_or_1_members', 'count_0_filter_by_name_like', 'count_1_filter_by_created_at_from', 'search_by']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getteamss" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `getteamss`")  # noqa: E501
        # verify the required parameter 'x_tenant' is set
        if ('x_tenant' not in params or
                params['x_tenant'] is None):
            raise ValueError("Missing the required parameter `x_tenant` when calling `getteamss`")  # noqa: E501
        # verify the required parameter 'x_version' is set
        if ('x_version' not in params or
                params['x_version'] is None):
            raise ValueError("Missing the required parameter `x_version` when calling `getteamss`")  # noqa: E501

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
        if 'filter_by_owner' in params:
            query_params.append(('filterBy[owner]', params['filter_by_owner']))  # noqa: E501
        if 'filter_by_members' in params:
            query_params.append(('filterBy[members]', params['filter_by_members']))  # noqa: E501
        if 'filter_by_created_at_from' in params:
            query_params.append(('filterBy[createdAt][from]', params['filter_by_created_at_from']))  # noqa: E501
        if 'filter_by_created_at_to' in params:
            query_params.append(('filterBy[createdAt][to]', params['filter_by_created_at_to']))  # noqa: E501
        if 'filter_by_or_0_members' in params:
            query_params.append(('filterBy[or][0][members]', params['filter_by_or_0_members']))  # noqa: E501
        if 'filter_by_or_1_members' in params:
            query_params.append(('filterBy[or][1][members]', params['filter_by_or_1_members']))  # noqa: E501
        if 'count_0_filter_by_name_like' in params:
            query_params.append(('count[0][filterBy][name][like]', params['count_0_filter_by_name_like']))  # noqa: E501
        if 'count_1_filter_by_created_at_from' in params:
            query_params.append(('count[1][filterBy][createdAt][from]', params['count_1_filter_by_created_at_from']))  # noqa: E501
        if 'search_by' in params:
            query_params.append(('searchBy', params['search_by']))  # noqa: E501

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
            '/teams', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TeamsList',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def updateteams(self, authorization, x_tenant, x_version, teams_id, body, **kwargs):  # noqa: E501
        """Update a specific team instance.  # noqa: E501

        Update a specific team instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.updateteams(authorization, x_tenant, x_version, teams_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: Basic Authentication. (required)
        :param str x_tenant: The tenant id. (required)
        :param str x_version: The API version. (required)
        :param str teams_id: The ID of the teams that will be updated. (required)
        :param Teams body: Data used to update teams (required)
        :return: Teams
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.updateteams_with_http_info(authorization, x_tenant, x_version, teams_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.updateteams_with_http_info(authorization, x_tenant, x_version, teams_id, body, **kwargs)  # noqa: E501
            return data

    def updateteams_with_http_info(self, authorization, x_tenant, x_version, teams_id, body, **kwargs):  # noqa: E501
        """Update a specific team instance.  # noqa: E501

        Update a specific team instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.updateteams_with_http_info(authorization, x_tenant, x_version, teams_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: Basic Authentication. (required)
        :param str x_tenant: The tenant id. (required)
        :param str x_version: The API version. (required)
        :param str teams_id: The ID of the teams that will be updated. (required)
        :param Teams body: Data used to update teams (required)
        :return: Teams
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'x_tenant', 'x_version', 'teams_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method updateteams" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `updateteams`")  # noqa: E501
        # verify the required parameter 'x_tenant' is set
        if ('x_tenant' not in params or
                params['x_tenant'] is None):
            raise ValueError("Missing the required parameter `x_tenant` when calling `updateteams`")  # noqa: E501
        # verify the required parameter 'x_version' is set
        if ('x_version' not in params or
                params['x_version'] is None):
            raise ValueError("Missing the required parameter `x_version` when calling `updateteams`")  # noqa: E501
        # verify the required parameter 'teams_id' is set
        if ('teams_id' not in params or
                params['teams_id'] is None):
            raise ValueError("Missing the required parameter `teams_id` when calling `updateteams`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `updateteams`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'teams_id' in params:
            path_params['teamsId'] = params['teams_id']  # noqa: E501

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
            '/teams/{teamsId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Teams',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
