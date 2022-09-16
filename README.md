# git_role
[![molecule](https://github.com/charlesrocket/git_role/actions/workflows/molecule.yml/badge.svg?branch=master&event=push)](https://github.com/charlesrocket/git_role/actions/workflows/molecule.yml)

Install Git on BSD/Linux machines with Ansible.

## Example
```
- name: Playbook
  hosts: all

  roles:
    - {role: charlesrocket.git}
```

#### Tested on

- generic/debian11
- generic/fedora36
- generic/opensuse15
- generic/freebsd13
- generic/netbsd9
- generic/openbsd7
