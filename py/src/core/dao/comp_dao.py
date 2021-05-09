import cx_Oracle
from core.config import ConfigLoader

class CompDAO:
    def get_all_comp(this, uname) -> list[tuple]:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM VERSENY WHERE ID NOT IN (SELECT VERSENYID FROM UTKOZETRESZVETEL WHERE FELHASZNALONEV=:1)",[uname])
            db_data: list[tuple] = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)
            result = list()

            for id, name in db_data:
                result.append((id, name))

            return result
        except Exception as e:
            print(e)
        return list()

    def get_my_comp(this, uname:str) -> list[tuple]:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM VERSENY WHERE ID IN (SELECT VERSENYID FROM UTKOZETRESZVETEL WHERE FELHASZNALONEV=:1)",[uname])
            db_data: list[tuple] = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)
            result = list()

            for id, name in db_data:
                result.append((id, name))

            return result
        except Exception as e:
            print(e)
        return list()

    def get_number(this, r_id):
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT BESTOF FROM FORDULO WHERE VERSENYID=:1",[r_id])
            db_data: list[tuple] = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)

            return db_data[0][0]
        except Exception as e:
            print(e)
        return 0


    def get_new_id(this):
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT max(ID)+1 FROM VERSENY")
            db_data: list[tuple[int, str]] = cursor.fetchall()
            if db_data[0][0] is None:
                return 1
            ConfigLoader.get_connection_pool().release(connection)
            result = list()
            for v_id in db_data:
                result.append((v_id))
            return result[0][0]
        except Exception as e:
            print(e)
        return -1

    def new_comp(this,r_id, r_name, r_date, r_best) -> bool:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("INSERT into VERSENY values (:1, :2)", [r_id, r_name])
            connection.commit()
            cursor.execute("INSERT into FORDULO values (:1, to_date(:2, 'yyyy-mm-dd'), :3)",[r_id, r_date, int(r_best)])
            connection.commit()
            ConfigLoader.get_connection_pool().release(connection)
            return True

        except Exception as e:
            print(e)
            return False


    def get_play(this, uname:str) -> list[tuple]:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("select VERSENY.NEV, UTKOZET.KEZDES FROM VERSENY, UTKOZET WHERE VERSENY.ID = UTKOZET.VERSENYID AND UTKOZET.FELHASZNALONEV = :1",[uname])
            db_data: list[tuple] = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)
            result = list()

            for id, name in db_data:
                result.append((id, name))

            return result
        except Exception as e:
            print(e)
        return list()

    def get_comp_id(this, r_name):
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT ID FROM VERSENY WHERE NEV = :1",[r_name])
            db_data: list[tuple] = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)
            result = list()

            for id in db_data:
                result.append(id)

            return result
        except Exception as e:
            print(e)
        return list()

    def join_comp(this,r_id, r_name) -> bool:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("INSERT into UTKOZETRESZVETEL values (:1, :2)", [r_id, r_name])
            connection.commit()
            ConfigLoader.get_connection_pool().release(connection)
            return True

        except Exception as e:
            print(e)
            return False

    def join_play(this,r_id, r_name, r_date) -> bool:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("INSERT into UTKOZET values (:1, TO_DATE(:2, 'YYYY-MM-DD-HH24:MI:SS'),:3)", [r_id, r_date, r_name])
            connection.commit()
            ConfigLoader.get_connection_pool().release(connection)
            return True

        except Exception as e:
            print(e)
            return False

    def run_comp(this, r_id):
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT count(*) FROM UTKOZET WHERE VERSENYID=:1",[r_id])
            db_data: list[tuple] = cursor.fetchall()
            db = db_data[0][0]
            ConfigLoader.get_connection_pool().release(connection)
            print(db_data)
            return not (db==0)
        except Exception as e:
            print(e)
        return False


    def get_free_space(this, r_id):
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM UTKOZETRESZVETEL WHERE VERSENYID = :1",[r_id])
            db_data: list[tuple] = cursor.fetchall()
            ossz = list()
            for s in db_data:
                ossz.append(s)

            cursor.execute("SELECT BESTOF FROM FORDULO WHERE VERSENYID = :1",[r_id])
            db_data: list[tuple] = cursor.fetchall()
            bof = list()
            for s in db_data:
                bof.append(s)

            ConfigLoader.get_connection_pool().release(connection)
            free = bof[0][0]-ossz[0][0]
            return free
        except Exception as e:
            print(e)
        return list()


    def is_playing(this, r_id, r_name):
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT count(*) FROM UTKOZET WHERE VERSENYID=:1 AND FELHASZNALONEV = :2",[r_id, r_name])
            db_data: list[tuple] = cursor.fetchall()
            ossz = list()
            for s in db_data:
                ossz.append(s)
            ConfigLoader.get_connection_pool().release(connection)
            return not (ossz[0][0] == 0)
        except Exception as e:
            print(e)
        return False

    def get_players(this, r_id):
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM UTKOZETRESZVETEL WHERE VERSENYID=:1",[r_id])
            db_data: list[tuple] = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)
            result = list()

            for (id, name) in db_data:
                result.append((id, name))

            return result
        except Exception as e:
            print(e)
        return list()

    def delete_comp(this,r_id) -> bool:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM UTKOZETRESZVETEL WHERE VERSENYID = :1", [r_id])
            connection.commit()
            ConfigLoader.get_connection_pool().release(connection)
            return True

        except Exception as e:
            print(e)
            return False

    def delete_utkozet(this, r_id, r_name):
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM UTKOZET WHERE VERSENYID = :1 AND FELHASZNALONEV = :2", [r_id, r_name])
            connection.commit()
            ConfigLoader.get_connection_pool().release(connection)
            return True

        except Exception as e:
            print(e)
            return False

    def delete_reszvetel(this, r_id, r_name):
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM UTKOZETRESZVETEL WHERE VERSENYID = :1 AND FELHASZNALONEV = :2", [r_id, r_name])
            connection.commit()
            ConfigLoader.get_connection_pool().release(connection)
            return True

        except Exception as e:
            print(e)
            return False

    def get_random_question(this, r_id):
        try:
            ret = dict()
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT SZOVEG, BETUJEL FROM KERDES ORDER BY DBMS_RANDOM.RANDOM")
            db_data: list[tuple] = cursor.fetchall()
            ques = list()

            for (szoveg, jel) in db_data:
                ques.append((szoveg, jel))
                break

            cursor.execute("INSERT INTO UTKOZETKERDESE VALUES (:1,:2)",[r_id, ques[0][0]])
            connection.commit()

            cursor.execute("SELECT szoveg FROM VALASZ WHERE KERDESSZOVEG = :1 AND BETUJEL = :2 ORDER BY BETUJEL ASC", [ques[0][0], ques[0][1]])
            r_ans = cursor.fetchall()

            ret={"szoveg":ques[0][0],
                 "jel":ques[0][1],
                 "comp_id":r_id,
                 "ans":r_ans
                 }

            cursor.execute("SELECT BETUJEL, SZOVEG FROM VALASZ WHERE KERDESSZOVEG = :1 ORDER BY BETUJEL ASC", [ques[0][0]])
            ret["answers"] = cursor.fetchall()

            ConfigLoader.get_connection_pool().release(connection)
            return ret
        except Exception as e:
            print(e)
        return dict()

    def add_answer(this,r_kerdes, r_name, r_adott,r_jel) -> bool:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("INSERT into ADOTTVALASZ values (-1, :1,:2,:3,:4)", [r_jel, r_kerdes, r_name,r_adott])
            connection.commit()
            ConfigLoader.get_connection_pool().release(connection)
            return True

        except Exception as e:
            print(e)
            return False