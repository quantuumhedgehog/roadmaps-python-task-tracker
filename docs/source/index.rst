Welcome to Task Tracker CLI's documentation!
=====================================

A robust command-line task management application built in Python.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   autoapi/index

Features
--------

- Create and manage tasks from command line
- Track task status (todo/in-progress/done)
- Persistent JSON storage
- Simple and intuitive interface

Version History
-------------

We maintain two logs to track project evolution:

Changelog
~~~~~~~~~

The ``CHANGELOG.md`` file tracks all notable changes to the project:

- Breaking changes
- New features
- Bug fixes
- Documentation updates
- Dependency updates

View the full changelog in our `GitHub repository <https://github.com/quantuumhedgehog/task-cli/blob/main/CHANGELOG.md>`_.

Future Planning
~~~~~~~~~~~~~

The ``FUTURELOG.md`` file outlines future development plans:

- Planned features and enhancements
- Architectural improvements
- Performance optimizations
- Integration possibilities

This helps us maintain a clear vision for future development.

Installation
-----------

The package is currently in development and not yet available on PyPI.
You can install it using one of the following methods:

From TestPyPI
~~~~~~~~~~~~

.. code-block:: bash

   pip install -i https://test.pypi.org/simple/ quantuumhedgehog-task-cli

From Source
~~~~~~~~~~

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/quantuumhedgehog/task-cli.git
      cd task-cli

2. Install in development mode:

   .. code-block:: bash

      pip install -e .

Quick Start
----------

Basic usage:

.. code-block:: bash

   # Add a new task
   task-cli add "Write documentation"

   # List all tasks
   task-cli list

   # Mark a task as done
   task-cli mark-done 1

   # Edit a task description
   task-cli edit 1 "Update documentation"

   # Remove a task
   task-cli remove 1

Development
----------

1. Install development dependencies:

   .. code-block:: bash

      pip install -e ".[dev,docs]"

2. Run tests:

   .. code-block:: bash

      pytest

Contributing
-----------

We follow the Conventional Commits specification for our commit messages:

- ``feat:`` for new features
- ``fix:`` for bug fixes
- ``docs:`` for documentation changes
- ``build:`` for build system updates
- ``chore:`` for maintenance tasks

When contributing:

1. Check ``FEATURELOG.md`` for planned features and current work
2. Update ``CHANGELOG.md`` with your changes
3. Follow our commit message conventions
4. Add tests for new features
5. Update documentation as needed

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
