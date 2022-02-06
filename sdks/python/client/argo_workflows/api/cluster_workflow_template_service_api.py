"""
    Argo Workflows API

    Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argoproj.github.io/argo-workflows/  # noqa: E501

    The version of the OpenAPI document: VERSION
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from argo_workflows.api_client import ApiClient, Endpoint as _Endpoint
from argo_workflows.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_workflow_v1alpha1_cluster_workflow_template import IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate
from argo_workflows.model.io_argoproj_workflow_v1alpha1_cluster_workflow_template_create_request import IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateCreateRequest
from argo_workflows.model.io_argoproj_workflow_v1alpha1_cluster_workflow_template_lint_request import IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateLintRequest
from argo_workflows.model.io_argoproj_workflow_v1alpha1_cluster_workflow_template_list import IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateList
from argo_workflows.model.io_argoproj_workflow_v1alpha1_cluster_workflow_template_update_request import IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateUpdateRequest


class ClusterWorkflowTemplateServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_cluster_workflow_template(
            self,
            body,
            **kwargs
        ):
            """create_cluster_workflow_template  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_cluster_workflow_template(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateCreateRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.create_cluster_workflow_template = _Endpoint(
            settings={
                'response_type': (IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate,),
                'auth': [],
                'endpoint_path': '/api/v1/cluster-workflow-templates',
                'operation_id': 'create_cluster_workflow_template',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
                ],
                'required': [
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'body':
                        (IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateCreateRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__create_cluster_workflow_template
        )

        def __delete_cluster_workflow_template(
            self,
            name,
            **kwargs
        ):
            """delete_cluster_workflow_template  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_cluster_workflow_template(name, async_req=True)
            >>> result = thread.get()

            Args:
                name (str):

            Keyword Args:
                delete_options_grace_period_seconds (str): The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. +optional.. [optional]
                delete_options_preconditions_uid (str): Specifies the target UID. +optional.. [optional]
                delete_options_preconditions_resource_version (str): Specifies the target ResourceVersion +optional.. [optional]
                delete_options_orphan_dependents (bool): Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. +optional.. [optional]
                delete_options_propagation_policy (str): Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. +optional.. [optional]
                delete_options_dry_run ([str]): When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed +optional.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                bool, date, datetime, dict, float, int, list, str, none_type
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['name'] = \
                name
            return self.call_with_http_info(**kwargs)

        self.delete_cluster_workflow_template = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [],
                'endpoint_path': '/api/v1/cluster-workflow-templates/{name}',
                'operation_id': 'delete_cluster_workflow_template',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'name',
                    'delete_options_grace_period_seconds',
                    'delete_options_preconditions_uid',
                    'delete_options_preconditions_resource_version',
                    'delete_options_orphan_dependents',
                    'delete_options_propagation_policy',
                    'delete_options_dry_run',
                ],
                'required': [
                    'name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'name':
                        (str,),
                    'delete_options_grace_period_seconds':
                        (str,),
                    'delete_options_preconditions_uid':
                        (str,),
                    'delete_options_preconditions_resource_version':
                        (str,),
                    'delete_options_orphan_dependents':
                        (bool,),
                    'delete_options_propagation_policy':
                        (str,),
                    'delete_options_dry_run':
                        ([str],),
                },
                'attribute_map': {
                    'name': 'name',
                    'delete_options_grace_period_seconds': 'deleteOptions.gracePeriodSeconds',
                    'delete_options_preconditions_uid': 'deleteOptions.preconditions.uid',
                    'delete_options_preconditions_resource_version': 'deleteOptions.preconditions.resourceVersion',
                    'delete_options_orphan_dependents': 'deleteOptions.orphanDependents',
                    'delete_options_propagation_policy': 'deleteOptions.propagationPolicy',
                    'delete_options_dry_run': 'deleteOptions.dryRun',
                },
                'location_map': {
                    'name': 'path',
                    'delete_options_grace_period_seconds': 'query',
                    'delete_options_preconditions_uid': 'query',
                    'delete_options_preconditions_resource_version': 'query',
                    'delete_options_orphan_dependents': 'query',
                    'delete_options_propagation_policy': 'query',
                    'delete_options_dry_run': 'query',
                },
                'collection_format_map': {
                    'delete_options_dry_run': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_cluster_workflow_template
        )

        def __get_cluster_workflow_template(
            self,
            name,
            **kwargs
        ):
            """get_cluster_workflow_template  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_cluster_workflow_template(name, async_req=True)
            >>> result = thread.get()

            Args:
                name (str):

            Keyword Args:
                get_options_resource_version (str): resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset +optional. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['name'] = \
                name
            return self.call_with_http_info(**kwargs)

        self.get_cluster_workflow_template = _Endpoint(
            settings={
                'response_type': (IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate,),
                'auth': [],
                'endpoint_path': '/api/v1/cluster-workflow-templates/{name}',
                'operation_id': 'get_cluster_workflow_template',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'name',
                    'get_options_resource_version',
                ],
                'required': [
                    'name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'name':
                        (str,),
                    'get_options_resource_version':
                        (str,),
                },
                'attribute_map': {
                    'name': 'name',
                    'get_options_resource_version': 'getOptions.resourceVersion',
                },
                'location_map': {
                    'name': 'path',
                    'get_options_resource_version': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_cluster_workflow_template
        )

        def __lint_cluster_workflow_template(
            self,
            body,
            **kwargs
        ):
            """lint_cluster_workflow_template  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.lint_cluster_workflow_template(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateLintRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.lint_cluster_workflow_template = _Endpoint(
            settings={
                'response_type': (IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate,),
                'auth': [],
                'endpoint_path': '/api/v1/cluster-workflow-templates/lint',
                'operation_id': 'lint_cluster_workflow_template',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
                ],
                'required': [
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'body':
                        (IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateLintRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__lint_cluster_workflow_template
        )

        def __list_cluster_workflow_templates(
            self,
            **kwargs
        ):
            """list_cluster_workflow_templates  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_cluster_workflow_templates(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                list_options_label_selector (str): A selector to restrict the list of returned objects by their labels. Defaults to everything. +optional.. [optional]
                list_options_field_selector (str): A selector to restrict the list of returned objects by their fields. Defaults to everything. +optional.. [optional]
                list_options_watch (bool): Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. +optional.. [optional]
                list_options_allow_watch_bookmarks (bool): allowWatchBookmarks requests watch events with type \"BOOKMARK\". Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server's discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored. +optional.. [optional]
                list_options_resource_version (str): resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset +optional. [optional]
                list_options_resource_version_match (str): resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset +optional. [optional]
                list_options_timeout_seconds (str): Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. +optional.. [optional]
                list_options_limit (str): limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.. [optional]
                list_options_continue (str): The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateList
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.list_cluster_workflow_templates = _Endpoint(
            settings={
                'response_type': (IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateList,),
                'auth': [],
                'endpoint_path': '/api/v1/cluster-workflow-templates',
                'operation_id': 'list_cluster_workflow_templates',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'list_options_label_selector',
                    'list_options_field_selector',
                    'list_options_watch',
                    'list_options_allow_watch_bookmarks',
                    'list_options_resource_version',
                    'list_options_resource_version_match',
                    'list_options_timeout_seconds',
                    'list_options_limit',
                    'list_options_continue',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'list_options_label_selector':
                        (str,),
                    'list_options_field_selector':
                        (str,),
                    'list_options_watch':
                        (bool,),
                    'list_options_allow_watch_bookmarks':
                        (bool,),
                    'list_options_resource_version':
                        (str,),
                    'list_options_resource_version_match':
                        (str,),
                    'list_options_timeout_seconds':
                        (str,),
                    'list_options_limit':
                        (str,),
                    'list_options_continue':
                        (str,),
                },
                'attribute_map': {
                    'list_options_label_selector': 'listOptions.labelSelector',
                    'list_options_field_selector': 'listOptions.fieldSelector',
                    'list_options_watch': 'listOptions.watch',
                    'list_options_allow_watch_bookmarks': 'listOptions.allowWatchBookmarks',
                    'list_options_resource_version': 'listOptions.resourceVersion',
                    'list_options_resource_version_match': 'listOptions.resourceVersionMatch',
                    'list_options_timeout_seconds': 'listOptions.timeoutSeconds',
                    'list_options_limit': 'listOptions.limit',
                    'list_options_continue': 'listOptions.continue',
                },
                'location_map': {
                    'list_options_label_selector': 'query',
                    'list_options_field_selector': 'query',
                    'list_options_watch': 'query',
                    'list_options_allow_watch_bookmarks': 'query',
                    'list_options_resource_version': 'query',
                    'list_options_resource_version_match': 'query',
                    'list_options_timeout_seconds': 'query',
                    'list_options_limit': 'query',
                    'list_options_continue': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_cluster_workflow_templates
        )

        def __update_cluster_workflow_template(
            self,
            name,
            body,
            **kwargs
        ):
            """update_cluster_workflow_template  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_cluster_workflow_template(name, body, async_req=True)
            >>> result = thread.get()

            Args:
                name (str): DEPRECATED: This field is ignored.
                body (IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateUpdateRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['name'] = \
                name
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.update_cluster_workflow_template = _Endpoint(
            settings={
                'response_type': (IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate,),
                'auth': [],
                'endpoint_path': '/api/v1/cluster-workflow-templates/{name}',
                'operation_id': 'update_cluster_workflow_template',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'name',
                    'body',
                ],
                'required': [
                    'name',
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'name':
                        (str,),
                    'body':
                        (IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateUpdateRequest,),
                },
                'attribute_map': {
                    'name': 'name',
                },
                'location_map': {
                    'name': 'path',
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_cluster_workflow_template
        )
