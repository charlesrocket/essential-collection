# Changelog

All notable changes to this project will be documented in this file.

## [1.5.1] - 2026-07-19

### Bug Fixes

- Accept key by default

### Documentation

- Add `Contributing`
- Update ci badges

### Operations

- Bump actions/checkout from 5 to 6
- Bump actions/deploy-pages from 4 to 5
- Bump actions/upload-pages-artifact from 4 to 5
- Bump actions/checkout from 6 to 7
- Update actions
- Remove docker jobs
- Move `galaxy` job

### Build

- Move repository
- Move issue tracker
- Ignore `.forgejo`

## [1.5.0] - 2025-10-24

### Features

- Add `dfs` support

### Miscellaneous tasks

- Update tags

### Operations

- Bump `ansible` to 13.0.0a1

### Testing

- Update bsd/linux case

## [1.4.2] - 2025-10-02

### Bug Fixes

- Fix helper conditional

### Operations

- Bump actions/checkout from 4 to 5
- Bump actions/upload-pages-artifact from 3 to 4
- Set permissions
- Bump actions/setup-python from 5 to 6
- Bump actions/labeler from 5 to 6

## [1.4.1] - 2025-07-21

### Bug Fixes

- Fix dry run
- Rename register

### Miscellaneous tasks

- Update LICENSE
- Ignore archives

### Operations

- Drop `vagrant`
- Fix `release`
- Fix `docsite`

## [1.4.0] - 2024-12-19

### Features

- Support local configs

### Miscellaneous tasks

- Update LICENSE
- Bump ansible to 2.17

### Operations

- Bump macos
- Bump fbsd version
- Update actions
- Update `labeler` config
- Fix docs permissions
- Use macos-12
- Build the collection
- Update test distros
- Switch to ubuntu-latest
- Configure dependabot
- Bump actions/deploy-pages from 1 to 4
- Bump actions/setup-python from 4 to 5

### Testing

- Fix network interfaces

## [1.3.3] - 2023-12-09

### Bug Fixes

- Rename internal variables

### Miscellaneous tasks

- Bump ansible version
- Bump ansible to 2.15.0
- Switch ansible to 2.14.0

### Operations

- Use `ansible-lint`

## [1.3.2] - 2023-12-07

### Bug Fixes

- Ignore `tempfile` changes

### Documentation

- Fix alternative link
- Change to code attribute
- Update short description
- Link alternative

### Miscellaneous tasks

- Update `antsibull-docs`
- Fix linter

### Operations

- Move `docsite`
- Fix `cd` syntax
- Rename `docs`
- Fix `docsite`

## [1.3.1] - 2023-12-06

### Bug Fixes

- Deprecate `remote_vars` module

### Documentation

- Add `fetch_vars` description

## [1.3.0] - 2023-12-05

### Bug Fixes

- Update plugin deprecation

### Documentation

- Fix deprecation message
- Fix description

### Features

- Deprecate `remote_vars`
- Add `fetch_vars` role

## [1.2.5] - 2023-10-03

### Documentation

- Fix galaxy badge
- Fix galaxy badge link
- Add `remote_vars`
- Fix host key description

### Miscellaneous tasks

- Update dev dependencies

### Operations

- Fix `lint`
- Update `checkout`
- Disable fail-fast

### Testing

- Set python interpreter
- Fix bsd scenarios (#3)

## [1.2.4] - 2023-06-07

### Documentation

- Update `remote_vars` description

### Miscellaneous tasks

- Use role prefix
- Update system variable

## [1.2.3] - 2023-05-01

### Bug Fixes

- Use `ansible_user` variable

### Miscellaneous tasks

- Add pr template
- Use `molecule-plugins`
- Add ansible config

### Operations

- Add pr labeler

### Testing

- Downgrade molecule

## [1.2.2] - 2023-04-14

### Bug Fixes

- Improve error handling

### Documentation

- Add attributes

### Miscellaneous tasks

- Fix test name
- Drop `display`

### Operations

- Add codecov config

### Testing

- Cover invalid inputs
- Rename test cases
- Check failed results
- Test empty files
- Test error 404

## [1.2.1] - 2023-04-12

### Documentation

- Update short descriptions

### Miscellaneous tasks

- Version bump
- Prepare for 1.2.1

### Testing

- Add test variables

## [1.2.0] - 2023-04-10

### Documentation

- Add codecov
- Improve `remote_vars` documentation

### Features

- Add `remote_vars` plugin
- Return downloaded variables

### Miscellaneous tasks

- Update README.md
- Version bump
- Fix header
- Version bump
- Prepare for 1.2.0

### Operations

- Perform integration testing
- Drop defaults

### Testing

- Add integration tests

## [1.1.0] - 2023-04-02

### Documentation

- Configure docsite
- Fix tarball filename
- Add documentation
- Edit `dotfiles_home`
- Drop smart quotes
- Add docsite link to Galaxy
- Update README.md
- Update docsite
- Update `dotfiles` variables

### Features

- Update defaults
- Add `accept_newhostkey`
- Drop `accept_hostkey`
- Don't rebuild helpers

### Miscellaneous tasks

- Version bump
- Update collection tags
- Update links

### Operations

- Deploy docsite
- Move docsite tasks to `release`
- Don't execute linter during release
- Add `ansible-test` to release dependencies

### Styling

- Fix formatting
- Drop implicit octals

### Testing

- Update converge.yml

## [1.0.0] - 2023-03-28

### Molecule

- Add macos
- Drop macos


