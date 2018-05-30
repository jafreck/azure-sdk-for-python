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

from .queue_build_request import QueueBuildRequest


class BuildTaskBuildRequest(QueueBuildRequest):
    """The queue build parameters based on a build task.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :param build_task_name: Required. The name of build task against which
     build has to be queued.
    :type build_task_name: str
    """

    _validation = {
        'type': {'required': True},
        'build_task_name': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'build_task_name': {'key': 'buildTaskName', 'type': 'str'},
    }

    def __init__(self, *, build_task_name: str, **kwargs) -> None:
        super(BuildTaskBuildRequest, self).__init__(**kwargs)
        self.build_task_name = build_task_name
        self.type = 'BuildTask'
