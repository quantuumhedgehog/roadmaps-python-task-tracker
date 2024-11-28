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
        Literal["add", "list", "edit", "rm", "remove", "mark-todo", "mark-progress", "mark-done"] | AnyStr | None
)


def ticket_print(tasklist: list):
    """

    Args:
        tasklist (list): List of tasks.
    """
    for task in tasklist:
        print(
                f"#Task {task.id}:\t{task.description}\n"
                f"Status:\t\t`{task.status}`\n"
                f"Created:\t{task.createdAt}\n"
                f"Updated:\t{task.updatedAt}\n"
        )


def usage_print():
    """ Prints usage information """
    print(f"Usage:\ttask-cli <command> [arguments]\nCommands:\t"
          f"{TaskerCommand.__args__[0].__args__}\nExample:\ttask-cli list todo")


def parse_arguments(line_input: list, tasker: Tasker = Tasker()):
    """Parse and execute CLI commands.

    Handles various command patterns:
    - list [status]
    - add <description>
    - edit <task_id> <description>
    - mark-todo/mark-progress/mark-done <task_id>

    Args:
        line_input (list): Command line arguments
        tasker (object): Tasker instance

    Returns:
        List[Task]: List of tasks after command execution
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