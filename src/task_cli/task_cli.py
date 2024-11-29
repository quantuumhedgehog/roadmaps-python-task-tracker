"""Task management implementation module.

This module provides the core functionality for the task-cli package.
It includes the Task dataclass for representing individual tasks and
the Tasker class for managing tasks.

Classes:
    Task: A dataclass representing a single task
    Tasker: The main task management class

Example:
    python task_cli.py list
    python task_cli.py list todo
    python task_cli.py add "Task with description"
    python task_cli.py edit 1 "New description for task 1"
    python task_cli.py mark-progress 1
    python task_cli.py mark-done 1
    python task_cli.py mark-todo 1
    python task_cli.py rm 1

"""

import logging
import sys
from typing import AnyStr, Literal

from .tasker import Tasker

# Configure logging
logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

TaskerCommand = (
        Literal[
            "add", "list", "edit", "rm", "remove", "mark-todo", "mark-progress", "mark-done"
        ] | AnyStr | None
)


def ticket_print(tasklist: list):
    """Print task details in a formatted way.

    Displays each task's ID, description, status, creation time,
    and last update time in a readable format.

    Args:
        tasklist (list[Task]): List of Task objects to display.
    """
    for task in tasklist:
        print(
                f"#Task {task.id}:\t{task.description}\n"
                f"Status:\t\t`{task.status}`\n"
                f"Created:\t{task.createdAt}\n"
                f"Updated:\t{task.updatedAt}\n"
        )


def usage_print():
    """Print command-line usage information.

    Displays available commands, their arguments, and proper syntax.
    The output includes all valid TaskerCommand values.
    """
    print(
            f"Usage:\ttask-cli <command> [arguments]\n"
            f"Commands:\t{TaskerCommand.__args__[0].__args__}\n"
            f"Example:\ttask-cli list todo"
    )


def parse_arguments(line_input: list, tasker: Tasker = Tasker()):
    """Parse and execute CLI commands.

    Processes command line arguments and executes corresponding task operations.
    All operations are performed through the provided Tasker instance.

    Args:
        line_input (list): Command line arguments excluding program name.
            First argument should be a command, followed by its parameters.
        tasker (Tasker, optional): Tasker instance for task management.
            Defaults to a new Tasker instance.

    Returns:
        List[Task]: List of tasks after command execution.
            For 'list' commands, returns filtered tasks.
            For other commands, returns all tasks.
    """
    status_filter = None
    match line_input:
        case ["list"]:
            pass
        case ["list", status]:
            status_filter = status
        case ["add", description]:
            tasker.add_task(description)
        case ["edit", task_id, description]:
            tasker.edit_task_description(int(task_id), description)
        case ["mark-todo", task_id]:
            tasker.edit_task_status(int(task_id), "todo")
        case ["mark-progress", task_id]:
            tasker.edit_task_status(int(task_id), "in-progress")
        case ["mark-done", task_id]:
            tasker.edit_task_status(int(task_id), "done")
        case ["rm" | "remove", task_id]:
            tasker.remove_task(int(task_id))
        case _:
            usage_print()
            exit(0)
    return tasker.list_tasks(status_filter)


if __name__ == "__main__":
    tasks = parse_arguments(sys.argv[1:])
    print(*enumerate(tasks), sep='\n')
