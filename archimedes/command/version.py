from doit.cmd_base import Command as DoitCommand

from archimedes.command import CommandPlugin


class CommandVersion(CommandPlugin):
    """
    Prints the Archimedes version.
    """

    doc_purpose: str
    doc_usage: str
    doc_description: str
