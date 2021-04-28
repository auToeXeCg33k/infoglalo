import cx_Oracle
from src.core.config import ConfigLoader

class SocialDAO:
    def get_messages(this,room:int) -> list[tuple[str, int, cx_Oracle.Date, str]]:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM UZENET WHERE KOZOSSEG = :1",[room])
            db_data: list[tuple[str, int, cx_Oracle.Date, str]] = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)
            result = list()

            for u_name, r_room, date, content in db_data:
                result.append((u_name, r_room, date, content))

            return result
        except Exception as e:
            print(e)
        return list()

    def get_room(this) -> list[tuple[int, str]]:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM KOZOSSEG")
            db_data: list[tuple[int, str]] = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)
            result = list()
            for room_id, room_name in db_data:
                result.append((room_id, room_name))
            return result
        except Exception as e:
            print(e)
        return list()

    def get_forum_messages(this) -> list[tuple[str, int, cx_Oracle.Date, str]]:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM UZENET WHERE KOZOSSEG = 0")
            db_data: list[tuple[str, int, cx_Oracle.Date, str]] = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)
            result = list()

            for u_name, r_room, date, content in db_data:
                result.append((u_name, r_room, date, content))

            return result
        except Exception as e:
            print(e)
        return list()

    def send_message(this, u_name, room_id, content) -> bool:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO UZENET(KULDO, KOZOSSEG, IDOPONT, SZOVEG) VALUES (:1, :2, SYSDATE, :3)", [u_name, room_id, content])
            ConfigLoader.get_connection_pool().release(connection)
            return True

        except Exception as e:
            print(e)
            return False