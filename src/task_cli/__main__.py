"""Command-line interface entry point for task-cli.

This module provides the entry point for the command-line interface.
It processes command-line arguments and delegates to the appropriate
task management functions.

"""

import sys

from .task_cli import parse_arguments, Tasker, ticket_print, usage_print


def main():
    """Entry point for the CLI application.

    Process command-line arguments and execute task operations.
    Creates a Tasker instance and handles the command execution flow.

    Command Format:
        task-cli <command> [arguments]

    Available Commands:
        add <description>     Add a new task
        list [status]        List all tasks or filter by status
        edit <id> <desc>     Edit task description
        mark-todo <id>       Mark task as todo
        mark-progress <id>   Mark task as in progress
        mark-done <id>       Mark task as done
        rm/remove <id>       Remove a task
    """
    result = parse_arguments(sys.argv[1:])
    ticket_print(result)


if __name__ == "__main__":
    main()
