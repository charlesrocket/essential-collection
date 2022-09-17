# git_role
[![molecule](https://github.com/charlesrocket/git_role/actions/workflows/molecule.yml/badge.svg?branch=master&event=push)](https://github.com/charlesrocket/git_role/actions/workflows/molecule.yml)

Install Git on BSD/Linux machines with Ansible.

## Setup

Use `ansible-galaxy install charlesrocket.git`.

## Example

```
- name: Playbook
  hosts: all

  roles:
    - charlesrocket.git
```

#### Tested on

- generic/alpine316
- generic/debian11
- generic/fedora36
- generic/freebsd13
- generic/netbsd9
- generic/openbsd7
