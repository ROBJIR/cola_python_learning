import sqlite3


class Model:
    _table = ""
    _fields = []

    def __init__(self, **kwargs):
        for field in self._fields:
            setattr(self, field, kwargs.get(field))
        self.id = kwargs.get("id")

    @classmethod
    def _connect(cls):
        return sqlite3.connect("databaza.db")

    @classmethod
    def create_table(cls):
        conn = cls._connect()
        cols = ", ".join(f"{f} TEXT" for f in cls._fields)
        conn.execute(
            f"CREATE TABLE IF NOT EXISTS {cls._table} "
            f"(id INTEGER PRIMARY KEY AUTOINCREMENT, {cols})"
        )
        conn.commit()
        conn.close()

    def save(self):
        conn = self._connect()
        cols = ", ".join(self._fields)
        placeholders = ", ".join("?" for _ in self._fields)
        values = tuple(getattr(self, f) for f in self._fields)
        conn.execute(
            f"INSERT INTO {self._table} ({cols}) VALUES ({placeholders})", values
        )
        conn.commit()
        conn.close()

    @classmethod
    def all(cls):
        conn = cls._connect()
        rows = conn.execute(f"SELECT * FROM {cls._table}").fetchall()
        conn.close()
        col_names = ["id"] + cls._fields
        return [cls(**dict(zip(col_names, row))) for row in rows]

    def __repr__(self):
        attrs = " ".join(f"{f}={getattr(self, f)!r}" for f in self._fields)
        return f"<{self.__class__.__name__} id={self.id} {attrs}>"


class User(Model):
    _table = "users"
    _fields = ["name", "age"]


if __name__ == "__main__":
    User.create_table()

    User(name="Adam", age=25).save()
    User(name="Peter", age=30).save()
    User(name="Jana", age=22).save()

    for user in User.all():
        print(user)
        print(user.name, user.age)
