# Changelog

All notable changes to this project will be documented in this file.

## [1.3.3] - 2023-12-09

### Bug Fixes

- Rename internal variables

### CI/CD

- Use `ansible-lint`

### Miscellaneous tasks

- Bump ansible version
- Bump ansible to 2.15.0
- Switch ansible to 2.14.0

## [1.3.2] - 2023-12-07

### Bug Fixes

- Ignore `tempfile` changes

### CI/CD

- Move `docsite`
- Fix `cd` syntax
- Rename `docs`
- Fix `docsite`

### Documentation

- Fix alternative link
- Change to code attribute
- Update short description
- Link alternative

### Miscellaneous tasks

- Update `antsibull-docs`
- Fix linter

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

### CI/CD

- Fix `lint`
- Update `checkout`
- Disable fail-fast

### Documentation

- Fix galaxy badge
- Fix galaxy badge link
- Add `remote_vars`
- Fix host key description

### Miscellaneous tasks

- Update dev dependencies

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

### CI/CD

- Add pr labeler

### Miscellaneous tasks

- Add pr template
- Use `molecule-plugins`
- Add ansible config

### Testing

- Downgrade molecule

## [1.2.2] - 2023-04-14

### Bug Fixes

- Improve error handling

### CI/CD

- Add codecov config

### Documentation

- Add attributes

### Miscellaneous tasks

- Fix test name
- Drop `display`

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

### CI/CD

- Perform integration testing
- Drop defaults

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

### Testing

- Add integration tests

## [1.1.0] - 2023-04-02

### CI/CD

- Deploy docsite
- Move docsite tasks to `release`
- Don't execute linter during release
- Add `ansible-test` to release dependencies

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

### Styling

- Fix formatting
- Drop implicit octals

### Testing

- Update converge.yml

## [1.0.0] - 2023-03-28

### Molecule

- Add macos
- Drop macos

