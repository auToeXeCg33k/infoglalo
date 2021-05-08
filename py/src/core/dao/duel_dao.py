from core.config import ConfigLoader


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
        return this.executesql("SELECT FELHASZNALONEV FROM JATEKOS\
                                WHERE FELHASZNALONEV NOT IN\
                                (SELECT PARBAJRAHIV.JATEKOS FROM PARBAJ\
                                INNER JOIN PARBAJRAHIV ON PARBAJ.ID = PARBAJRAHIV.ID\
                                WHERE PARBAJ.PENDING = 1 OR PARBAJ.NYERTES IS NULL)\
                                AND FELHASZNALONEV NOT IN\
                                (SELECT PARBAJRAHIVOTT.JATEKOS FROM PARBAJ\
                                INNER JOIN PARBAJRAHIVOTT ON PARBAJ.ID = PARBAJRAHIVOTT.ID\
                                WHERE PARBAJ.PENDING = 1 OR PARBAJ.NYERTES IS NULL)\
                                AND FELHASZNALONEV != :1", [uname])

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

    def delete_duel_by_id(this, id: int) -> None:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM PARBAJ WHERE ID = :1", [id])
            connection.commit()

        except Exception as e:
            print(e)


    def accept_duel(this, challenger: str, challenged: str) -> None:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            # TODO UNIQUE?
            cursor.execute("UPDATE PARBAJ SET PENDING = 0 WHERE ID = (\
                            SELECT UNIQUE PARBAJRAHIV.ID FROM PARBAJRAHIV\
                            INNER JOIN PARBAJRAHIVOTT ON PARBAJRAHIV.ID = PARBAJRAHIVOTT.ID\
                            INNER JOIN PARBAJ ON PARBAJ.ID = PARBAJRAHIV.ID\
                            WHERE PARBAJRAHIV.JATEKOS = :1 AND PARBAJRAHIVOTT.JATEKOS = :2 AND PENDING = 1)", [challenger, challenged])
            connection.commit()

        except Exception as e:
            print(e)


    def get_unfinished_duel(this, challenger: str, challenged: str, pending: int) -> dict:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT PARBAJ.ID, PARBAJKERDESE.SZOVEG, KERDES.BETUJEL  FROM PARBAJ\
                            INNER JOIN PARBAJKERDESE ON PARBAJ.ID = PARBAJKERDESE.ID\
                            INNER JOIN PARBAJRAHIV ON PARBAJ.ID = PARBAJRAHIV.ID\
                            INNER JOIN PARBAJRAHIVOTT ON PARBAJ.ID = PARBAJRAHIVOTT.ID\
                            INNER JOIN KERDES ON PARBAJKERDESE.SZOVEG = KERDES.SZOVEG\
                            WHERE PARBAJRAHIV.JATEKOS = :1 AND PARBAJRAHIVOTT.JATEKOS = :2 AND PARBAJ.PENDING = :3 AND PARBAJ.NYERTES IS NULL", [challenger, challenged, pending])

            data = cursor.fetchone()
            ret = {"id": data[0], "question": data[1], "correct_ans": data[2]}

            cursor.execute("SELECT BETUJEL, SZOVEG FROM VALASZ WHERE KERDESSZOVEG = :1 ORDER BY BETUJEL ASC", [ret["question"]])
            ret["answers"] = cursor.fetchall()

            return ret

        except Exception as e:
            print(e)
            return dict()


    def set_winner(this, id: int, winner: str) -> None:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("UPDATE PARBAJ SET NYERTES = :1 WHERE ID = :2", [winner, id])
            connection.commit()

        except Exception as e:
            print(e)


    def add_answer(this, id: int, uname: str, ans: str) -> None:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO PARBAJVALASZ(parbajid, jatekos, valasz) VALUES (:1, :2, :3)", [id, uname, ans])
            connection.commit()

        except Exception as e:
            print(e)


    def has_both_answers(this, id: int) -> bool:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(parbajid) FROM PARBAJVALASZ WHERE parbajid = :1", [id])
            return cursor.fetchone()[0] == 2

        except Exception as e:
            print(e)
            return False


    def get_answer(this, id: int, uname: str) -> str:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT VALASZ FROM PARBAJVALASZ WHERE PARBAJID = :1 AND JATEKOS = :2", [id, uname])
            return cursor.fetchone()[0]

        except Exception as e:
            return ""