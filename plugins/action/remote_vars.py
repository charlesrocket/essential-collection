from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import urllib
import yaml

from ansible.errors import AnsibleError
from ansible.plugins.action import ActionBase
from ansible.module_utils.urls import open_url
from ansible.module_utils.common.text.converters import to_native


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        result = super().run(tmp, task_vars)
        url = self._task.args.get('url')

        if not url:
            return {'failed': True, 'msg': 'URL is missing or invalid'}

        response = None

        try:
            response = open_url(url, timeout=10)
            content = response.read().decode()
            loaded_vars = yaml.safe_load(content)

            if not loaded_vars:
                return {'failed': True,
                        'msg': 'No variables found'}

            loaded_vars = self._templar.template(loaded_vars)
            result['ansible_facts'] = dict(
                task_vars['ansible_facts'],
                **loaded_vars)

        except urllib.error.URLError as err:
            raise AnsibleError('Error connecting to %s: %s'
                               % (to_native(url), to_native(err))) from err

        except yaml.YAMLError as err:
            raise AnsibleError('Error loading YAML from %s: %s'
                               % (to_native(url), to_native(err))) from err

        finally:
            if response is not None:
                response.close()

        content = None
        result['new_vars'] = loaded_vars

        return result
