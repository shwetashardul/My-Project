"""Module for testing command functionalities in the application."""
import pytest
#import sys
from app import App
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

def test_greet_command(capfd):
    """Test that the GreetCommand prints the expected greeting."""
    command = GreetCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"

def test_goodbye_command(capfd):
    """Test that the GoodbyeCommand prints the message."""
    command = GoodbyeCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "Goodbye\n", "The GoodbyeCommand should print 'Goodbye''"

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

'''def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'menu' command and lists all commands."""
    # Simulate user entering 'menu' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()

    out, _ = capfd.readouterr()
    
    # Verify that the output contains the names of registered commands
    expected_commands = ["greet", "goodbye", "exit", "menu", "discord", "add", "subtract", "multiply", "divide"]
    for command in expected_commands:
        assert command in out, f"The command '{command}' should be listed by the 'menu' command"

''''''def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'menu' command and lists all commands."""
    # Simulate user entering 'menu' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Mock sys.exit so it doesn't actually exit
    monkeypatch.setattr(sys, 'exit', lambda x: None)

    app = App()
    app.start()

    out, _ = capfd.readouterr()
    # Now you can make your assertions without being interrupted by SystemExit
    assert "Available commands:" in out
    # Add more assertions as needed'''


def test_add_command(capfd):
    """Test that the REPL correctly handles the 'add' command."""
    command = AddCommand()
    command.execute("3 4")
    out, _ = capfd.readouterr()
    assert out.strip() == "3.0 + 4.0 = 7.0", "The AddCommand should correctly add two numbers"

def test_subtract_command(capfd):
    """Test that the REPL correctly handles the 'subtract' command."""
    command = SubtractCommand()
    command.execute("10 4")
    out, _ = capfd.readouterr()
    assert out.strip() == "10.0 - 4.0 = 6.0", "The SubtractCommand should correctly subtract two numbers"

def test_multiply_command(capfd):
    """Test that the REPL correctly handles the 'multiply' command."""
    command = MultiplyCommand()
    command.execute("2 5")
    out, _ = capfd.readouterr()
    assert out.strip() == "2.0 * 5.0 = 10.0", "The MultiplyCommand should correctly multiply two numbers"

def test_divide_command(capfd):
    """Test that the REPL correctly handles the 'divide' command."""
    command = DivideCommand()
    command.execute("8 2")
    out, _ = capfd.readouterr()
    assert out.strip() == "8.0 / 2.0 = 4.0", "The DivideCommand should correctly divide two numbers"

def test_divide_by_zero_command(capfd):
    """Test that the REPL correctly handles the 'divide by zero' command."""
    command = DivideCommand()
    command.execute("8 0")
    out, _ = capfd.readouterr()
    assert "Error" in out, "The DivideCommand should handle division by zero with an error message"
