from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
import utilities

def login(username,password):
    print(generate_password_hash("admin"))
    sql = "SELECT password, id, username, admin FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None: #tämä turha?
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
    del session["username"]
    del session["admin"]
    del session["ordinal"]

def test_length(username, password):
    if 2 < len(username) <= 15 and 2 < len(password) <= 15:
        return True
    return False

def register(username,password):
    hash_value = generate_password_hash(password)
    try: 
        sql = "INSERT INTO users (username,password,created_at) VALUES (:username,:password, NOW())"
        db.session.execute(sql, {"username":username,"password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username,password)

def user_id():
    return session.get("user_id")

def get_registration_time():
    user = user_id()
    sql = "SELECT created_at FROM users WHERE users.id = :user"
    result = db.session.execute(sql, {"user":user})
    return result.fetchone()[0]

def is_admin():
    return session.get("admin")
