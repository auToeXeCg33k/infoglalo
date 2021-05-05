from src.core.config import ConfigLoader


class DuelDAO:
    def executesql(this, sql, args: list) -> list:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute(sql, args)
            ret = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)
            return ret

        except Exception as e:
            print(e)
            return list()


    def get_availables(this, uname: str) -> list[str]:
        # TODO POTENTIAL PLSQL
        return this.executesql("SELECT FELHASZNALONEV FROM JATEKOS \
                               WHERE FELHASZNALONEV != :1 AND FELHASZNALONEV NOT IN \
                               (SELECT JATEKOS FROM PARBAJRAHIVOTT WHERE ID IN \
                               (SELECT ID FROM PARBAJRAHIV WHERE JATEKOS = :1)) \
                               AND FELHASZNALONEV NOT IN \
                               (SELECT JATEKOS FROM PARBAJRAHIV WHERE ID IN \
                               (SELECT ID FROM PARBAJRAHIVOTT WHERE JATEKOS = :1))", [uname])

    def get_incoming(this, uname: str) -> list[str]:
        return this.executesql("SELECT PARBAJRAHIV.JATEKOS FROM PARBAJRAHIV \
                               INNER JOIN PARBAJRAHIVOTT ON PARBAJRAHIV.ID = PARBAJRAHIVOTT.ID \
                               INNER JOIN PARBAJ ON PARBAJ.ID = PARBAJRAHIV.ID \
                               WHERE PENDING = 1 AND PARBAJRAHIVOTT.JATEKOS = :1", [uname])

    def get_requested(this, uname: str) -> list[str]:
        return this.executesql("SELECT PARBAJRAHIVOTT.JATEKOS FROM PARBAJRAHIV \
                               INNER JOIN PARBAJRAHIVOTT ON PARBAJRAHIV.ID = PARBAJRAHIVOTT.ID \
                               INNER JOIN PARBAJ ON PARBAJ.ID = PARBAJRAHIV.ID \
                               WHERE PENDING = 1 AND PARBAJRAHIV.JATEKOS = :1", [uname])


    def create_new_duel(self, challenger: str, challenged: str) -> None:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.callproc("ADD_PARBAJ", [challenger, challenged])
            connection.commit()

        except Exception as e:
            print(e)