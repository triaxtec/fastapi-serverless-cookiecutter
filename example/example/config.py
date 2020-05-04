import re
from getpass import getpass
from pathlib import Path
from typing import Dict, Optional, Any

from flex_config import AWSSource, EnvSource, FlexConfig, YAMLSource

_app_config: Optional[FlexConfig] = None
yaml_path = Path.cwd() / "config.yml"


default_config = {
    "env": "local",
}


def get_config(override: Dict[str, Any] = None, prompt_db_creds: bool = False) -> FlexConfig:
    """ Get the app config for this  """
    global _app_config

    if _app_config:
        return _app_config

    if not override:
        override = {}

    _app_config = FlexConfig()
    _app_config.load_sources([default_config, EnvSource("EXAMPLE_"), YAMLSource(yaml_path), override])

    env = _app_config["env"]
    if env != "local":
        _app_config.load_sources(AWSSource(f"example/{env}"))

    if prompt_db_creds:  # pragma: no cover
        username = input("Username: ")
        password = getpass()
        main_url = re.sub(
            r"(mysql\+pymysql://)\S+:\S+(@.*)", fr"\1{username}:{password}\2", _app_config["database_url"]
        )
        _app_config["database_url"] = main_url

    return _app_config
