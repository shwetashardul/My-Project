from app.commands import Command


class GreetCommand(Command):
    def execute(self, args=None):
        print("Hello, World!")