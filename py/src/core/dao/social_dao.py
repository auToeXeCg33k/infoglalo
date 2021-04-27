import cx_Oracle
from src.core.config import ConfigLoader

class SocialDAO:
    def get_messages(this,room:int) -> list[tuple[str, int, cx_Oracle.Date, str]]:
        try:
            with cx_Oracle.connect(ConfigLoader.get_db_user(), ConfigLoader.get_db_pwd(), ConfigLoader.get_db_url(), encoding=ConfigLoader.get_db_encoding()) as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM UZENET WHERE KOZOSSEG = :1",[room])
                db_data: list[tuple[str, int, cx_Oracle.Date, str]] = cursor.fetchall()
                result = list()

                for u_name, r_room, date, content in db_data:
                    result.append((u_name, r_room, date, content))

                return result
        except Exception as e:
            print(e)
        return list()

    def get_room(this) -> list[tuple[int, str]]:
        try:
            with cx_Oracle.connect(ConfigLoader.get_db_user(), ConfigLoader.get_db_pwd(), ConfigLoader.get_db_url(), encoding=ConfigLoader.get_db_encoding()) as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM KOZOSSEG")
                db_data: list[tuple[int, str]] = cursor.fetchall()
                result = list()
                for room_id, room_name in db_data:
                    result.append((room_id, room_name))
                return result
        except Exception as e:
            print(e)
        return list()