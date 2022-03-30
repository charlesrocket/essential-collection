# dotfiles_role
[![molecule](https://github.com/charlesrocket/dotfiles_role/actions/workflows/molecule.yml/badge.svg?branch=master&event=push)](https://github.com/charlesrocket/dotfiles_role/actions/workflows/molecule.yml)
[![ansible lint](https://github.com/charlesrocket/dotfiles_role/actions/workflows/ansible-lint.yml/badge.svg?branch=master&event=push)](https://github.com/charlesrocket/dotfiles_role/actions/workflows/ansible-lint.yml)

Deploy dotfiles from git repositories

## Install
```
- name: Playbook
  hosts: all

  roles:
    - {role: charlesrocket.dotfiles}
```

## Set variables
```
dotfiles_repo: "https://github.com/charlesrocket/dotfiles.git"
dotfiles_repo_version: openbsd # branch option
dotfiles_repo_accept_hostkey: false
dotfiles_repo_permissions: true # +x for scripts
dotfiles_repo_local_destination: "~/git/dotfiles"
dotfiles_home: "~"
dotfiles_files:
  - .config/mc/ini
  - .zshrc
```
