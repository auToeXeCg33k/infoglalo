import cx_Oracle

from src.core.config import ConfigLoader


class TopListDAO:
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


    def aggregate(this) -> list[dict[str, int]]:
        try:
            with cx_Oracle.connect(ConfigLoader.get_db_user(), ConfigLoader.get_db_pwd(), ConfigLoader.get_db_url(), encoding=ConfigLoader.get_db_encoding()) as connection:
                return this.object_repr(connection.cursor().callfunc("aggregate_points", connection.gettype("AGGREGATE_TOPLIST_TABLE_T"), [0.1, 0.2, 0.3]))

        except Exception as e:
            print(e)
            return list()