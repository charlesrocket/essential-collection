#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2023, charlesrocket
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
module: remote_vars
short_description: Include variables from remote files
description:
  - Download variables file from remote host and inject them into C(ansible_facts)
version_added: "1.2.0"
options:
  url:
    description:
      - Location of a remote YAML file.
    type: str
    required: true

author:
  - k (@charlesrocket)
'''

EXAMPLES = r'''
- name: Import user variables
  charlesrocket.essential.remote_vars:
    url: https://www.example.com/user_vars.yml
'''

RETURN = r''' # '''
