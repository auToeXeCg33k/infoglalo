import cx_Oracle
from src.core.config import ConfigLoader


class DuelDAO:
    def executesql(this, sql, args: list) -> list:
        try:
            with cx_Oracle.connect(ConfigLoader.get_db_user(), ConfigLoader.get_db_pwd(), ConfigLoader.get_db_url(), encoding=ConfigLoader.get_db_encoding()) as connection:
                cursor = connection.cursor()
                cursor.execute(sql, args)
                return cursor.fetchall()

        except Exception as e:
            print(e)
            return list()


    def get_availables(this, uname: str) -> list:
        return this.executesql("SELECT FELHASZNALONEV FROM JATEKOS WHERE FELHASZNALONEV != :1 AND FELHASZNALONEV NOT IN \
                               (SELECT JATEKOS FROM PARBAJRAHIVOTT WHERE ID IN \
                               (SELECT ID FROM PARBAJRAHIV WHERE JATEKOS = :1))", [uname])

    def get_incoming(this, uname: str) -> list:
        return this.executesql("SELECT PARBAJRAHIV.JATEKOS, PARBAJRAHIVOTT.JATEKOS, PARBAJ.PENDING FROM PARBAJRAHIV \
                               INNER JOIN PARBAJRAHIVOTT ON PARBAJRAHIV.JATEKOS = PARBAJRAHIVOTT.JATEKOS \
                               INNER JOIN PARBAJ ON PARBAJ.ID = PARBAJRAHIV.ID \
                               WHERE PENDING = 1 AND PARBAJRAHIVOTT.JATEKOS = :1", [uname])

    def get_requested(this, uname: str) -> list:
        return this.executesql("SELECT PARBAJRAHIV.JATEKOS, PARBAJRAHIVOTT.JATEKOS, PARBAJ.PENDING FROM PARBAJRAHIV \
                               INNER JOIN PARBAJRAHIVOTT ON PARBAJRAHIV.JATEKOS = PARBAJRAHIVOTT.JATEKOS \
                               INNER JOIN PARBAJ ON PARBAJ.ID = PARBAJRAHIV.ID \
                               WHERE PENDING = 1 AND PARBAJRAHIV.JATEKOS = :1", [uname])