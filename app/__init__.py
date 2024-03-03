'''from app.commands import CommandHandler


class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()


    def start(self):
        # Register commands here
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand())
        self.command_handler.register_command("discord", DiscordCommand())
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())

        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            input_command = input(">>> ").strip()  # Read the command input
            command_parts = input_command.split(maxsplit=1)  # Split into command and arguments
            command_name = command_parts[0]  # The command itself
            args = command_parts[1] if len(command_parts) > 1 else ""  # Arguments, if any

            # Execute the command with the provided arguments
            if command_name in self.command_handler.commands:
                self.command_handler.execute_command(command_name, args)
            else:
                print(f"No such command: {command_name}")'''
            
import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

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
        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())
            command_parts = input_command.split(maxsplit=1)  # Split into command and arguments
            command_name = command_parts[0]  # The command itself
            args = command_parts[1] if len(command_parts) > 1 else ""  # Arguments, if any



