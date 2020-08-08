from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

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

            numerals = ["ensimmäinen", "toinen", "kolmas", "neljäs", "viides", "kuudes",\
                            "seitsemäs", "kahdeksas", "yhdeksäs", "kymmenes"]         
            if session["user_id"] <= 10:
                for i in range (1, 10):
                    if i == session["user_id"]:
                        session["ordinal"] = numerals[i-1]
            else:
                session["ordinal"] = str(session["user_id"]) + "."
                
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(username,password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
        db.session.execute(sql, {"username":username,"password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username,password)

def user_id():
    return session.get("user_id",0)