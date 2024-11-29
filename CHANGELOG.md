# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2024-01-09
### Added
- Future features planning in FUTURELOG.md
  - Command enhancements roadmap
  - Task organization features
  - Advanced features and integrations
  - Performance improvements planning
- Development dependencies for documentation generation (Sphinx)
- Build and publishing tools (twine, build) to dev dependencies
- Conventional Commits specification guide in README
- Comprehensive Sphinx documentation:
  - API documentation with sphinx-autoapi
  - Installation and usage guides
  - Development setup instructions
  - Contributing guidelines

### Changed
- Simplified project documentation structure:
  - CHANGELOG.md for tracking all changes
  - FUTURELOG.md for future planning
  - Removed redundant FEATURELOG.md
- Updated documentation in README.md and Sphinx docs to reflect two-file structure
- Improved source code documentation:
  - Enhanced docstrings with detailed descriptions
  - Added return type descriptions
  - Updated command list in main module
  - Improved code formatting

### Development
- Added separate docs dependencies group in pyproject.toml
- Added Sphinx documentation build configuration
- Improved development setup with clear documentation

## [0.1.1] - 2024-11-29
### Changed
- Updated project homepage to GitHub Wiki
- Added TestPyPI package link to README
- Added roadmap.sh solution link to README and project metadata
- Package renamed to `quantuumhedgehog-task-cli` for PyPI compatibility

## [0.1.0] - 2024-11-29
### Added
- Initial release of Task CLI
- Core task management functionality:
  - Adding tasks
  - Listing tasks
  - Updating task status
  - Editing task descriptions
  - Removing tasks
- Command-line interface implementation
- JSON-based data storage
- Package structure and configuration

### Documentation
- Comprehensive README.md with:
  - Installation instructions
  - Usage examples
  - Development setup guide
  - Added rm/remove command documentation
- Project documentation:
  - CHANGELOG.md for version history
  - FUTURELOG.md for planned features

### Development
- Project setup and configuration:
  - pyproject.toml for package management
  - Development dependencies
- Testing implementation:
  - unittest-based tests
  - pytest-based tests
  - Two testing approaches demonstration
- GitHub release configuration with:
  - Source distribution (tar.gz)
  - Python wheel package (whl)

[Unreleased]: https://github.com/quantuumhedgehog/roadmaps-python-task-tracker/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/quantuumhedgehog/roadmaps-python-task-tracker/compare/v0.1.0-66f3ac06...v0.1.1
[0.1.0]: https://github.com/quantuumhedgehog/roadmaps-python-task-tracker/releases/tag/v0.1.0-66f3ac06
