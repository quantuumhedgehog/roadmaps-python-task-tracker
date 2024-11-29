# Task Tracker CLI

A robust command-line task management application built in Python that helps you organize and track your tasks efficiently.

> This is an implementation of the [Task Tracker Project](https://roadmap.sh/projects/task-tracker) from roadmap.sh.  
> View my solution: [roadmap.sh/projects/task-tracker/solutions?u=66f3ac06c45e253cb03d158d](https://roadmap.sh/projects/task-tracker/solutions?u=66f3ac06c45e253cb03d158d)

📦 **Package**: [TestPyPI](https://test.pypi.org/project/quantuumhedgehog-task-cli/) | [GitHub Wiki](https://github.com/quantuumhedgehog/roadmaps-python-task-tracker/wiki)

## 📋 Table of Contents
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Development](#-development)
- [Data Storage](#-data-storage)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)
- [Version History](#-version-history)

## ✨ Features

- **Task Management**
  - Create tasks with descriptions
  - List all tasks or filter by status
  - Update task descriptions
  - Mark tasks as todo/in-progress/done

- **Data Persistence**
  - Automatic JSON storage
  - Timestamps for creation and updates
  - Data integrity checks

## 🔧 Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

## 🚀 Installation

### From TestPyPI

```bash
pip install -i https://test.pypi.org/simple/ quantuumhedgehog-task-cli
```

### From Source

1. Clone the repository:
```bash
git clone https://github.com/quantuumhedgehog/roadmaps-python-task-tracker.git
cd roadmaps-python-task-tracker
```

2. Install in development mode:
```bash
# Install with development dependencies
pip install -e ".[dev]"

# Or install just the application
pip install -e .
```

### Via pip (when published)

```bash
pip install task-tracker-cli
```

### Build from Source

```bash
# Install build dependencies
pip install build

# Build the package
python -m build

# Install the built package
pip install dist/task_cli-0.1.0-py3-none-any.whl
```

## 💻 Usage

The `task-cli` command provides several subcommands for task management:

### Task Creation
```bash
# Add a new task
task-cli add "Complete the project documentation"
```

### Task Listing
```bash
# List all tasks
task-cli list

# List tasks by status
task-cli list todo
task-cli list in-progress
task-cli list done
```

### Task Updates
```bash
# Edit task description
task-cli edit <task-id> "Updated task description"

# Update task status
task-cli mark-todo <task-id>
task-cli mark-progress <task-id>
task-cli mark-done <task-id>

# Remove a task
task-cli rm <task-id>      # or
task-cli remove <task-id>  # alternative command
```

## 🛠 Development

### Testing

The project includes two testing implementations to demonstrate different Python testing approaches:

#### Using unittest
The `unittest` implementation follows Python's built-in testing framework approach:
```bash
# Run unittest tests
python -m unittest tests/test_task_cli_unittests.py -v
```

Key features:
- Uses Python's standard library testing framework
- Class-based test organization
- Built-in assertion methods
- Test discovery and execution

#### Using pytest
The `pytest` implementation offers a more modern and feature-rich testing approach:
```bash
# Run basic tests
pytest tests/test_task_cli_pytest.py -v

# Run tests with coverage report
pytest tests/test_task_cli_pytest.py -v --cov=src/task_cli

# Generate HTML coverage report
pytest tests/test_task_cli_pytest.py --cov=src/task_cli --cov-report=html
```

Key features:
- Fixtures for better test setup and teardown
- Powerful assertion introspection
- Built-in parameterization
- Rich plugin ecosystem
- Coverage reporting

### Project Structure

```
task-tracker-cli/                   # Root project directory
├── src/                            # Source code directory
│   └── task_cli/                   # Main package directory
│       ├── __init__.py             # Package initialization
│       ├── __main__.py             # Entry point for CLI
│       └── task_cli.py             # Core implementation
├── tests/                          # Test files directory
│   ├── test_task_cli_pytest.py     # Pytest test suite
│   └── test_task_cli_unittests.py  # Unittest test suite
├── README.md                       # Project documentation
└── pyproject.toml                  # Project metadata and dependencies
```

## 🗄️ Data Storage

The application uses a simple JSON file to store tasks, ensuring data persistence between sessions. The storage mechanism includes automatic file creation, data validation, and error handling.

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Commit Conventions

We follow [Conventional Commits](https://www.conventionalcommits.org/) specification. Each commit message should be structured as follows:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

#### Types
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, semicolons, etc)
- `refactor`: Code changes that neither fix bugs nor add features
- `test`: Adding or modifying tests
- `build`: Changes affecting build system or dependencies
- `ci`: Changes to CI configuration files and scripts
- `chore`: Other changes that don't modify src or test files

#### Examples
```bash
feat: add task priority feature
fix(parser): handle empty task descriptions
docs: update installation instructions
build(deps): add sphinx for documentation
test: add unit tests for task deletion
```

#### Breaking Changes
For breaking changes, add a `!` after the type/scope or add `BREAKING CHANGE` in the footer:
```bash
feat!: change task storage format
feat(api)!: remove deprecated endpoints

feat: allow provided config object

BREAKING CHANGE: `config` key in API response has been renamed to `settings`
```

### Getting Started
1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/roadmaps-python-task-tracker.git`
3. Create a feature branch: `git checkout -b feature-name`
4. Make your changes
5. Push to your fork: `git push origin feature-name`
6. Open a Pull Request

### What to Work On
- Check our [Issues](https://github.com/quantuumhedgehog/roadmaps-python-task-tracker/issues) page for open tasks
- See [FUTURELOG.md](FUTURELOG.md) for planned features
- Look for issues tagged with `good first issue` if you're new
- Feel free to suggest new features!

### Guidelines
- Follow the existing code style
- Add tests for new features
- Update documentation as needed
- Keep commits focused and write clear commit messages
- Reference issues in your pull request

### Development Setup
Follow the [Development](#-development) section above to set up your environment.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

This project is prepared within the [Python Developer](https://roadmap.sh/python) path on [Roadmap.sh](https://roadmap.sh/).

Documentation and unit tests improvements were generated with assistance from [Codeium AI](https://codeium.com/).

## 📝 Version History

We maintain two logs to track project evolution:

### Changelog

The `CHANGELOG.md` file tracks all notable changes to the project:
- Breaking changes
- New features
- Bug fixes
- Documentation updates
- Dependency updates

View the [full changelog](CHANGELOG.md).

### Future Planning

The `FUTURELOG.md` file outlines future development plans:
- Planned features and enhancements
- Architectural improvements
- Performance optimizations
- Integration possibilities

This helps us maintain a clear vision for future development.