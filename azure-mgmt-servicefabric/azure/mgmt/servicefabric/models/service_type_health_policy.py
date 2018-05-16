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


class ServiceTypeHealthPolicy(Model):
    """Represents the health policy used to evaluate the health of services
    belonging to a service type.
    .

    :param max_percent_unhealthy_services: The maximum percentage of services
     allowed to be unhealthy before your application is considered in error.
     . Default value: 0 .
    :type max_percent_unhealthy_services: int
    """

    _validation = {
        'max_percent_unhealthy_services': {'maximum': 100, 'minimum': 0},
    }

    _attribute_map = {
        'max_percent_unhealthy_services': {'key': 'maxPercentUnhealthyServices', 'type': 'int'},
    }

    def __init__(self, max_percent_unhealthy_services=0):
        super(ServiceTypeHealthPolicy, self).__init__()
        self.max_percent_unhealthy_services = max_percent_unhealthy_services
