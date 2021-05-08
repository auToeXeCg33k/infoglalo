from ..config import ConfigLoader


class StatDAO:
    def get_age_stat(this):
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT ROUND((SYSDATE-JATEKOS.szuldatum)/365) as age FROM JATEKOS")
            result: list() = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)

            return result

        except Exception as e:
            print(e)
            return None

    def get_user_theme(this, user: str):
        pass
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT KERDES.TEMAKOR, COUNT(ADOTTVALASZ.ID) FROM ADOTTVALASZ INNER JOIN kerdes ON adottvalasz.kerdesszoveg = kerdes.szoveg WHERE ADOTTVALASZ.VALASZADO = :1 AND KERDES.BETUJEL = ADOTTVALASZ.VALASZJEL AND kerdes.temakor != 'IQ' GROUP BY KERDES.TEMAKOR", [user])
            result: list(tuple) = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)

            return result

        except Exception as e:
            print(e)
            return None
