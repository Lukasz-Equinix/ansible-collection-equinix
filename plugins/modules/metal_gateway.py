#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# DOCUMENTATION, EXAMPLES, and RETURN are generated by
# ansible_specdoc. Do not edit them directly.

DOCUMENTATION = '''
author: Equinix DevRel Team (@equinix) <support@equinix.com>
description: Manage Metal Gateway in Equinix Metal. You can use *id* or *ip_reservation_id*
  to lookup a Gateway. If you want to create new resource, you must provide *project_id*,
  *virtual_network_id* and either *ip_reservation_id* or *private_ipv4_subnet_size*.
module: metal_gateway
notes: []
options:
  id:
    description:
    - UUID of the gateway.
    required: false
    type: str
  ip_reservation_id:
    description:
    - UUID of Public Reservation to associate with the gateway, the reservation must
      be in the same metro as the VLAN, conflicts with private_ipv4_subnet_size.
    required: false
    type: str
  private_ipv4_subnet_size:
    description:
    - Size of the private IPv4 subnet to create for this metal gateway, must be one
      of 8, 16, 32, 64, 128. Conflicts with ip_reservation_id.
    required: false
    type: int
  project_id:
    description:
    - UUID of the project where the gateway is scoped to.
    required: false
    type: str
  timeout:
    default: 10
    description:
    - Timeout in seconds for gateway to get to "ready" state, and for gateway to be
      removed
    required: false
    type: int
  virtual_network_id:
    description:
    - UUID of the VLAN where the gateway is scoped to.
    required: false
    type: str
requirements: null
short_description: Manage Metal Gateway in Equinix Metal
'''
EXAMPLES = '''
- name: Create new gateway with existing IP reservation
  hosts: localhost
  tasks:
  - equinix.cloud.metal_gateway:
      project_id: a4cc87f9-e00f-48c2-9460-74aa60beb6b0
      ip_reservation_id: 83b5503c-7b7f-4883-9509-b6b728b41491
      virtual_network_id: eef49903-7a09-4ca1-af67-4087c29ab5b6
- name: Create new gateway with new private /29 subnet
  hosts: localhost
  tasks:
  - equinix.cloud.metal_gateway:
      project_id: '{{ project.id }}'
      virtual_network_id: '{{ vlan.id }}'
      private_ipv4_subnet_size: 8
- name: Lookup a gateway by ID
  hosts: localhost
  tasks:
  - equinix.cloud.metal_gateway:
      id: eef49903-7a09-4ca1-af67-4087c29ab5b6
    register: gateway
- name: Lookup a gateway by IP reservation ID
  hosts: localhost
  tasks:
  - equinix.cloud.metal_gateway:
      ip_reservation_id: a4cc87f9-e00f-48c2-9460-74aa60beb6b0
    register: gateway
'''
RETURN = '''
metal_gateway:
  description: The module object
  returned: always
  sample:
  - changed: true
    id: 1f4d30da-4041-406d-8d94-6ce929340d98
    ip_reservation_id: fa017281-b10e-4b22-b449-35a93fb88d85
    metal_state: ready
    project_id: 2e85a66a-ea6a-4e33-8029-cc5ab9a0bc91
    virtual_network_id: 4a06c542-e47c-4e3c-ab85-bfc3cba4004d
  - changed: true
    id: be809e36-42a0-4a3b-982c-8f4487b9b9fc
    ip_reservation_id: e5c4be29-e238-431a-8c5f-f44f30fd5098
    metal_state: ready
    private_ipv4_subnet_size: 8
    project_id: 0491c16b-376d-4842-89d2-da3efead4991
    virtual_network_id: f46ab2c8-1332-4f87-91e9-f3a6a81d9769
  type: dict
'''

# End of generated documentation

# This is a template for a new module. It is not meant to be used as is.
# It is meant to be copied and modified to create a new module.
# Replace all occurrences of "metal_resource" with the name of the new
# module, for example "metal_vlan".


