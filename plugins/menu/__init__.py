import sys
from app.commands import Command


class MenuCommand(Command):
    def execute(self, args=None):
        print(f'Menu')