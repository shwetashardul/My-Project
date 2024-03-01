import pytest
from app import App
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

def test_greet_command(capfd):
    command = GreetCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"

def test_goodbye_command(capfd):
    command = GoodbyeCommand()
    command.execute()
    out, err = capfd.readouterr()
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

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_add_command(capfd):
    command = AddCommand()
    command.execute("3 4")
    out, err = capfd.readouterr()
    assert out.strip() == "3.0 + 4.0 = 7.0", "The AddCommand should correctly add two numbers"

def test_subtract_command(capfd):
    command = SubtractCommand()
    command.execute("10 4")
    out, err = capfd.readouterr()
    assert out.strip() == "10.0 - 4.0 = 6.0", "The SubtractCommand should correctly subtract two numbers"

def test_multiply_command(capfd):
    command = MultiplyCommand()
    command.execute("2 5")
    out, err = capfd.readouterr()
    assert out.strip() == "2.0 * 5.0 = 10.0", "The MultiplyCommand should correctly multiply two numbers"

def test_divide_command(capfd):
    command = DivideCommand()
    command.execute("8 2")
    out, err = capfd.readouterr()
    assert out.strip() == "8.0 / 2.0 = 4.0", "The DivideCommand should correctly divide two numbers"

def test_divide_by_zero_command(capfd):
    command = DivideCommand()
    command.execute("8 0")
    out, err = capfd.readouterr()
    assert "Error" in out, "The DivideCommand should handle division by zero with an error message"
