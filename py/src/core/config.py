import json
import cx_Oracle
from pathlib import Path


class ConfigLoader:
    # LOAD JSON DATA
    with open(str(Path(__file__).parent.absolute()) + "/data/config.json") as file:
        data: dict[str, str] = json.load(file)

    # INIT ORACLE LIB
    cx_Oracle.init_oracle_client(data["oracle_dir"])

    def __new__(cls, *args, **kwargs) -> None:
        if cls is ConfigLoader:
            raise TypeError("ConfigLoader cannot be instantiated!")

    @staticmethod
    def get_oracle_dir()->str:
        return ConfigLoader.data.get('oracle_dir')

    @staticmethod
    def get_db_user()->str:
        return ConfigLoader.data.get('db_user')

    @staticmethod
    def get_db_pwd()->str:
        return ConfigLoader.data.get('db_pwd')

    @staticmethod
    def get_db_url()->str:
        return ConfigLoader.data.get('db_url')

    @staticmethod
    def get_db_encoding()->str:
        return ConfigLoader.data.get('db_encoding')