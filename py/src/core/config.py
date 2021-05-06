import json
import cx_Oracle
from pathlib import Path

from typing import Union


class ConfigLoader:
    # LOAD JSON DATA
    with open(str(Path(__file__).parent.absolute()) + "/data/config.json", encoding="utf-8") as file:
        data_: dict[str, str] = json.load(file)

    # INIT ORACLE LIB
    cx_Oracle.init_oracle_client(data_["oracle_dir"])
    connection_pool_ = cx_Oracle.SessionPool(data_["db_user"], data_["db_pwd"], data_["db_url"], encoding=data_["db_encoding"])

    def __new__(cls, *args, **kwargs) -> None:
        if cls is ConfigLoader:
            raise TypeError("ConfigLoader cannot be instantiated!")

    @staticmethod
    def get_oracle_dir()->str:
        return ConfigLoader.data_.get('oracle_dir')

    @staticmethod
    def get_db_user()->str:
        return ConfigLoader.data_.get('db_user')

    @staticmethod
    def get_db_pwd()->str:
        return ConfigLoader.data_.get('db_pwd')

    @staticmethod
    def get_db_url()->str:
        return ConfigLoader.data_.get('db_url')

    @staticmethod
    def get_db_encoding()->str:
        return ConfigLoader.data_.get('db_encoding')

    @staticmethod
    def get_connection_pool():
        return ConfigLoader.connection_pool_

    @staticmethod
    def get(key: str) -> Union[str, None]:
        if key in ConfigLoader.data_:
            return ConfigLoader.data_[key]
        return None