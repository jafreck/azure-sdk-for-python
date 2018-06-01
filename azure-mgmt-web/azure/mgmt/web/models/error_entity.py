# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ErrorEntity(Model):
    """Body of the error response returned from the API.

    :param extended_code: Type of error.
    :type extended_code: str
    :param message_template: Message template.
    :type message_template: str
    :param parameters: Parameters for the template.
    :type parameters: list[str]
    :param inner_errors: Inner errors.
    :type inner_errors: list[~azure.mgmt.web.models.ErrorEntity]
    :param code: Basic error code.
    :type code: str
    :param message: Any details of the error.
    :type message: str
    """

    _attribute_map = {
        'extended_code': {'key': 'extendedCode', 'type': 'str'},
        'message_template': {'key': 'messageTemplate', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '[str]'},
        'inner_errors': {'key': 'innerErrors', 'type': '[ErrorEntity]'},
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ErrorEntity, self).__init__(**kwargs)
        self.extended_code = kwargs.get('extended_code', None)
        self.message_template = kwargs.get('message_template', None)
        self.parameters = kwargs.get('parameters', None)
        self.inner_errors = kwargs.get('inner_errors', None)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
