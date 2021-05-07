from ..config import ConfigLoader


class StatDAO:
    def get_age_stat(this):
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT FELHASZNALONEV,ROUND((SYSDATE-JATEKOS.szuldatum)/365) as age FROM JATEKOS")
            result: list[tuple] = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)

            if len(result) == 0:
                return None
            else:
                return result

        except Exception as e:
            print(e)
            return None
