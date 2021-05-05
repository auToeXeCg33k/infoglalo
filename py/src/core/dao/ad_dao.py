import cx_Oracle
from src.core.config import ConfigLoader
from PIL import ImageTk, Image
import io


class AdDAO:
    #TODO: str (or smth) to blob problem

    def input_type_handler(this, cursor, value, numElements):
        print(type(value))
        if value == cx_Oracle.DB_TYPE_LONG_RAW:
            return cursor.var(cx_Oracle.DB_TYPE_BLOB, arraysize=cursor.arraysize)

    def insert(this, title: str, text: str, poster: Image) -> bool:
        output = io. BytesIO()
        poster.save(output, format="gif")
        poster_as_string = output.getvalue()

        try:
             connection = ConfigLoader.get_connection_pool().acquire()
             connection.inputtypehandler = this.input_type_handler
             cursor = connection.cursor()
             cursor.execute("INSERT INTO HIRDETES(CIM, SZOVEG, PLAKAT) VALUES (:1, :2, :3)", [title, text, poster_as_string])
             connection.commit()
             ConfigLoader.get_connection_pool().release(connection)
             return True

        except Exception as e:
             print(e)
             return False

    def delete(this, index: int) -> bool:
        pass

    def output_type_handler(this, cursor, name, default_type, size, precision, scale):
        if default_type == cx_Oracle.DB_TYPE_BLOB:
            return cursor.var(cx_Oracle.DB_TYPE_LONG_RAW, arraysize=cursor.arraysize)


    def find_all(this) -> list[tuple[str, str, ImageTk.PhotoImage]]:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            connection.outputtypehandler = this.output_type_handler
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM HIRDETES")

            db_data : list[tuple[int, str, str, str]] = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)
            ret = list()

            for db_id, title, text, image in db_data:
                ret.append((title, text, ImageTk.PhotoImage(data = image)))
            return ret


        except Exception as e:
            print(e)

        return list()