"""
Contains logic regarding the configuration of an Archimedes site.
"""
from __future__ import annotations

from pathlib import Path
from types import ModuleType
from typing import Any, Optional, Type, TypeVar

import toml
from pydantic import BaseSettings, FilePath

from archimedes.config import (
    default_config as default_config_mod,
    runtime_config as runtime_config_mod,
    user_config as user_config_mod,
)

SENTINEL = object()


# TOML Config

T = TypeVar("T", bound="TOMLConfig")


class TOMLConfig(BaseSettings):
    """
    Base Config Class that is used by TOML-Pydantic based configurations.

    Currently these are:
    - archi.toml
    - theme_config.toml
    """

    @classmethod
    def load(cls: Type[T], filepath: Path) -> T:
        """
        Loads a TOML Config file and parses it as a TOMLConfig.
        """
        with open(filepath, "r") as f:
            filestring = f.read()

        return cls.loads(filestring)

    @classmethod
    def loads(cls: Type[T], filestring: str) -> T:
        """
        Loads a TOML formatted config string and parses it as a TOMLConfig.
        """
        raw_dict = toml.loads(filestring)

        return cls.parse_obj(raw_dict)


class ThemeConfig(TOMLConfig):
    pass


class ArchiTOMLConfig(TOMLConfig):
    config_file: FilePath


# Site Config


class SiteConfig:
    """
    This contains the final, resolved site configuration.

    Essentially any configurations not found in the UserSiteConfig will be
    retrieved from the DefaultSiteConfig.

    ! Maybe remove runtime_config.
    ! Django seems to think this is a bad idea, and not sure how order
    ! would work or what a good usecase might be.

    Configuration inheritance (lowest = highest priority):
        1 - RuntimeSiteConfig
        2 - UserSiteConfig
        3 - DefaultSiteConfig
    """

    WHITELIST_ATTRS: list[str] = [
        "user_config",
        "default_config",
        "runtime_config",
    ]

    def __init__(
        self,
        user_config: Optional[ModuleType] = None,
        default_config: Optional[ModuleType] = None,
        runtime_config: Optional[ModuleType] = None,
    ) -> None:

        if user_config is None:
            self.user_config = user_config_mod
        else:
            self.user_config = user_config

        if default_config is None:
            self.default_config = default_config_mod
        else:
            self.default_config = default_config

        if runtime_config is None:
            self.runtime_config = runtime_config_mod
        else:
            self.runtime_config = runtime_config

    def __setattr__(self, setting: str, value: Any) -> None:
        if setting in self.WHITELIST_ATTRS:
            super().__setattr__(setting, value)
        else:
            setattr(self.runtime_config, setting, value)  # type: ignore

    def __getattribute__(self, setting: str) -> Any:
        # This is seems a bit iffy.
        # Essentially we need to explicitly evaluate the WHITELIST_ATTRS case
        # Then we bypass any WHITELIST_ATTRS as well such that we can
        # retrieve our configs

        if setting == "WHITELIST_ATTRS":
            return super().__getattribute__("WHITELIST_ATTRS")

        if setting in self.WHITELIST_ATTRS:
            return super().__getattribute__(setting)

        result = getattr(self.runtime_config, setting, SENTINEL)  # type: ignore
        # Setting was specified in runtime_config
        if result is not SENTINEL:
            return result

        result = getattr(self.user_config, setting, SENTINEL)  # type: ignore
        # Setting was specified in user_config, not in runtime_config
        if result is not SENTINEL:
            return result

        result = getattr(self.default_config, setting, SENTINEL)  # type: ignore
        # Setting was specified in default_config,
        # not in runtime_config, user_config
        if result is not SENTINEL:
            return result

        raise KeyError(f"No configuration option with the name '{setting}'")

    def is_overridden(self, setting: str) -> bool:
        return hasattr(self.user_config, setting)
