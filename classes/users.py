from datetime import datetime, timezone
from .db import DbQuery
import hashlib
from flask import session

class Users(DbQuery):


    def create_user(self, form):
        email = form["email"]
        username = form["username"]
        password = form["password"]
        confirm_password = form["confirm_password"]
        name = form["name"]
        if password == confirm_password:
            hashed_password = self.password_hashing(password)
            self.connect_to_engine(f"INSERT INTO users (email, username, password, name, date_of_reg) VALUES ('{email}', '{username}', '{hashed_password}', '{name}', '{datetime.now(timezone.utc)}')")
        else:
            return "Passwords dont match"

    def change_password(self, new_password, user_id):
        new_password = self.password_hashing(new_password)
        self.connect_to_engine(f"UPDATE users SET password = {new_password} WHERE id = {user_id}")

    def password_hashing(self, password):
        password = password.encode("utf-8")
        hash = hashlib.sha256()
        hash.update(password)
        return hash.hexdigest()
    
    def login(self, username, password):
        username = username
        password = self.password_hashing(password)
        check_user = self.connect_to_engine(f"SELECT * FROM users WHERE username = '{username}'", True)
        if len(check_user) > 0:
            check_pass = self.connect_to_engine(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'", True)
            print(check_pass)
            if len(check_pass) > 0:
                session['user_id'] = check_pass[0][0]
                print(session['user_id'])
            else:
                print('Passowrd wrong')
        else:
            print('No such user')

    def logout(self):
        session.pop('user_id', default=None)