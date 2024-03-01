"""Tests for the app module."""
import pytest
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    """Test app starts and exits correctly."""
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit
    out, _ = capfd.readouterr()
    assert "Type 'exit' to exit." in out

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    
    with pytest.raises(SystemExit) as excinfo:
        app.start()
    
    # Optionally, check for specific exit code or message
    # assert excinfo.value.code == expected_exit_code
    
    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out
