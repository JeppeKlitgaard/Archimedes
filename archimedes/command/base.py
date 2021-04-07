from doit.cmd_base import Command as DoitCommand

from archimedes.plugin import BasePlugin


class CommandPlugin(BasePlugin, DoitCommand):  # type: ignore
    doc_purpose: str
    doc_usage: str
    doc_description: str

    def __init__(self) -> None:
        BasePlugin.__init__(self)
        DoitCommand.__init__(self)

    def execute(self) -> None:
        ...
