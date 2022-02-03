from peewee import SqliteDatabase, Model, CharField, ForeignKeyField, DateField

db = SqliteDatabase('highfive.db', pragmas={'foreign_keys': 1})


class BaseModel(Model):
    class Meta:
        database = db


class Flair(BaseModel):
    id = CharField()
    base_text = CharField()


class User(BaseModel):
    username = CharField(primary_key=True)
    flair = ForeignKeyField(Flair, backref="users")


class Thread(BaseModel):
    id = CharField()
    posted = DateField()


class Checkin(BaseModel):
    user = ForeignKeyField(User, backref="checkins")
    thread = ForeignKeyField(Thread, backref="checkins")
    text = CharField()


if __name__ == "__main__":
    db.connect()
    db.create_tables([Flair, User, Thread, Checkin])
