import sys
from app.commands import Command


class DiscordCommand(Command):
    def execute(self, args=None):
        print(f'I WIll send something to discord')