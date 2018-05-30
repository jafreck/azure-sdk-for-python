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

from .resource import Resource


class SBTopic(Resource):
    """Description of topic resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :ivar size_in_bytes: Size of the topic, in bytes.
    :vartype size_in_bytes: long
    :ivar created_at: Exact time the message was created.
    :vartype created_at: datetime
    :ivar updated_at: The exact time the message was updated.
    :vartype updated_at: datetime
    :ivar accessed_at: Last time the message was sent, or a request was
     received, for this topic.
    :vartype accessed_at: datetime
    :ivar subscription_count: Number of subscriptions.
    :vartype subscription_count: int
    :ivar count_details: Message count deatils
    :vartype count_details: ~azure.mgmt.servicebus.models.MessageCountDetails
    :param default_message_time_to_live: ISO 8601 Default message timespan to
     live value. This is the duration after which the message expires, starting
     from when the message is sent to Service Bus. This is the default value
     used when TimeToLive is not set on a message itself.
    :type default_message_time_to_live: timedelta
    :param max_size_in_megabytes: Maximum size of the topic in megabytes,
     which is the size of the memory allocated for the topic. Default is 1024.
    :type max_size_in_megabytes: int
    :param requires_duplicate_detection: Value indicating if this topic
     requires duplicate detection.
    :type requires_duplicate_detection: bool
    :param duplicate_detection_history_time_window: ISO8601 timespan structure
     that defines the duration of the duplicate detection history. The default
     value is 10 minutes.
    :type duplicate_detection_history_time_window: timedelta
    :param enable_batched_operations: Value that indicates whether server-side
     batched operations are enabled.
    :type enable_batched_operations: bool
    :param status: Enumerates the possible values for the status of a
     messaging entity. Possible values include: 'Active', 'Disabled',
     'Restoring', 'SendDisabled', 'ReceiveDisabled', 'Creating', 'Deleting',
     'Renaming', 'Unknown'
    :type status: str or ~azure.mgmt.servicebus.models.EntityStatus
    :param support_ordering: Value that indicates whether the topic supports
     ordering.
    :type support_ordering: bool
    :param auto_delete_on_idle: ISO 8601 timespan idle interval after which
     the topic is automatically deleted. The minimum duration is 5 minutes.
    :type auto_delete_on_idle: timedelta
    :param enable_partitioning: Value that indicates whether the topic to be
     partitioned across multiple message brokers is enabled.
    :type enable_partitioning: bool
    :param enable_express: Value that indicates whether Express Entities are
     enabled. An express topic holds a message in memory temporarily before
     writing it to persistent storage.
    :type enable_express: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'size_in_bytes': {'readonly': True},
        'created_at': {'readonly': True},
        'updated_at': {'readonly': True},
        'accessed_at': {'readonly': True},
        'subscription_count': {'readonly': True},
        'count_details': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'size_in_bytes': {'key': 'properties.sizeInBytes', 'type': 'long'},
        'created_at': {'key': 'properties.createdAt', 'type': 'iso-8601'},
        'updated_at': {'key': 'properties.updatedAt', 'type': 'iso-8601'},
        'accessed_at': {'key': 'properties.accessedAt', 'type': 'iso-8601'},
        'subscription_count': {'key': 'properties.subscriptionCount', 'type': 'int'},
        'count_details': {'key': 'properties.countDetails', 'type': 'MessageCountDetails'},
        'default_message_time_to_live': {'key': 'properties.defaultMessageTimeToLive', 'type': 'duration'},
        'max_size_in_megabytes': {'key': 'properties.maxSizeInMegabytes', 'type': 'int'},
        'requires_duplicate_detection': {'key': 'properties.requiresDuplicateDetection', 'type': 'bool'},
        'duplicate_detection_history_time_window': {'key': 'properties.duplicateDetectionHistoryTimeWindow', 'type': 'duration'},
        'enable_batched_operations': {'key': 'properties.enableBatchedOperations', 'type': 'bool'},
        'status': {'key': 'properties.status', 'type': 'EntityStatus'},
        'support_ordering': {'key': 'properties.supportOrdering', 'type': 'bool'},
        'auto_delete_on_idle': {'key': 'properties.autoDeleteOnIdle', 'type': 'duration'},
        'enable_partitioning': {'key': 'properties.enablePartitioning', 'type': 'bool'},
        'enable_express': {'key': 'properties.enableExpress', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(SBTopic, self).__init__(**kwargs)
        self.size_in_bytes = None
        self.created_at = None
        self.updated_at = None
        self.accessed_at = None
        self.subscription_count = None
        self.count_details = None
        self.default_message_time_to_live = kwargs.get('default_message_time_to_live', None)
        self.max_size_in_megabytes = kwargs.get('max_size_in_megabytes', None)
        self.requires_duplicate_detection = kwargs.get('requires_duplicate_detection', None)
        self.duplicate_detection_history_time_window = kwargs.get('duplicate_detection_history_time_window', None)
        self.enable_batched_operations = kwargs.get('enable_batched_operations', None)
        self.status = kwargs.get('status', None)
        self.support_ordering = kwargs.get('support_ordering', None)
        self.auto_delete_on_idle = kwargs.get('auto_delete_on_idle', None)
        self.enable_partitioning = kwargs.get('enable_partitioning', None)
        self.enable_express = kwargs.get('enable_express', None)
