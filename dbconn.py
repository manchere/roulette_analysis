import psycopg2


class DbConnection:
    def __init__(self, db, host, user, password):
        super(DbConnection, self).__init__()
        self.db = db
        self.host = host
        self.user = user
        self.password = password

    def connect(self):
        conn = psycopg2.connect(dbname=self.db,
                                host=self.host,
                                user=self.user,
                                password=self.password,
                                port=5432)
        conn.cursor()
        # print(conn.status)

    @property
    def db(self):
        return self._db

    @db.setter
    def db(self, value):
        self._db = value

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        self._host = value

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

