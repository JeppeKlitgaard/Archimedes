import importlib.util
import logging
import os
import sys
from pathlib import Path
from typing import Optional

from doit.cmd_help import Help as DoitHelp

from archimedes import ArchimedesSite
from archimedes.config import SiteConfig

logger = logging.getLogger(__name__)


def run_cli(args: Optional[list[str]] = None) -> None:
    """
    Runs Archimedes.
    """

    MARKER_FILE: str = "archi_config.py"
    project_active: bool

    # We want to make as much of the CLI available as possible even when
    # we are not in a project folder.
    # the ArchimedesSite.project_active flag marks whether the project
    # has been activated or not.
    # If True we are in an Archimedean project
    # If False the ArchimedeanSite has been instanciated using
    # default values and should not be considered an active site.

    if args is None:
        args = sys.argv[1:]

    # Go up until we find MARKER_FILE
    # MARKER_FILE is the tombstone that marks our project root, always.
    search_dir = Path(os.getcwd())
    logger.debug(
        "Searching for '%s' in filetree, starting at: %s", MARKER_FILE, search_dir
    )
    while True:
        archi_path = search_dir / MARKER_FILE
        if archi_path.exists():
            project_active = True
            break

        # If we have gone all the way to root and still not found it...
        if search_dir == search_dir.parent:
            project_active = False
            break

        search_dir = search_dir.parent

    logger.debug("Site project active: %s", project_active)

    site_config: SiteConfig
    # Project active, load the user_config file
    if project_active:
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

    # Project inactive, load default config for the purposes of
    # setting up an ArchimedesSite
    # This ArchimedesSite is should only be used for providing as much
    # of the CLI as possible
    else:
        logger.info(
            "Site is marked as inactive, "
            "instanciate with default configuration to provide CLI."
        )

        site_config = SiteConfig()

    # Set up site
    site = ArchimedesSite(  # noqa  assigned not used
        site_config=site_config, project_active=project_active
    )
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
