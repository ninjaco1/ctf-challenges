import mysql.connector
import hashlib
import random

####
# WARNING: DO NOT USE THIS AS A GUIDE FOR HOW TO USE MYSQL WITH PYTHON
# THIS STUFF BARELY WORKS
####

class CtfDatabase:
    def __init__(self, config, log):
        self.log = log
        self.connection = mysql.connector.connect(**config)
        # Sometimes queries are cached and it causes issues, this is supposed to fix it
        self.connection.autocommit = True
        self.connection.cursor(buffered=True)

    def sql_fetchone(self, sql, val=None):
        self.connection.ping(reconnect=True, attempts=2, delay=2)
        self.log.log("SQL: " + sql)
        cursor = self.connection.cursor()
        if val:
            self.log.log("VAL: " + repr(val))
            cursor.execute(sql, val)
        else:
            cursor.execute(sql)
        ret = cursor.fetchone()
        cursor.close()
        return ret

    def sql_fetchall(self, sql, val=None):
        self.connection.ping(reconnect=True, attempts=2, delay=2)
        self.log.log("SQL: " + sql)
        cursor = self.connection.cursor()
        if val:
            self.log.log("VAL: " + repr(val))
            cursor.execute(sql, val)
        else:
            cursor.execute(sql)
        ret = cursor.fetchall()
        cursor.close()
        return ret

    def sql_commit(self, sql, val=None):
        self.connection.ping(reconnect=True, attempts=2, delay=2)
        self.log.log("SQL: " + sql)
        cursor = self.connection.cursor()
        if val:
            self.log.log("VAL: " + repr(val))
            cursor.execute(sql, val)
        else:
            cursor.execute(sql)
        self.connection.commit()
        ret = cursor.lastrowid
        cursor.close()
        return ret

    # Member Verification (patched out because y'all are verified already)
    def new_member(self, id, username):
            # Do nothing if the user is already in the members table
            if (self.sql_fetchone("select * from members where id = %d" % id)):
                return

            # Generate a new token and add the user to the member table
            token = hashlib.md5(
                (str(id) + str(random.randint(10000000, 9999999999))).encode()
            ).hexdigest()
            self.sql_commit("insert into members (id, username, token) values (%s, %s, %s);", val=(id, username, token))

    def verify_member(self, id, token):
        self.sql_commit("update members set verified = 1 where id = %s;", val=(id,))
        return self.is_user_verified(id)

    def is_user_verified(self, id):
            try:
                return self.sql_fetchone("select verified from members where id = %s;", val=(id,))[0] == 1
            except:
                return False

    def get_email(self, id):
        try:
            email = self.sql_fetchone("select email from members where id = %s;", val=(id,))[0]
            return email
        except:
            return ""

    def get_token(self, id):
        try:
            token = self.sql_fetchone("select token from members where id = %s;", val=(id,))[0]
            return token
        except:
            return ""

    def set_email(self, id, email):
        self.sql_commit("update members set email = %s where id = %s;", val=(email, id))
