from db import DbQuery
import hashlib

class Users:

    def __init__(self):
        pass

    def create_user(self, query):
        keys = ""
        values = ""
        for key, val in query:
            keys += f"`{key}`, "
            values += f"`{val}`, "
        keys = keys[:-2]
        values = values[:-2]
        DbQuery().connect_to_engine(f"INSERT INTO users ({keys}) VAlUES ({values})")


    def change_password(self, new_password, user_id):
        h = hashlib.sha256()
        h.update(new_password)
        h.digest
        DbQuery().connect_to_engine(f"UPDATE users SET password = {h} WHERE id = {user_id}")