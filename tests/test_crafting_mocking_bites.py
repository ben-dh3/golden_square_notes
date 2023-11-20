import pytest
from unittest.mock import Mock
from lib.task_formatter import *

# test file must start with 'test_'... so that pytest can see it

# Delete the lines starting with `@pytest.mark.skip` one by one as you work through.


def test_set_up_blank_mock():
    # Uncomment and set up your mocks here
    fake_object = Mock()

    # Don't edit below
    assert fake_object is not None


def test_set_up_mock_with_methods():
    # Uncomment and set up your mocks here
    fake_object = Mock()
    fake_object.speak.return_value = "Meow, Jess"
    fake_object.count_ears.return_value = 2
    fake_object.count_legs.return_value = 4

    # Don't edit below
    assert fake_object.speak("Jess") == "Meow, Jess"
    assert fake_object.count_ears() == 2
    assert fake_object.count_legs() == 4


def test_assert_that_mock_was_called():
    fake_object = Mock()

    # Don't edit this next line
    fake_object.speak("Steve")

    # Write an assertion below that the method "speak" was called with
    # the argument "Steve"
    fake_object.speak.assert_called_with("Steve")



def test_creates_mock_for_specific_case():
    fake_diary = Mock()

    # Set up this mock to pass the tests below
    fake_diary.count_entries.return_value = 2

    # Don't edit below
    fake_diary.add(Mock())
    fake_diary.add(Mock())
    assert fake_diary.count_entries() == 2


# challenge crafting mocking bites

def test_creates_a_sophisticated_mock():
    # Uncomment and set up your mocks here
    task_list = Mock()
    task = Mock()

    task_list.list.return_value = [task]
    task_list.count.return_value = 1
    task_list.clear.return_value = "success"

    # Don't edit below
    task_list.add(task)
    assert task_list.list() == [task]
    assert task_list.count() == 1
    assert task_list.clear() == "success"

# challenge testing peer classes

def test_task_formatter():
    fake_task = Mock()
    fake_task.title = 'task title'
    fake_task.complete = True
    task_formatter = TaskFormatter(fake_task)
    result = task_formatter.format()
    assert result == '- [x] task title'

def test_task_incomplete():
    fake_task = Mock()
    fake_task.title = 'task title'
    fake_task.complete = False
    task_formatter = TaskFormatter(fake_task)
    result = task_formatter.format()
    assert result == '- [ ] task title'

