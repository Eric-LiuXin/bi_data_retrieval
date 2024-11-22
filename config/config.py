import os
from pathlib import Path
from configparser import ConfigParser

from util.singleton import Singleton, singleton_object
from util.enums import ConfigOptionType


@singleton_object
class Config(metaclass=Singleton):
    def __init__(self):
        _current = Path(os.path.dirname(os.path.abspath(__file__)))
        _cfg = _current / "config.ini"

        self.__conf = ConfigParser()
        if _cfg.exists():
            self.__conf.read(os.path.normpath(_cfg))

    def get_section(self, section: str) -> dict:
        return dict(self.__conf[section]) if section in self.__conf else {}

    def get_options(
        self,
        section: str,
        option: str,
        option_type: ConfigOptionType = ConfigOptionType.STRING,
        fallback=None,
    ) -> any:
        match option_type:
            case ConfigOptionType.INT:
                res = self.__conf.getint(section, option, fallback=fallback)
            case ConfigOptionType.FLOAT:
                res = self.__conf.getfloat(section, option, fallback=fallback)
            case ConfigOptionType.BOOLEAN:
                res = self.__conf.getboolean(section, option, fallback=fallback)
            case _:
                res = self.__conf.get(section, option, fallback=fallback)

        return res
