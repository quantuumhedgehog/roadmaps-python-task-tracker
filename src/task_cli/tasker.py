"""Task management implementation module.

This module provides the core functionality for the task-cli package.
It includes the Task dataclass for representing individual tasks and
the Tasker class for managing tasks.

Classes:
    Task: A dataclass representing a single task
    Tasker: The main task management class

Example:
    from tasker import Tasker
    tasker = Tasker()
    task = tasker.add_task("Write documentation")
    print(f"{task.id}: {task.description} ({task.status})")
    print(f"Created: {task.createdAt}")
    print(f"Updated: {task.updatedAt}")
"""

import json
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional

TaskStatus = Literal["todo", "in-progress", "done"] | None


@dataclass
class Task:
    """A class representing a single task.

    Attributes:
        id (int): Unique identifier for the task
        description (str): The task description
        status (str): Current status (todo/in-progress/done)
        createdAt (str): ISO format timestamp of creation
        updatedAt (Optional[str]): ISO format timestamp of last update, None if never updated
    """

    id: int
    description: str
    status: str = "todo"
    createdAt: str = ""
    updatedAt: Optional[str] = None


class Tasker:
    """Main task management class.

    This class provides methods for managing tasks, including creating,
    listing, editing, and updating task status. Tasks are persisted to
    a JSON file.

    Attributes:
        db_file (Path): Path to the JSON file storing tasks

    Example:
        tasker = Tasker("tasks.json")
        tasker.add_task("Complete the project")
        tasks = tasker.list_tasks("todo")
    """

    def __init__(self, tasks_file: str = "tasks.json"):
        """Initialize Tasker with a tasks file.

        Args:
            tasks_file (str, optional): Path to tasks JSON file.
                Defaults to "tasks.json".
        """
        self.db_file = self._get_db_file(tasks_file)
        self._ensure_tasks_file()

    @staticmethod
    def _get_timestamp() -> str:
        """Get current timestamp in ISO format.

        Returns:
            str: Current timestamp in ISO format
        """
        return datetime.now().isoformat()

    @staticmethod
    def _get_db_file(filename: str) -> Path:
        """Initialize and get the path to the tasks storage file.

        Creates the file if it doesn't exist, initializing it with an empty task list.

        Args:
            filename (str): Name of the tasks file

        Returns:
            Path: Path object pointing to the tasks file
        """
        tasks_file = Path.cwd().joinpath(filename)
        if not tasks_file.exists():
            with open(tasks_file, "w") as f:  # type: Any
                json.dump([], f)
        return tasks_file

    def _ensure_tasks_file(self) -> None:
        """Ensure tasks file exists, create if not."""
        if not self.db_file.exists():
            with open(self.db_file, "w") as f:  # type: Any
                json.dump([], f)

    def _save_tasks(self, tasks: List[Dict[str, Any]]) -> None:
        """Save tasks to file.

        Args:
            tasks (List[Dict[str, Any]]): List of task dictionaries
        """
        with self.db_file.open("w") as f:  # type: Any
            json.dump(tasks, f, indent=4)

    def _load_tasks(self) -> List[Dict[str, Any]]:
        """Load tasks from file.

        Returns:
            List[Dict[str, Any]]: List of task dictionaries
        """
        with self.db_file.open("r") as f:
            return json.load(f)

    def _get_next_id(self):
        """Generate the next available task ID.

        Returns:
            int: Next available ID (current maximum ID + 1)
        """
        tasks = self._load_tasks()
        return max([task["id"] for task in tasks], default=0) + 1

    def get_task(self, task_id):
        """Get task by id.

         Args:
             task_id (int): Id of task to retrieve

         Returns:
             Task: Selected task if found
         """
        tasks = self._load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                return Task(**task)
        raise ValueError(f"Task with id {task_id} not found")

    def add_task(self, description: str) -> Task:
        """Add a new task.

        Args:
            description (str): Task description

        Returns:
            Task: The newly created task
        """
        tasks = self._load_tasks()

        task = Task(
                id=self._get_next_id(),
                description=description,
                createdAt=self._get_timestamp(),
        )

        tasks.append(asdict(task))
        self._save_tasks(tasks)
        return task

    def list_tasks(self, status: Optional[str] = None) -> List[Task]:
        """List tasks, optionally filtered by status.

        Args:
            status (Optional[str], optional): Filter by status.
                Defaults to None.

        Returns:
            List[Task]: List of matching tasks
        """
        tasks = self._load_tasks()
        if status:
            tasks = [task for task in tasks if task["status"] == status]
        return [Task(**task) for task in tasks]

    def edit_task_description(self, task_id: int, new_description: str) -> Task:
        """Edit task description.

        Args:
            task_id (int): ID of task to edit
            new_description (str): New task description

        Returns:
            Task: Updated task

        Raises:
            ValueError: If task_id not found
        """
        tasks = self._load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                task["description"] = new_description
                task["updatedAt"] = self._get_timestamp()
                self._save_tasks(tasks)
                return Task(**task)
        raise ValueError(f"Task with id {task_id} not found")

    def edit_task_status(self, task_id: int, new_status: str) -> Task:
        """Update task status.

        Args:
            task_id (int): ID of task to update
            new_status (str): New status (todo/in-progress/done)

        Returns:
            Task: Updated task

        Raises:
            ValueError: If task_id not found or invalid status
        """
        if new_status not in ["todo", "in-progress", "done"]:
            raise ValueError("Status must be todo, in-progress, or done")

        tasks = self._load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = new_status
                task["updatedAt"] = self._get_timestamp()
                self._save_tasks(tasks)
                return Task(**task)
        raise ValueError(f"Task with id {task_id} not found")

    def remove_task(self, task_id: int) -> Task:
        """Update task status.

        Args:
            task_id (int): ID of task to be removed

        Returns:
            Task: Removed task

        Raises:
            ValueError: If task_id not found
        """

        tasks = self._load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                self._save_tasks(tasks)
                return Task(**task)
        raise ValueError(f"Task with id {task_id} not found")
