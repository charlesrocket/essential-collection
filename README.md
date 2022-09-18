# dotfiles_role
[![Ansible Role](https://img.shields.io/ansible/role/47410)](https://galaxy.ansible.com/charlesrocket/dotfiles)
[![molecule](https://github.com/charlesrocket/dotfiles_role/actions/workflows/molecule.yml/badge.svg?branch=master&event=push)](https://github.com/charlesrocket/dotfiles_role/actions/workflows/molecule.yml)
![score](https://img.shields.io/ansible/quality/47410)

Deploy dotfiles from git repositories

#### Requirements
`git` on managed machines

### Install

`requirements.yml`:

```
roles:
  - name: charlesrocket.dotfiles
```

##### Example

```
- name: Playbook
  hosts: all

  roles:
    - {role: charlesrocket.dotfiles}
```

### Set variables
##### Example

```
dotfiles_repo: "https://github.com/charlesrocket/dotfiles.git" # dotfiles
dotfiles_repo_version: openbsd # branch to track
dotfiles_repo_accept_hostkey: false # StrictHostKeyChecking
dotfiles_repo_force: false # force git clone
dotfiles_repo_local_destination: "~/git/dotfiles" # local repo path
dotfiles_home: "~" # local dotfiles path
dotfiles_files: # files to track
  - .config/mc/ini
  - .zshrc
```
