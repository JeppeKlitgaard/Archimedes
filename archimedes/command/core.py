import importlib.util
import logging
import os
import sys
from pathlib import Path
from typing import Optional

from doit.cmd_help import Help as DoitHelp

from archimedes import ArchimedesSite
from archimedes.config import SiteConfig, ThemeConfig

logger = logging.getLogger(__name__)


def run_cli(args: Optional[list[str]] = None) -> None:
    """
    Runs Archimedes.
    """

    MARKER_FILE: str = "archi_config.py"

    if args is None:
        args = sys.argv[1:]

    # Go up until we find MARKER_FILE
    # MARKER_FILE is the tombstone that marks our project root, always.
    search_dir = Path(os.getcwd())
    logger.debug("Searching for '%s' in filetree, starting at: %s", MARKER_FILE, search_dir)
    while True:
        archi_path = search_dir / MARKER_FILE
        if archi_path.exists():
            break

        # If we have gone all the way to root and still not found it...
        if search_dir == search_dir.parent:
            print(
                f"Unable to find '{MARKER_FILE}' in file tree. "
                 "We are not in an Archimedes project folder!"
            )

            sys.exit(1)

        search_dir = search_dir.parent

    base_dir = archi_path.parent
    config_file = (base_dir / MARKER_FILE).absolute()
    logger.info("Found project root at: %s", base_dir)
    logger.debug("Loading configuration file: %s", config_file)


    import_spec = importlib.util.spec_from_file_location(
        "user_site_config", config_file
    )
    user_site_config_module = importlib.util.module_from_spec(import_spec)
    import_spec.loader.exec_module(user_site_config_module)  # type: ignore

    # We have now resolved site_config
    site_config = SiteConfig(user_config=user_site_config_module)
    logger.debug("User site config: \n%s", SiteConfig)

    # Set up site
    site = ArchimedesSite(site_config=site_config)
    # doit_site = DoitArchimedes(site)

    import pdb

    pdb.set_trace()


class CommandHelp(DoitHelp):  # type: ignore
    """
    Display help dialog.
    """

    @staticmethod
    def print_usage(cmds: str) -> None:
        ...
