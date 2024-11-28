"""Unittest test suite for task_cli module."""

import json
import os
import tempfile
import unittest
from pathlib import Path

from src.task_cli.tasker import Task, Tasker
from src.task_cli.task_cli import parse_arguments



class TestTasker(unittest.TestCase):
    """Test cases for Tasker class."""

    def setUp(self):
        """Set up test environment."""
        self.test_dir = tempfile.mkdtemp()
        self.test_file = Path(self.test_dir) / "test_tasks.json"
        with open(self.test_file, "w") as f:
            json.dump([], f)
        self.tasker = Tasker(str(self.test_file))

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        os.rmdir(self.test_dir)

    def test_read_tasks_empty(self):
        """Test reading tasks from empty file."""
        tasks = self.tasker.list_tasks()
        self.assertEqual(len(tasks), 0)

    def test_read_tasks_with_status_filter(self):
        """Test reading tasks with status filter."""
        # Add test tasks
        task1 = self.tasker.add_task("Test1")
        task2 = self.tasker.add_task("Test2")
        self.tasker.edit_task_status(task2.id, "done")

        # Test filtering
        todo_tasks = self.tasker.list_tasks("todo")
        done_tasks = self.tasker.list_tasks("done")

        self.assertEqual(len(todo_tasks), 1)
        self.assertEqual(len(done_tasks), 1)
        self.assertEqual(todo_tasks[0].description, "Test1")
        self.assertEqual(done_tasks[0].description, "Test2")

    def test_add_task(self):
        """Test adding a new task."""
        task = self.tasker.add_task("Test task")

        # Verify task was added
        tasks = self.tasker.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].description, "Test task")
        self.assertEqual(tasks[0].status, "todo")
        self.assertNotEqual(tasks[0].createdAt, "")
        self.assertNotEqual(tasks[0].updatedAt, "")

    def test_edit_task_description(self):
        """Test editing task description."""
        # Add initial task
        task = self.tasker.add_task("Original")

        # Edit description
        updated_task = self.tasker.edit_task_description(task.id, "Updated")

        # Verify changes
        self.assertEqual(updated_task.description, "Updated")
        self.assertNotEqual(updated_task.updatedAt, task.updatedAt)

    def test_edit_task_status(self):
        """Test editing task status."""
        # Add initial task
        task = self.tasker.add_task("Test task")

        # Change status
        updated_task = self.tasker.edit_task_status(task.id, "done")

        # Verify status change
        self.assertEqual(updated_task.status, "done")
        self.assertNotEqual(updated_task.updatedAt, task.updatedAt)

    def test_parse_arguments_add(self):
        """Test parsing add command."""
        # Create a new tasker with a temp file
        test_dir = tempfile.mkdtemp()
        test_file = Path(test_dir) / "test_tasks.json"
        with open(test_file, "w") as f:
            json.dump([], f)
        
        # Test add command
        tasks = parse_arguments(["add", "New task"], Tasker(str(test_file)))
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].description, "New task")

        # Cleanup
        if os.path.exists(test_file):
            os.remove(test_file)
        os.rmdir(test_dir)

    def test_parse_arguments_list(self):
        """Test parsing list command."""
        # Create a new tasker with a temp file
        test_dir = tempfile.mkdtemp()
        test_file = Path(test_dir) / "test_tasks.json"
        with open(test_file, "w") as f:
            json.dump([], f)
        
        tasker = Tasker(str(test_file))
        # Add test tasks
        task1 = tasker.add_task("Test1")
        task2 = tasker.add_task("Test2")
        tasker.edit_task_status(task2.id, "done")

        # Test list all
        result = parse_arguments(["list"], tasker)
        self.assertEqual(len(result), 2)

        # Test list with status
        result = parse_arguments(["list", "done"], tasker)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].status, "done")

        # Cleanup
        if os.path.exists(test_file):
            os.remove(test_file)
        os.rmdir(test_dir)

    def test_parse_arguments_edit(self):
        """Test parsing edit command."""
        # Add initial task
        task = self.tasker.add_task("Original")

        # Test edit
        tasks = parse_arguments(["edit", str(task.id), "Updated"])

        self.assertEqual(tasks[0].description, "Updated")

    def test_parse_arguments_mark_status(self):
        """Test parsing status marking commands."""
        # Add initial task
        task = self.tasker.add_task("Test task")

        # Test different status changes
        tasks = parse_arguments(["mark-progress", str(task.id)])
        self.assertEqual(tasks[0].status, "in-progress")

        tasks = parse_arguments(["mark-done", str(task.id)])
        self.assertEqual(tasks[0].status, "done")

        tasks = parse_arguments(["mark-todo", str(task.id)])
        self.assertEqual(tasks[0].status, "todo")

    def test_task_creation(self):
        """Test Task dataclass creation and defaults."""
        task = Task(id=1, description="Test")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Test")
        self.assertEqual(task.status, "todo")
        self.assertEqual(task.createdAt, "")
        self.assertIsNone(task.updatedAt)


if __name__ == "__main__":
    unittest.main()