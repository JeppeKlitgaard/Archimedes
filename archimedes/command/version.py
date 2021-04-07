from archimedes.command.base import CommandPlugin


class CommandVersion(CommandPlugin):
    """
    Prints the Archimedes version.
    """

    doc_purpose: str
    doc_usage: str
    doc_description: str
