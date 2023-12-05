#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2023, charlesrocket
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: remote_vars
short_description: Includes variables from remote files
deprecated:
  removed_in: '1.4.0'
  alternative: Use M(charlesrocket.essential.fetch_vars) instead.
description:
  - Download variables file from remote hosts and inject it into C(ansible_facts).
options:
  url:
    description:
      - Location of a remote YAML file.
    type: str
    required: true
extends_documentation_fragment:
- action_common_attributes
- action_common_attributes.facts
attributes:
    check_mode:
        support: full
    diff_mode:
        support: none
    facts:
        support: full
    platform:
        platforms: all

author:
  - k (@charlesrocket)
'''

EXAMPLES = r'''
- name: Import user variables
  charlesrocket.essential.remote_vars:
    url: https://www.example.com/user_vars.yml
'''

RETURN = r'''
ansible_facts:
  description: Updated C(ansible_facts)
  returned: success
  type: dict
  sample: {'variable': 'value'}
new_vars:
  description: Downloaded variables
  returned: success
  type: dict
  sample: {'variable': 'value'}
'''
