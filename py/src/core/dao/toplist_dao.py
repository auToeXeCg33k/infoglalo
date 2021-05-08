import cx_Oracle

from core.config import ConfigLoader


class TopListDAO:
    # REPRODUCE PYTHON OBJECTS FROM PLSQL OBJECTS
    def object_repr(this, obj):
        if obj.type.iscollection:
            ret = list()
            for value in obj.aslist():
                if isinstance(value, cx_Oracle.Object):
                    value = this.object_repr(value)
                ret.append(value)
        else:
            ret = dict()
            for attr in obj.type.attributes:
                value = getattr(obj, attr.name)
                if value is None:
                    continue
                elif isinstance(value, cx_Oracle.Object):
                    value = this.object_repr(value)
                ret[attr.name] = value
        return ret


    # GET AGGREGATE SCORES
    def aggregate(this) -> list[dict[str, int]]:
        connection = ConfigLoader.get_connection_pool().acquire()

        try:
            return this.object_repr(connection.cursor().callfunc("aggregate_points", connection.gettype("AGGREGATE_TOPLIST_TABLE_T"), [0.5, 0.75, 1]))

        except Exception as e:
            print(e)
            return list()

        finally:
            ConfigLoader.get_connection_pool().release(connection)


    # GET EASY SCORES
    def easy(this) -> list[tuple[str, int]]:
        return this.query_categorized_points("KONNYUPONT")

    # GET MEDIUM POINTS
    def medium(this) -> list[tuple[str, int]]:
        return this.query_categorized_points("KOZEPESPONT")

    # GET HARD POINTS
    def hard(this) -> list[tuple[str, int]]:
        return this.query_categorized_points("NEHEZPONT")


    # QUERY HELPER
    def query_categorized_points(this, field_name: str) -> list[tuple[str, int]]:
        connection = ConfigLoader.get_connection_pool().acquire()

        try:
            cursor = connection.cursor()
            cursor.execute("SELECT FELHASZNALONEV, " + field_name + " FROM JATEKOS ORDER BY " + field_name + " DESC")
            return cursor.fetchall()

        except Exception as e:
            print(e)
            return list()

        finally:
            ConfigLoader.get_connection_pool().release(connection)