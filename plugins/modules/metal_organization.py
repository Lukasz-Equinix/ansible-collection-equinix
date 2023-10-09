#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# DOCUMENTATION, EXAMPLES, and RETURN are generated by
# ansible_specdoc. Do not edit them directly.

DOCUMENTATION = '''
author: Equinix DevRel Team (@equinix) <support@equinix.com>
description: !!python/tuple
- 'Lookup a single organization by ID in Equinix Metal. '
- 'This resource only fetches a single organization by resource ID. '
- It doesn't allow to create or update organizations.
module: metal_organization
notes: []
options:
  id:
    description:
    - UUID of the organization.
    required: true
    type: str
requirements: null
short_description: Lookup a single organization by ID in Equinix Metal
'''
EXAMPLES = '''
- name: Lookup a single organization by id
  hosts: localhost
  tasks:
  - equinix.cloud.metal_organization:
      id: 7624f0f7-75b6-4271-bc64-632b80f87de2
'''
RETURN = '''
metal_organization:
  description: The module object
  returned: always
  sample:
  - "\n{\n\n  \"changed\": false,\n  \"description\": \"\",\n  \"id\": \"70c2f878-9f32-452e-8c69-ab15480e1d99\"\
    ,\n  },\n  \"name\": \"Tomas\u2019 Projects\",\n  \"projects\": [\n      \"18234234-0432-4eb5-9636-5f05671ff33a\"\
    ,\n      \"4394a515-8423-46ed-b0f5-8bfd09573a06\",\n      \"52000324-e342-4673-93a8-de242342343b\"\
    ,\n      \"64234231-bce5-4a62-a47c-14234d7ea8d9\",\n      \"81423459-f69d-40c4-9b72-51e23c324243\"\
    ,\n      \"e9324234-6423-4232-8423-854234238106\"\n  ],\n  \"website\": \"\"\n\
    }\n"
  type: dict
'''

# End of generated documentation

# This is a template for a new module. It is not meant to be used as is.
# It is meant to be copied and modified to create a new module.
# Replace all occurrences of "metal_organization" with the name of the new
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


module_spec = dict(
    id=SpecField(
        type=FieldType.string,
        required=True,
        description=['UUID of the organization.'],
    ),
)


specdoc_examples = [
    '''
- name: Lookup a single organization by id
  hosts: localhost
  tasks:
  - equinix.cloud.metal_organization:
      id: 7624f0f7-75b6-4271-bc64-632b80f87de2
''',
]

result_sample = ['''
{

  "changed": false,
  "description": "",
  "id": "70c2f878-9f32-452e-8c69-ab15480e1d99",
  },
  "name": "Tomas’ Projects",
  "projects": [
      "18234234-0432-4eb5-9636-5f05671ff33a",
      "4394a515-8423-46ed-b0f5-8bfd09573a06",
      "52000324-e342-4673-93a8-de242342343b",
      "64234231-bce5-4a62-a47c-14234d7ea8d9",
      "81423459-f69d-40c4-9b72-51e23c324243",
      "e9324234-6423-4232-8423-854234238106"
  ],
  "website": ""
}
''']

SPECDOC_META = getSpecDocMeta(
    short_description='Lookup a single organization by ID in Equinix Metal',
    description=(
        'Lookup a single organization by ID in Equinix Metal. ',
        'This resource only fetches a single organization by resource ID. ',
        "It doesn't allow to create or update organizations.",
    ),
    examples=specdoc_examples,
    options=module_spec,
    return_values={
        "metal_organization": SpecReturnValue(
            description='The module object',
            type=FieldType.dict,
            sample=result_sample,
        ),
    },
)


def main():
    module = EquinixModule(
        argument_spec=SPECDOC_META.ansible_spec,
    )

    state = module.params.get("state")
    if state == "absent":
        module.fail_json(msg="absent state is not supported in this module")
    changed = False

    try:
        module.params_syntax_check()
        fetched = module.get_by_id("metal_organization", False)

        if fetched:
            module.params['id'] = fetched['id']
        else:
            module.fail_json(msg="Organization not found")
    except Exception as e:
        tb = traceback.format_exc()
        module.fail_json(msg="Error in metal_organization: {0}".format(to_native(e)),
                         exception=tb)

    fetched.update({'changed': changed})
    module.exit_json(**fetched)


if __name__ == '__main__':
    main()