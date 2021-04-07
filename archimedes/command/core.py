import importlib
import logging
import os
import sys
from pathlib import Path
from typing import Optional

from doit.cmd_help import Help as DoitHelp

from archimedes import ArchimedesSite
from archimedes.config import ArchiTOMLConfig, SiteConfig

logger = logging.getLogger(__name__)


def run_cli(args: Optional[list[str]] = None):
    """
    Runs Archimedes.
    """
    if args is None:
        args = sys.argv[1:]

    # Go up until we find archi.toml
    # archi.toml is the tombstone that marks our project root, always
    search_dir = Path(os.getcwd())
    logger.debug("Searching for 'archi.toml' in filetree, starting at: %s", search_dir)
    while True:
        archi_path = search_dir / "archi.toml"
        if archi_path.exists():
            break

        # If we have gone all the way to root and still not found it...
        if search_dir == search_dir.parent:
            print(
                "Unable to find 'archi.toml' in file tree. "
                "We are not in an Archimedes project folder!"
            )

            sys.exit(1)

        search_dir = search_dir.parent

    base_dir = archi_path.parent
    logger.info("Found project root at: %s", base_dir / "archi.toml")

    os.chdir(base_dir)
    archi_config = ArchiTOMLConfig.load(base_dir / "archi.toml")
    logger.debug("Using archi.toml config: \n%s", archi_config)

    logger.info("Using site config from: %s", archi_config.config_file.absolute())
    import_spec = importlib.util.spec_from_file_location(
        "user_site_config", archi_config.config_file
    )
    user_site_config_module = importlib.util.module_from_spec(import_spec)
    import_spec.loader.exec_module(user_site_config_module)

    # We have now resolved site_config
    site_config = SiteConfig(user_config=user_site_config_module)
    logger.debug("User site config: \n%s", SiteConfig)

    # Set up site
    site = ArchimedesSite(archi_config=archi_config, site_config=site_config)
    # doit_site = DoitArchimedes(site)



class CommandHelp(DoitHelp):
    """
    Display help dialog.
    """

    @staticmethod
    def print_usage(cmds):
        ...
