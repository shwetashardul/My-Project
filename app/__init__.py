import pkgutil
import importlib
#import os
#import importlib
#from pathlib import Path
from app.commands import CommandHandler
from app.commands import Command
from app.plugins.menu import MenuCommand

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    '''def load_internal_plugins(self, start_dir='app/plugins'):
        base_dir = os.path.dirname(__file__)
        start_path = Path(base_dir) / start_dir
        for root, dirs, files in os.walk(start_path):
            if '__init__.py' in files:
                relative_path = Path(root).relative_to(base_dir)
                module_path = str(relative_path).replace(os.sep, '.')
                module = importlib.import_module(module_path)
                self.register_plugin_commands(module)

    def register_plugin_commands(self, module):
        for item_name in dir(module):
            item = getattr(module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                command_name = item_name.lower()  # Simplified example
                self.command_handler.register_command(command_name, item())

    def start(self):
        self.load_internal_plugins()'''
    
    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore
    def start(self):
        # Register commands here
        self.load_plugins()
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))
        print("Type 'menu' to display available commands. \nType 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            input_command = input(">>> ").strip()  # Read the command input
            command_parts = input_command.split(maxsplit=1)  # Split into command and arguments
            command_name = command_parts[0]  # The command itself
            args = command_parts[1] if len(command_parts) > 1 else ""  # Arguments, if any

            # Execute the command with the provided arguments
            if command_name in self.command_handler.commands:
                self.command_handler.execute_command(command_name, args)
            else:
                print(f"No such command: {command_name}")
            


