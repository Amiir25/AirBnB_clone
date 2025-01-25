#!/usr/bin/python3

"""
This module provides a unit test for the `HBNBCommand` class of
`console.py` module.

"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.user import User
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    """Test class for the HBNBCommand console."""

    def setUp(self):
        """Set up test cases and reset storage."""

        storage.reset()  # a reset method from storage to clear objects.

    def test_quit(self):
        """Test `quit` command exits the console."""

        with patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """Test EOF exits the console."""

        with patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))
            self.assertEqual(output.getvalue(), "\n")

    def test_emptyline(self):
        """Test empty line does nothing."""

        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual(output.getvalue(), "")

    def test_create(self):
        """Test `create` command for new object creation."""

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            obj_id = output.getvalue().strip()
            self.assertIn(f"User.{obj_id}", storage.all())

    def test_create_invalid_class(self):
        """Test `create` with an invalid class name."""

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create InvalidClass")
            self.assertEqual(output.getvalue().strip(),
                             "** class doesn't exist **")

    def test_show(self):
        """Test `show` command to display an object."""

        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(f"show User {user.id}")
            self.assertIn(str(user), output.getvalue().strip())

    def test_show_invalid_class(self):
        """Test `show` command with invalid class."""

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show InvalidClass 1234")
            self.assertEqual(output.getvalue().strip(),
                             "** class doesn't exist **")

    def test_show_invalid_id(self):
        """Test `show` command with invalid ID."""

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show User 1234")
            self.assertEqual(output.getvalue().strip(),
                             "** no instance found **")

    def test_destroy(self):
        """Test `destroy` command."""

        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(f"destroy User {user.id}")
            self.assertNotIn(f"User.{user.id}", storage.all())

    def test_all(self):
        """Test `all` command for listing all objects."""

        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all")
            self.assertIn(str(user), output.getvalue().strip())

    def test_all_class_filter(self):
        """Test `all` command with a specific class."""

        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all User")
            self.assertIn(str(user), output.getvalue().strip())

    def test_count(self):
        """Test `count` command to count objects of a class."""

        User()
        User().save()
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual(output.getvalue().strip(), "2")

    def test_update(self):
        """Test `update` command with individual attribute."""

        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(f'update User {user.id} name "Test"')
            self.assertEqual(user.name, "Test")

    def test_update_dict(self):
        """Test `update` command with dictionary."""

        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(
                f'update User {user.id} {{"name": "Test", "age": 30}}'
            )
            self.assertEqual(user.name, "Test")
            self.assertEqual(user.age, 30)

    def test_invalid_update(self):
        """Test `update` with invalid attribute."""

        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(f"update User {user.id}")
            self.assertEqual(
                output.getvalue().strip(), "** attribute name missing **"
            )


if __name__ == "__main__":
    unittest.main()
