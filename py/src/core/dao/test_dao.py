from ..config import ConfigLoader


class TestDAO():
    def get_categories(this) -> list[str]:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM TEMAKOR ORDER BY NEV")
            res = cursor.fetchall()
            return [row[0] for row in res]

        except Exception as e:
            print(e)