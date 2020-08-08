from db import db
from flask import session

def init():
    init = ["DROP TABLE IF EXISTS quizzes cascade", 
    "DROP TABLE IF EXISTS questions cascade", 
    "DROP TABLE IF EXISTS users cascade", 
    "DROP TABLE IF EXISTS answers cascade",
    "DROP TABLE IF EXISTS user_answers cascade", 
    "CREATE TABLE quizzes (id SERIAL PRIMARY KEY, topic TEXT)", 
    "CREATE TABLE questions (id SERIAL PRIMARY KEY, content TEXT, quiz_id INTEGER REFERENCES quizzes)", 
    "CREATE TABLE answers (id SERIAL PRIMARY KEY, content TEXT, question_id INTEGER REFERENCES questions, correct BOOLEAN)", 
    "CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL, admin BOOLEAN)", 
    "CREATE TABLE user_answers (user_id INTEGER REFERENCES users, answer_id INTEGER REFERENCES answers)"]
    for sql in init:
        db.session.execute(sql)
    
    db.session.commit()


def create():
    create = ["INSERT INTO quizzes (topic) VALUES ('Matematiikkaa englanniksi')",
    "INSERT INTO quizzes (topic) VALUES ('Googlatuin tv-sarja')",
    "INSERT INTO questions (content, quiz_id) VALUES ('Mitä on vähentää englanniksi?', 1)",
    "INSERT INTO questions (content, quiz_id) VALUES ('Mitä on yhteenlasku englanniksi?', 1)",
    "INSERT INTO questions (content, quiz_id) VALUES ('Mitä on kertoma englanniksi?', 1)",
    "INSERT INTO questions (content, quiz_id) VALUES ('Mitä on dividend suomeksi?', 1)",
    "INSERT INTO questions (content, quiz_id) VALUES ('Mikä oli maailmanlaajuisesti googlatuin tv-sarja vuonna 2019?', 2)",
    "INSERT INTO questions (content, quiz_id) VALUES ('Mikä oli maailmanlaajuisesti googlatuin tv-sarja vuonna 2012?', 2)",
    "INSERT INTO questions (content, quiz_id) VALUES ('Mikä oli googlatuin tv-sarja Suomessa vuonna 2018?', 2)",
    "INSERT INTO questions (content, quiz_id) VALUES ('Mikä oli googlatuin tv-sarja USA:ssa vuonna 2015?', 2)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('subtract', 1, TRUE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('distract', 1, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('submit', 1, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('fraction', 1, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('addiction', 2, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('multiply', 2, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('ordinal', 2, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('addition', 2, TRUE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('difference', 3, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('factorial', 3, TRUE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('permutation', 3, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('factory', 3, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('erotus', 4, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('jakaja', 4, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('jaettava', 4, TRUE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('osamäärä', 4, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('American Ninja', 5, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('American Idol', 5, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('Better Call Saul', 5, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('Game of Thrones', 5, TRUE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('Big Brother Brasilia', 6, TRUE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('Gangnam Style', 6, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('Breaking bad', 6, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('Salatut Elämät', 6, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('Salatut Elämät', 7, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('Temptation Island Suomi', 7, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('Selviytyjät Suomi', 7, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('Love Island Suomi', 7, TRUE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('Fear the Walking Dead', 8, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('Breaking Bad', 8, FALSE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('Better Call Saul', 8, TRUE)",
    "INSERT INTO answers (content, question_id, correct) VALUES ('Prison Break', 8, FALSE)"]
    for sql in create:
        db.session.execute(sql)
    
    db.session.commit()