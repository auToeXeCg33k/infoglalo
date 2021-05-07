import cx_Oracle

from src.core.config import ConfigLoader

from typing import Union


class UserDAO:
    def insert(self, uname: str, email: str, pwdhash: str, salt: str, birth_date: cx_Oracle.Date) -> bool:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO JATEKOS(FELHASZNALONEV, EMAIL, ADMIN, JELSZO, SALT, SZULDATUM) VALUES (:1, :2, :3, :4, :5, to_date(:6, 'yyyy-mm-dd'))", [uname, email, False, pwdhash, salt, birth_date])
            connection.commit()
            ConfigLoader.get_connection_pool().release(connection)
            return True

        except Exception as e:
            print(e)
            return False


    def get(self, uname: str) -> Union[tuple[str, str, str, str, bool, cx_Oracle.Date, int, int, int], None]:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT FELHASZNALONEV, EMAIL, JELSZO, SALT, ADMIN, SZULDATUM, KONNYUPONT, KOZEPESPONT, NEHEZPONT  FROM JATEKOS WHERE FELHASZNALONEV = :1", [uname])
            result: list[tuple] = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)

            if len(result) == 0:
                return None
            else:
                return result[0]

        except Exception as e:
            print(e)
            return None

    def get_all(self):
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT FELHASZNALONEV FROM JATEKOS")
            result: list[tuple] = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)

            return result


        except Exception as e:
            print(e)
            return None