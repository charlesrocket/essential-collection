# Changelog

All notable changes to this project will be documented in this file.

## [1.2.3] - 2023-05-01

### Bug Fixes

- Use `ansible_user` variable

### CI/CD

- Add pr labeler

### Miscellaneous tasks

- Add pr template
- Use `molecule-plugins`
- Add ansible config
- Version bump

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

- Version bump
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

