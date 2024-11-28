# Task Tracker CLI

A robust command-line task management application built in Python that helps you organize and track your tasks efficiently.

> This is an implementation of the [Task Tracker Project](https://roadmap.sh/projects/task-tracker) from roadmap.sh.

## 📋 Table of Contents
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Development](#-development)
- [Data Storage](#-data-storage)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

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

### From Source

1. Clone the repository:
```shell
git clone <repository-url>
cd roadmaps-python-task-tracker
```

2. Install in development mode:
```shell
# Install with development dependencies
pip install -e ".[dev]"

# Or install just the application
pip install -e .
```

### Via pip (when published)

```shell
pip install task-tracker-cli
```

### Build from Source

```shell
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
```shell
# Add a new task
task-cli add "Complete the project documentation"
```

### Task Listing
```shell
# List all tasks
task-cli list

# List tasks by status
task-cli list todo
task-cli list in-progress
task-cli list done
```

### Task Updates
```shell
# Edit task description
task-cli edit <task-id> "Updated task description"

# Update task status
task-cli mark-todo <task-id>
task-cli mark-progress <task-id>
task-cli mark-done <task-id>
```

## 🛠 Development

### Testing

The project includes two testing implementations to demonstrate different Python testing approaches:

#### Using unittest
The `unittest` implementation follows Python's built-in testing framework approach:
```shell
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
```shell
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
- Parallel test execution (with pytest-xdist)

### Project Structure

```
task-tracker-cli/           # Root project directory
├── src/                    # Source code directory
│   └── task_cli/          # Main package directory
│       ├── __init__.py    # Package initialization
│       ├── __main__.py    # Entry point for CLI
│       └── task_cli.py    # Core implementation
├── tests/                  # Test files directory
│   ├── test_task_cli_pytest.py  # Pytest test suite
│   └── test_task_cli_unittests.py  # Unittest test suite
├── README.md              # Project documentation
└── pyproject.toml         # Project metadata and dependencies
```

## 💾 Data Storage

Tasks are stored in a JSON file (`tasks.json` by default) with the following schema:

```json
[
    {
        "id": 1,
        "description": "Task description",
        "status": "todo",
        "createdAt": "2024-01-01T10:00:00",
        "updatedAt": "2024-01-01T10:30:00"
    }
]
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

This project is prepared within the [Python Developer](https://roadmap.sh/python) path on [Roadmap.sh](https://roadmap.sh/).

Documentation and unit tests improvements were generated with assistance from [Codeium AI](https://codeium.com/).