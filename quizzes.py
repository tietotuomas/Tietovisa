from db import db
import users

def get_all():
    sql = "SELECT topic, id FROM quizzes"
    result = db.session.execute(sql)
    return result.fetchall()

def get_done():
    user = users.user_id()
    sql = "SELECT DISTINCT quizzes.topic, quizzes.id FROM answers\
    JOIN user_answers ON answers.id = user_answers.answer_id\
    JOIN users ON user_answers.user_id = users.id\
    JOIN questions ON answers.question_id = questions.id\
    JOIN quizzes ON questions.quiz_id = quizzes.id\
    WHERE users.id = :user"
    result = db.session.execute(sql, {"user":user})
    return result.fetchall()
    
