from doit.cmd_base import Command as DoitCommand, TaskLoader2
from doit.task import Task, dict_to_task

from archimedes import ArchimedesSite
from archimedes.plugin import BasePlugin
from archimedes.types import DoitConfigValue


class CommandPlugin(BasePlugin, DoitCommand):  # type: ignore
    doc_purpose: str
    doc_usage: str
    doc_description: str

    def __init__(self) -> None:
        BasePlugin.__init__(self)
        DoitCommand.__init__(self)

    def execute(self) -> None:
        ...


test_task = {
    "name": "test_task",
    "actions": ["echo hello world"],
    "doc": "sample doc",
}


class ArchimedesTaskLoader(TaskLoader2):  # type: ignore
    def __init__(self, site: ArchimedesSite):
        self.site = site

    def load_doit_config(self) -> dict[str, DoitConfigValue]:
        return {}

    def load_tasks(self, cmd: DoitCommand, pos_args: list[str]) -> list[Task]:
        return [dict_to_task(test_task)]

    def setup(self, opt_values: dict[str, str]) -> None:
        ...
