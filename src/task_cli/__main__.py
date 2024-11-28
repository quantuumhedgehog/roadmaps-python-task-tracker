"""Command-line interface entry point for task-cli.

This module provides the entry point for the command-line interface.
It processes command-line arguments and delegates to the appropriate
task management functions.

Example:
    task-cli add "New task"
    task-cli list
    task-cli mark-done 1
"""

import sys

from .task_cli import parse_arguments, Tasker, ticket_print, usage_print


def main():
    """Entry point for the CLI application.
    Process command-line arguments and execute task operations.

    This function creates a Tasker instance and processes command-line
    arguments to perform the requested task operations.

    Command Format:
        task-cli <command> [arguments]

    Available Commands:
        add <description>     Add a new task
        list [status]        List all tasks or filter by status
        edit <id> <desc>     Edit task description
        mark-todo <id>       Mark task as todo
        mark-progress <id>   Mark task as in progress
        mark-done <id>       Mark task as done
    """
    result = parse_arguments(sys.argv[1:])
    ticket_print(result)


if __name__ == "__main__":
    main()
