"""
Task CLI - A Command Line Task Management Tool.

This package provides a command-line interface for managing tasks. It allows users
to create, list, edit, and update the status of tasks, with persistent storage
in JSON format.

Main Features:
    - Create new tasks with descriptions
    - List all tasks or filter by status
    - Edit task descriptions
    - Update task status (todo/in-progress/done)
    - Persistent JSON storage
    - Task creation and update timestamps

For command-line usage, see README.md
"""

__version__ = "0.1.0"
__author__ = "@quantuumhedgehog"
__email__ = "lutso.mykhailo@gmail.com"

from .tasker import Tasker, Task
from .task_cli import parse_arguments, usage_print, ticket_print
__all__ = ["Tasker", "Task", "parse_arguments", "usage_print", "ticket_print"]