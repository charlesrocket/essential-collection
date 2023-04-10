from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import urllib
import yaml

from ansible.plugins.action import ActionBase
from ansible.module_utils.urls import open_url
from ansible.module_utils._text import to_native
from ansible.utils.display import Display

display = Display()


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        result = super().run(tmp, task_vars)
        url = self._task.args.get('url')

        if not url:
            return {'failed': True, 'msg': 'URL is missing or invalid'}

        try:
            with open_url(url, timeout=10) as response:
                content = response.read().decode()
                loaded_vars = yaml.safe_load(content)

                if not loaded_vars:
                    return {'failed': True,
                            'msg': 'No variables found in content'}

                loaded_vars = self._templar.template(loaded_vars)
                result['ansible_facts'] = dict(
                    task_vars['ansible_facts'],
                    **loaded_vars)

        except urllib.error.URLError as err:
            return {'failed': True,
                    'msg':
                    f"Error connecting to URL {url}: {to_native(err)}"}

        except yaml.YAMLError as err:
            return {'failed': True,
                    'msg':
                    f"Error loading YAML from URL {url}: {to_native(err)}"}

        finally:
            response.close()

        content = None
        result['new_vars'] = loaded_vars

        return result
