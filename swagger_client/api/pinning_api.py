# coding: utf-8

"""
    Estuary API

    This is the API for the Estuary application.  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PinningApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def pinning_pins_get(self, **kwargs):  # noqa: E501
        """List all pin status objects  # noqa: E501

        This endpoint lists all pin status objects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pinning_pins_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pinning_pins_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.pinning_pins_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def pinning_pins_get_with_http_info(self, **kwargs):  # noqa: E501
        """List all pin status objects  # noqa: E501

        This endpoint lists all pin status objects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pinning_pins_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pinning_pins_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pinning/pins', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pinning_pins_pinid_delete(self, pinid, **kwargs):  # noqa: E501
        """Delete a pinned object  # noqa: E501

        This endpoint deletes a pinned object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pinning_pins_pinid_delete(pinid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pinid: Pin ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pinning_pins_pinid_delete_with_http_info(pinid, **kwargs)  # noqa: E501
        else:
            (data) = self.pinning_pins_pinid_delete_with_http_info(pinid, **kwargs)  # noqa: E501
            return data

    def pinning_pins_pinid_delete_with_http_info(self, pinid, **kwargs):  # noqa: E501
        """Delete a pinned object  # noqa: E501

        This endpoint deletes a pinned object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pinning_pins_pinid_delete_with_http_info(pinid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pinid: Pin ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pinid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pinning_pins_pinid_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pinid' is set
        if ('pinid' not in params or
                params['pinid'] is None):
            raise ValueError("Missing the required parameter `pinid` when calling `pinning_pins_pinid_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pinid' in params:
            path_params['pinid'] = params['pinid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pinning/pins/{pinid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pinning_pins_pinid_get(self, pinid, **kwargs):  # noqa: E501
        """Get a pin status object  # noqa: E501

        This endpoint returns a pin status object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pinning_pins_pinid_get(pinid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pinid: cid (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pinning_pins_pinid_get_with_http_info(pinid, **kwargs)  # noqa: E501
        else:
            (data) = self.pinning_pins_pinid_get_with_http_info(pinid, **kwargs)  # noqa: E501
            return data

    def pinning_pins_pinid_get_with_http_info(self, pinid, **kwargs):  # noqa: E501
        """Get a pin status object  # noqa: E501

        This endpoint returns a pin status object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pinning_pins_pinid_get_with_http_info(pinid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pinid: cid (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pinid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pinning_pins_pinid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pinid' is set
        if ('pinid' not in params or
                params['pinid'] is None):
            raise ValueError("Missing the required parameter `pinid` when calling `pinning_pins_pinid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pinid' in params:
            path_params['pinid'] = params['pinid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pinning/pins/{pinid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pinning_pins_pinid_post(self, pinid, **kwargs):  # noqa: E501
        """Replace a pinned object  # noqa: E501

        This endpoint replaces a pinned object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pinning_pins_pinid_post(pinid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pinid: Pin ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pinning_pins_pinid_post_with_http_info(pinid, **kwargs)  # noqa: E501
        else:
            (data) = self.pinning_pins_pinid_post_with_http_info(pinid, **kwargs)  # noqa: E501
            return data

    def pinning_pins_pinid_post_with_http_info(self, pinid, **kwargs):  # noqa: E501
        """Replace a pinned object  # noqa: E501

        This endpoint replaces a pinned object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pinning_pins_pinid_post_with_http_info(pinid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pinid: Pin ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pinid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pinning_pins_pinid_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pinid' is set
        if ('pinid' not in params or
                params['pinid'] is None):
            raise ValueError("Missing the required parameter `pinid` when calling `pinning_pins_pinid_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pinid' in params:
            path_params['pinid'] = params['pinid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pinning/pins/{pinid}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pinning_pins_post(self, cid, name, **kwargs):  # noqa: E501
        """Add and pin object  # noqa: E501

        This endpoint adds a pin to the IPFS daemon.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pinning_pins_post(cid, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cid: cid (required)
        :param str name: name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pinning_pins_post_with_http_info(cid, name, **kwargs)  # noqa: E501
        else:
            (data) = self.pinning_pins_post_with_http_info(cid, name, **kwargs)  # noqa: E501
            return data

    def pinning_pins_post_with_http_info(self, cid, name, **kwargs):  # noqa: E501
        """Add and pin object  # noqa: E501

        This endpoint adds a pin to the IPFS daemon.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pinning_pins_post_with_http_info(cid, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cid: cid (required)
        :param str name: name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cid', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pinning_pins_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cid' is set
        if ('cid' not in params or
                params['cid'] is None):
            raise ValueError("Missing the required parameter `cid` when calling `pinning_pins_post`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `pinning_pins_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cid' in params:
            path_params['cid'] = params['cid']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pinning/pins', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
