import cx_Oracle

from src.core.config import ConfigLoader

from typing import Union


class UserDAO:
    def insert(self, uname, email, pwdhash, salt) -> bool:
        try:
            with cx_Oracle.connect(ConfigLoader.get_db_user(), ConfigLoader.get_db_pwd(), ConfigLoader.get_db_url(), encoding=ConfigLoader.get_db_encoding()) as connection:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO JATEKOS(FELHASZNALONEV, EMAIL, ADMIN, JELSZO, PONTSZAM, SALT) VALUES (:1, :2, :3, :4, :5, :6)", [uname, email, False, pwdhash, 0, salt])
                return True

        except Exception as e:
            print(e)
            return False


    def get(self, uname) -> Union[tuple[str, str,str, str, bool, int], None]:
        try:
            with cx_Oracle.connect(ConfigLoader.get_db_user(), ConfigLoader.get_db_pwd(), ConfigLoader.get_db_url(), encoding=ConfigLoader.get_db_encoding()) as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT FELHASZNALONEV, EMAIL, JELSZO, SALT, ADMIN, PONTSZAM  FROM JATEKOS WHERE FELHASZNALONEV = :1", [uname])
                result: list[tuple] = cursor.fetchall()

                if len(result) == 0:
                    return None
                else:
                    return result[0]

        except Exception as e:
            print(e)
            return None