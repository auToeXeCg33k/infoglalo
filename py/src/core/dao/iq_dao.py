from ..config import ConfigLoader

class IQDAO:
    def get_questions(this) -> list[dict]:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT SZOVEG, BETUJEL FROM KERDES WHERE TEMAKOR = 'IQ' ORDER BY DBMS_RANDOM.VALUE")

            ret = list()
            for question in cursor.fetchall():
                ret.append(dict())
                ret[-1]["question"] = question[0]
                ret[-1]["correct_ans"] = question[1]

                cursor.execute('''SELECT SZOVEG, BETUJEL FROM VALASZ
                                            WHERE KERDESSZOVEG = :1
                                            ORDER BY BETUJEL''', [question[0]])

                ret[-1]["answers"] = list()
                for ans in cursor.fetchall():
                    ret[-1]["answers"].append((ans[1], ans[0]))

            return ret

        except Exception as e:
            print(e)
            return list()