from ansible.module_utils._text import to_native
from ansible_specdoc.objects import (
    SpecField,
    FieldType,
    SpecReturnValue,
)
import traceback

from ansible_collections.equinix.cloud.plugins.module_utils.equinix import (
    EquinixModule,
    get_diff,
    getSpecDocMeta,
)

MODULE_NAME = "metal_gateway"

module_spec = dict(
    id=SpecField(
        type=FieldType.string,
        description=['UUID of the gateway.'],
    ),
    project_id=SpecField(
        type=FieldType.string,
        description=['UUID of the project where the gateway is scoped to.'],
    ),
    # in order to support VRF, we should do antoher parameter
    # vrf_ip_reservation_id which will use VRF 
    ip_reservation_id=SpecField(
        type=FieldType.string,
        conflicts_with=["private_ipv4_subnet_size"],
        description=['UUID of Public Reservation to associate with the gateway, the reservation must be in the same metro as the VLAN, conflicts with private_ipv4_subnet_size.'],
    ),
    private_ipv4_subnet_size=SpecField(
        type=FieldType.integer,
        conflicts_with=["ip_reservation_id"],
        description=['Size of the private IPv4 subnet to create for this metal gateway, must be one of 8, 16, 32, 64, 128. Conflicts with ip_reservation_id.'],
    ),
    virtual_network_id=SpecField(
        type=FieldType.string,
        description=['UUID of the VLAN where the gateway is scoped to.'],
    ),
    timeout=SpecField(
        type=FieldType.integer,
        description=['Timeout in seconds for gateway to get to "ready" state, and for gateway to be removed'],
        default=10,
    ),
)


specdoc_examples = [
'''
- name: Create new gateway with existing IP reservation
  hosts: localhost
  tasks:
  - equinix.cloud.metal_gateway:
      project_id: "a4cc87f9-e00f-48c2-9460-74aa60beb6b0"
      ip_reservation_id: "83b5503c-7b7f-4883-9509-b6b728b41491"
      virtual_network_id: "eef49903-7a09-4ca1-af67-4087c29ab5b6"
''',
'''
- name: Create new gateway with new private /29 subnet
  hosts: localhost
  tasks:
  - equinix.cloud.metal_gateway:
      project_id: "{{ project.id }}"
      virtual_network_id: "{{ vlan.id }}"
      private_ipv4_subnet_size: 8
''',
'''
- name: Lookup a gateway by ID
  hosts: localhost
  tasks:
  - equinix.cloud.metal_gateway:
      id: "eef49903-7a09-4ca1-af67-4087c29ab5b6"
    register: gateway
''',
'''
- name: Lookup a gateway by IP reservation ID
  hosts: localhost
  tasks:
  - equinix.cloud.metal_gateway:
      ip_reservation_id: "a4cc87f9-e00f-48c2-9460-74aa60beb6b0"
    register: gateway
''',
]

result_sample = [
{
                 
  "changed": True,
  "id": "1f4d30da-4041-406d-8d94-6ce929340d98",
  "ip_reservation_id": "fa017281-b10e-4b22-b449-35a93fb88d85",
  "metal_state": "ready",
  "project_id": "2e85a66a-ea6a-4e33-8029-cc5ab9a0bc91",
  "virtual_network_id": "4a06c542-e47c-4e3c-ab85-bfc3cba4004d"
},
{
  "changed": True,
  "id": "be809e36-42a0-4a3b-982c-8f4487b9b9fc",
  "ip_reservation_id": "e5c4be29-e238-431a-8c5f-f44f30fd5098",
  "metal_state": "ready",
  "private_ipv4_subnet_size": 8,
  "project_id": "0491c16b-376d-4842-89d2-da3efead4991",
  "virtual_network_id": "f46ab2c8-1332-4f87-91e9-f3a6a81d9769"
}
]

