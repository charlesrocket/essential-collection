# git_role
[![Ansible Role](https://img.shields.io/ansible/role/60363)](https://galaxy.ansible.com/charlesrocket/git)
[![molecule](https://github.com/charlesrocket/git_role/actions/workflows/molecule.yml/badge.svg?branch=master&event=push)](https://github.com/charlesrocket/git_role/actions/workflows/molecule.yml)
![score](https://img.shields.io/ansible/quality/60363)

Install Git on BSD/Linux machines with Ansible.

## Setup

Run `ansible-galaxy install charlesrocket.git` or use `requirements.yml`:

```
roles:
  - name: charlesrocket.dotfiles
```

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
