from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
import utilities

def login(username,password):
    sql = "SELECT password, id, username, admin FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if check_password_hash(user[0],password):
            session["user_id"] = user[1]
            session["username"] = user[2]
            session["admin"] = user[3]
            session["ordinal"] = utilities.get_ordinal(user[1])              
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(username,password):
    hash_value = generate_password_hash(password)
    
    try:
        if 2 < len(username) <= 15 and 2 < len(password) <= 15:
            sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
            db.session.execute(sql, {"username":username,"password":hash_value})
            db.session.commit()
        else: raise ValueError("Invalid length.")
    except:
        return False
    return login(username,password)

def user_id():
    return session.get("user_id",0)