MUTABLE_ATTRIBUTES = [
    k for k, v in module_spec.items() if v.editable
]

SPECDOC_META = getSpecDocMeta(
    short_description='Manage Metal Gateway in Equinix Metal',
    description=(
        'Manage Metal Gateway in Equinix Metal. '
        'You can use *id* or *ip_reservation_id* to lookup a Gateway. '
        'If you want to create new resource, you must provide *project_id*, *virtual_network_id* and either *ip_reservation_id* or *private_ipv4_subnet_size*.'
    ),
    examples=specdoc_examples,
    options=module_spec,
    return_values={
        "metal_gateway": SpecReturnValue(
            description='The module object',
            type=FieldType.dict,
            sample=result_sample,
        ),
    },
)


def main():
    # In case you ever want to try to understand the dependencies between module options:
    # https://docs.ansible.com/ansible/latest/dev_guide/developing_program_flow_modules.html#argument-spec-dependencies
    module = EquinixModule(
        argument_spec=SPECDOC_META.ansible_spec,
        # we either create new gateway with ip_reservation_id or with private_ipv4_subnet_size
        mutually_exclusive=[("private_ipv4_subnet_size", "ip_reservation_id")],
        required_one_of=[
            # we either create new gateway or lookup existing one by id or 
            # by ip_reservation_id
            ("id", "project_id", "ip_reservation_id"),
            ],
        required_by=dict(
            # if we create new gateway in a project we need to provide virtual_network_id 
            project_id=["virtual_network_id"],
            # if we lookup existing gateway, we need to provide ip_reservation_id 
            ip_reservation_id=["virtual_network_id","project_id"],
        ),
        # I think we still need to check that:
        # - if we create new gateway in a project, either of ip_reservation_id or private_ipv4_subnet_size must be provided
    )


    state = module.params.get("state")
    changed = False
    fetched = False

    try:
      module.params_syntax_check()
      if module.params.get("id"):
          tolerate_not_found = state == "absent"
          fetched = module.get_by_id(MODULE_NAME, tolerate_not_found)
      else:
          fetched = None

          # If user supplied ip_reservation_id, we need to check if
          # there's already a gateway with the same reservation ID
          if module.params.get("ip_reservation_id") is not None:
              fetched = module.get_one_from_list(
                  MODULE_NAME,
                  ['ip_reservation_id'],
              )

      if fetched:
          module.params['id'] = fetched['id']
          if state == "present":
              diff = get_diff(module.params, fetched, MUTABLE_ATTRIBUTES)
              if diff:
                  module.fail_json(msg="Metal_gateway isn't mutable.")

          else:
              module.delete_by_id(MODULE_NAME)
              # We wait for removal because Terraform resource for Gateway
              # also waits for removal.
              module.wait_for_resource_removal(
                  "metal_gateway",
                  timeout=module.params.get("timeout"),
              )
              changed = True
      else:
          if state == "present":
              # if not any((module.params.get("private_ipv4_subnet_size"), module.params.get("ip_reservation_id"))):
              #     module.fail_json(msg="You must set either ip_reservation_id or private_ipv4_subnet_size!")
              # todo remove
              # module.params.pop("ip_reservation_id")
              fetched = module.create(MODULE_NAME)
              if 'id' not in fetched:
                  module.fail_json(msg="UUID not found in gateway creation response")
              module.params['id'] = fetched['id']
              seconds = module.params.get("timeout")
              fetched = module.wait_for_resource_condition(
                  "metal_gateway",
                  "metal_state",
                  "ready",
                  timeout=seconds)
              changed = True
          else:
              fetched = {}
    except Exception as e:
        tb = traceback.format_exc()
        module.fail_json(msg=f"Error in metal_gateway: {to_native(e)}",
                         exception=tb)

    fetched.update({'changed': changed})
    module.exit_json(**fetched)


if __name__ == '__main__':
    main()
