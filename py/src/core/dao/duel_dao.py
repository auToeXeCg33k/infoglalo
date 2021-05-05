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
        # TODO DOESNT CHECK FOR NULL WINNER, BUT STILL WORKS, INTERESTING ANOMALY
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


    def delete_duel(this, challenger: str, challenged:str, pending: int) -> None:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM PARBAJ WHERE PENDING = :1 AND ID IN(\
                            SELECT PARBAJRAHIV.ID FROM PARBAJRAHIV INNER JOIN PARBAJRAHIVOTT ON PARBAJRAHIV.ID = PARBAJRAHIVOTT.ID\
                            WHERE PARBAJRAHIVOTT.JATEKOS = :2 AND PARBAJRAHIV.JATEKOS = :3)", [pending, challenged, challenger])
            connection.commit()

        except Exception as e:
            print(e)


    def accept_duel(this, challenger: str, challenged: str) -> None:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("UPDATE PARBAJ SET PENDING = 0 WHERE ID = (\
                            SELECT PARBAJRAHIV.ID FROM PARBAJRAHIV\
                            INNER JOIN PARBAJRAHIVOTT ON PARBAJRAHIV.ID = PARBAJRAHIVOTT.ID\
                            WHERE PARBAJRAHIV.JATEKOS = :1 AND PARBAJRAHIVOTT.JATEKOS = :2 AND PENDING = 1)", [challenger, challenged])
            connection.commit()

        except Exception as e:
            print(e)


    def get_accepted_duel(this, challenger: str, challenged: str) -> dict:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT PARBAJ.ID, PARBAJKERDESE.SZOVEG, KERDES.BETUJEL  FROM PARBAJ\
                            INNER JOIN PARBAJKERDESE ON PARBAJ.ID = PARBAJKERDESE.ID\
                            INNER JOIN PARBAJRAHIV ON PARBAJ.ID = PARBAJRAHIV.ID\
                            INNER JOIN PARBAJRAHIVOTT ON PARBAJ.ID = PARBAJRAHIVOTT.ID\
                            INNER JOIN KERDES ON PARBAJKERDESE.SZOVEG = KERDES.SZOVEG\
                            WHERE PARBAJRAHIV.JATEKOS = :1 AND PARBAJRAHIVOTT.JATEKOS = :2 AND PARBAJ.PENDING = 0 AND PARBAJ.NYERTES IS NULL", [challenger, challenged])

            data = cursor.fetchone()
            ret = {"id": data[0], "question": data[1], "correct_ans": data[2]}

            cursor.execute("SELECT BETUJEL, SZOVEG FROM VALASZ WHERE KERDESSZOVEG = :1", [ret["question"]])
            ret["answers"] = cursor.fetchall()

            return ret

        except Exception as e:
            print(e)
            return dict()