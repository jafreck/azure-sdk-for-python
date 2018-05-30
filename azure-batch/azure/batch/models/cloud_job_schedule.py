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


class CloudJobSchedule(Model):
    """A job schedule that allows recurring jobs by specifying when to run jobs
    and a specification used to create each job.

    :param id: A string that uniquely identifies the schedule within the
     account.
    :type id: str
    :param display_name: The display name for the schedule.
    :type display_name: str
    :param url: The URL of the job schedule.
    :type url: str
    :param e_tag: The ETag of the job schedule. This is an opaque string. You
     can use it to detect whether the job schedule has changed between
     requests. In particular, you can be pass the ETag with an Update Job
     Schedule request to specify that your changes should take effect only if
     nobody else has modified the schedule in the meantime.
    :type e_tag: str
    :param last_modified: The last modified time of the job schedule. This is
     the last time at which the schedule level data, such as the job
     specification or recurrence information, changed. It does not factor in
     job-level changes such as new jobs being created or jobs changing state.
    :type last_modified: datetime
    :param creation_time: The creation time of the job schedule.
    :type creation_time: datetime
    :param state: The current state of the job schedule. Possible values
     include: 'active', 'completed', 'disabled', 'terminating', 'deleting'
    :type state: str or ~azure.batch.models.JobScheduleState
    :param state_transition_time: The time at which the job schedule entered
     the current state.
    :type state_transition_time: datetime
    :param previous_state: The previous state of the job schedule. This
     property is not present if the job schedule is in its initial active
     state. Possible values include: 'active', 'completed', 'disabled',
     'terminating', 'deleting'
    :type previous_state: str or ~azure.batch.models.JobScheduleState
    :param previous_state_transition_time: The time at which the job schedule
     entered its previous state. This property is not present if the job
     schedule is in its initial active state.
    :type previous_state_transition_time: datetime
    :param schedule: The schedule according to which jobs will be created.
    :type schedule: ~azure.batch.models.Schedule
    :param job_specification: The details of the jobs to be created on this
     schedule.
    :type job_specification: ~azure.batch.models.JobSpecification
    :param execution_info: Information about jobs that have been and will be
     run under this schedule.
    :type execution_info: ~azure.batch.models.JobScheduleExecutionInformation
    :param metadata: A list of name-value pairs associated with the schedule
     as metadata. The Batch service does not assign any meaning to metadata; it
     is solely for the use of user code.
    :type metadata: list[~azure.batch.models.MetadataItem]
    :param stats: The lifetime resource usage statistics for the job schedule.
     The statistics may not be immediately available. The Batch service
     performs periodic roll-up of statistics. The typical delay is about 30
     minutes.
    :type stats: ~azure.batch.models.JobScheduleStatistics
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'JobScheduleState'},
        'state_transition_time': {'key': 'stateTransitionTime', 'type': 'iso-8601'},
        'previous_state': {'key': 'previousState', 'type': 'JobScheduleState'},
        'previous_state_transition_time': {'key': 'previousStateTransitionTime', 'type': 'iso-8601'},
        'schedule': {'key': 'schedule', 'type': 'Schedule'},
        'job_specification': {'key': 'jobSpecification', 'type': 'JobSpecification'},
        'execution_info': {'key': 'executionInfo', 'type': 'JobScheduleExecutionInformation'},
        'metadata': {'key': 'metadata', 'type': '[MetadataItem]'},
        'stats': {'key': 'stats', 'type': 'JobScheduleStatistics'},
    }

    def __init__(self, id=None, display_name=None, url=None, e_tag=None, last_modified=None, creation_time=None, state=None, state_transition_time=None, previous_state=None, previous_state_transition_time=None, schedule=None, job_specification=None, execution_info=None, metadata=None, stats=None):
        super(CloudJobSchedule, self).__init__()
        self.id = id
        self.display_name = display_name
        self.url = url
        self.e_tag = e_tag
        self.last_modified = last_modified
        self.creation_time = creation_time
        self.state = state
        self.state_transition_time = state_transition_time
        self.previous_state = previous_state
        self.previous_state_transition_time = previous_state_transition_time
        self.schedule = schedule
        self.job_specification = job_specification
        self.execution_info = execution_info
        self.metadata = metadata
        self.stats = stats
