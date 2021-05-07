from ..config import ConfigLoader


class TestDAO():
    def get_categories(this) -> list[str]:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT NEV FROM TEMAKOR WHERE NEV != 'IQ' ORDER BY NEV")
            res = cursor.fetchall()
            return [row[0] for row in res]

        except Exception as e:
            print(e)


    def get_question_series(this, difficulty: int, category: str, amount: int) -> list[dict]:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute('''SELECT * FROM
                            (SELECT KERDES.SZOVEG, KERDES.BETUJEL FROM KERDES
                            WHERE TEMAKOR = :1 AND NEHEZSEG = :2
                            ORDER BY DBMS_RANDOM.VALUE)
                            WHERE ROWNUM <= :1
                            ''', [category, difficulty, amount])

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


    def add_answer(this, uname: str, question: str, answer_letter: str, answer_text: str) -> None:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO ADOTTVALASZ(id, valaszjel, KERDESSZOVEG, VALASZADO, VALASZSZOVEG)
                                VALUES(-1, :1, :2, :3, :4)''', [answer_letter, question, uname, answer_text])

            connection.commit()

        except Exception as e:
            print(e)