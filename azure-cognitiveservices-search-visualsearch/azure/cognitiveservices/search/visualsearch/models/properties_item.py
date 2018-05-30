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


class PropertiesItem(Model):
    """Defines an item.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: Rating

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar text: Text representation of an item.
    :vartype text: str
    :param _type: Required. Constant filled by server.
    :type _type: str
    """

    _validation = {
        'text': {'readonly': True},
        '_type': {'required': True},
    }

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'},
        '_type': {'key': '_type', 'type': 'str'},
    }

    _subtype_map = {
        '_type': {'Rating': 'Rating'}
    }

    def __init__(self, **kwargs):
        super(PropertiesItem, self).__init__(**kwargs)
        self.text = None
        self._type = None
