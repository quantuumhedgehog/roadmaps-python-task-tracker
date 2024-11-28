"""Pytest test suite for task_cli module."""

import json

import pytest

from task_cli.task_cli import parse_arguments
from task_cli.tasker import Task, Tasker


# region Fixtures
@pytest.fixture
def test_file(tmp_path):
    """Create a temporary test file."""
    test_file = tmp_path / "test_tasks.json"
    with open(test_file, "w") as f: # Type: Any
        json.dump([], f)
    return test_file

@pytest.fixture
def tasker(test_file):
    """Create a Tasker instance with test file."""
    return Tasker(str(test_file))

@pytest.fixture
def populated_tasker(tasker):
    """Create a Tasker instance with some predefined tasks."""
    tasks = [
        tasker.add_task("Test1"),  # todo
        tasker.add_task("Test2"),  # will be done
        tasker.add_task("Test3"),  # will be in-progress
    ]
    tasker.edit_task_status(tasks[1].id, "done")
    tasker.edit_task_status(tasks[2].id, "in-progress")
    return tasker
# endregion

# region Task CRUD Tests
class TestTaskOperations:
    """Test basic CRUD operations for tasks."""
    
    def test_read_tasks_empty(self, tasker):
        """Test reading tasks from empty file."""
        tasks = tasker.list_tasks()
        assert len(tasks) == 0

    def test_read_tasks_with_status_filter(self, populated_tasker):
        """Test reading tasks with different status filters."""
        todo_tasks = populated_tasker.list_tasks("todo")
        in_progress_tasks = populated_tasker.list_tasks("in-progress")
        done_tasks = populated_tasker.list_tasks("done")

        assert len(todo_tasks) == 1
        assert len(in_progress_tasks) == 1
        assert len(done_tasks) == 1
        assert todo_tasks[0].description == "Test1"
        assert in_progress_tasks[0].description == "Test3"
        assert done_tasks[0].description == "Test2"

    def test_add_task(self, tasker):
        """Test adding a new task."""
        tasker.add_task("Test task")

        tasks = tasker.list_tasks()
        assert len(tasks) == 1
        assert tasks[0].description == "Test task"
        assert tasks[0].status == "todo"
        assert tasks[0].createdAt != ""
        assert tasks[0].updatedAt is None

    def test_edit_task_description(self, tasker):
        """Test editing task description."""
        task = tasker.add_task("Original")
        updated_task = tasker.edit_task_description(task.id, "Updated")
        
        assert updated_task.description == "Updated"
        assert updated_task.updatedAt != task.updatedAt

    def test_edit_nonexistent_task(self, tasker):
        """Test editing a task that doesn't exist."""
        with pytest.raises(ValueError):
            tasker.edit_task_description(999, "Updated")

class TestCommandParsing:
    """Test command-line argument parsing."""
    
    def test_parse_arguments_add(self, tasker):
        """Test parsing add command."""
        # Clear any existing tasks
        with open(tasker.db_file, 'w') as f:
            json.dump([], f)
            
        tasks = parse_arguments(["add", "New task"], tasker)
        assert len(tasks) == 1
        assert tasks[0].description == "New task"

    def test_parse_arguments_list(self, populated_tasker):
        """Test parsing list command with different filters."""
        # Test list all
        result = parse_arguments(["list"], populated_tasker)
        assert len(result) == 3

        # Test list with status
        result = parse_arguments(["list", "done"], populated_tasker)
        assert len(result) == 1
        assert result[0].status == "done"

    def test_parse_invalid_command(self, tasker):
        """Test parsing invalid command."""
        with pytest.raises(SystemExit, match='0'):
            parse_arguments(["invalid_command"], tasker)

    def test_parse_arguments_mark_status(self, tasker):
        """Test parsing status marking commands."""
        task = tasker.add_task("Test task")
        task_id = str(task.id)

        # Test all status transitions
        command_status_pairs = [
            (["mark-progress", task_id], "in-progress"),
            (["mark-done", task_id], "done"),
            (["mark-todo", task_id], "todo")
        ]

        for command, expected_status in command_status_pairs:
            tasks = parse_arguments(command, tasker)
            assert tasks[0].status == expected_status

# endregion

# region Task Status Tests
class TestTaskStatus:
    """Test task status operations."""
    
    def test_edit_task_status(self, tasker):
        """Test editing task status through different states."""
        task = tasker.add_task("Test task")
        
        # Test all status transitions
        statuses = ["in-progress", "done", "todo"]
        for status in statuses:
            updated_task = tasker.edit_task_status(task.id, status)
            assert updated_task.status == status
            assert updated_task.updatedAt != task.updatedAt

    def test_invalid_status(self, tasker):
        """Test setting an invalid status."""
        task = tasker.add_task("Test task")
        with pytest.raises(ValueError):
            tasker.edit_task_status(task.id, "invalid_status")
# endregion

# region Task Model Tests
def test_task_creation():
    """Test Task dataclass creation and defaults."""
    task = Task(id=1, description="Test")
    assert task.id == 1
    assert task.description == "Test"
    assert task.status == "todo"
    assert task.createdAt == ""
    assert task.updatedAt is None
# endregion