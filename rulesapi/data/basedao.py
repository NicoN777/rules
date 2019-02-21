from conf import connection
import sqlite3


class Base:
    def read(self, sql, params):
        with connection as conn:
            rs = conn.execute(sql, params)
            return self.map(rs)

    def write(self, sql, params=None):
        with connection as conn:
            try:
                rs = conn.execute(sql, params)
                return rs.rowcount
            except Exception as e:
                raise sqlite3.DataError(str(e))

    def map(self, rs):
        return list(map(lambda x: str(x[0]).lower(), rs.description)), rs.fetchall()

    def query_for_object(self, mapper=None, sql=None, params={}):
        attrs, data = self.read(sql, params)
        if len(data) != 1:
            raise sqlite3.DataError(f'Result set returned {len(data)} rows.')
        record = data[0]
        obj = mapper()
        for index in range(len(data[0])):
            setattr(obj, mapper._fields[index], record[index])
        return obj

    def query_for_list(self, mapper=None, sql=None, params={}):
        attrs, data = self.read(sql, params)
        records = []
        for row in data:
            obj = mapper()
            for index in range(len(row)):
                setattr(obj, mapper._fields[index], row[index])
            records.append(obj)
        return records

    def update(self, mapper=None, sql=None, params={}):
        data = self.write(sql, params)
        return data
