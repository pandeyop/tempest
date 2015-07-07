# Copyright 2014 NEC Corporation.  All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

add_remove_list_flavor_access = {
    'status_code': [200],
    'response_body': {
        'type': 'object',
        'properties': {
            'flavor_access': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'flavor_id': {'type': 'string'},
                        'tenant_id': {'type': 'string'},
                    },
                    'additionalProperties': False,
                    'required': ['flavor_id', 'tenant_id'],
                }
            }
        },
        'additionalProperties': False,
        'required': ['flavor_access']
    }
}
