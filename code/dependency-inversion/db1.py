class UserDB:
    def insert_user(self, user):
        pass

    def delete_user(self, user):
        pass

    def list_users(self):
        pass


# MySQL implementation
class MySQLUserDB(DB):
    def __init__(self):
        self.__connection = mysql.connect(...)

    def insert_user(self, user):
        self.__connection.execute(...)

    def delete_user(self, user):
        self.__connection.execute(...)

    def list_users(self):
        self.__connection.execute(...)


# Fake db for tests
class FakeUserDB(DB):
    def __init__(self):
        self.__users = {}

    def insert_user(self, user):
        self.__users[user.id] = user

    def delete_user(self, user):
        del self.__users[user.id]

    def list_users(self):
        return self.__users


class UserActions:
    def new_user(user, db):
        if is_valid(user):
            db.insert_user(user)

    def is_valid(user):
        return user.id and user.name


class UserActionsTest(unittest.TestCase):
    def test_new_user(self):
        db = FakeUserDB()
        user = User(id: 1, name: "John")
        new_user(user, db)
        self.assertEqual(1, len(db.list_user))
