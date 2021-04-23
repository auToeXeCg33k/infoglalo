import cx_Oracle


class AdDAO:
    def __init__(this) -> None:
        cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_10")


    def find_all(this) -> list[tuple[str, str, cx_Oracle.BLOB]]:
        try:
            with cx_Oracle.connect("infoglalo", "jelszo", "leopph.tplinkdns.com/xe", encoding="UTF-8") as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM HIRDETES")
                return cursor.fetchall()

        except Exception as e:
            print(e)

        return list()