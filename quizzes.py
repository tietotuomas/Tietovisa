from db import db
import users

def get_all_quizzes():
    sql = "SELECT topic, id FROM quizzes"
    result = db.session.execute(sql)
    return result.fetchall()

def get_done_quizzes():
    user = users.user_id()
    sql = "SELECT DISTINCT quizzes.topic, quizzes.id FROM answers\
        JOIN user_answers ON answers.id = user_answers.answer_id\
        JOIN users ON user_answers.user_id = users.id\
        JOIN questions ON answers.question_id = questions.id\
        JOIN quizzes ON questions.quiz_id = quizzes.id\
        WHERE users.id = :user"
    result = db.session.execute(sql, {"user":user})
    return result.fetchall()

def get_quiz_topic(id):
    sql = "SELECT topic FROM quizzes WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def get_question_content_and_ids(id):
    sql = "SELECT id, content FROM questions WHERE quiz_id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def get_user_answers(id):
    user = users.user_id()
    sql = "SELECT answers.id FROM answers \
        JOIN user_answers ON answers.id = user_answers.answer_id \
        JOIN users ON user_answers.user_id = users.id \
        JOIN questions ON answers.question_id = questions.id \
        JOIN quizzes ON questions.quiz_id = quizzes.id \
        WHERE quizzes.id = :id AND users.id = :user"
    result = db.session.execute(sql, {"id":id, "user":user})
    return [row[0] for row in result.fetchall()]

def get_correct_answers(id):
    user = users.user_id()
    sql= "SELECT COUNT(answers.id) FROM answers \
        JOIN user_answers ON answers.id = user_answers.answer_id \
        JOIN users ON user_answers.user_id = users.id \
        JOIN questions ON answers.question_id = questions.id \
        JOIN quizzes ON questions.quiz_id = quizzes.id \
        WHERE quizzes.id = :id AND answers.correct = TRUE AND users.id = :user"
    result = db.session.execute(sql, {"id":id, "user":user})
    return result.fetchone()[0] 

def get_answers_info(questions):
    answers = []
    for question in questions:
        sql = "SELECT id, content, question_id, correct FROM answers WHERE question_id=:q_id"
        result = db.session.execute(sql, {"q_id":question[0]})
        answers += result.fetchall()
    return answers

def set_answers(answer_ids):
    user = users.user_id()
    for answer in answer_ids:
        sql = "INSERT INTO user_answers (user_id, answer_id) VALUES (:user, :answer);"
        db.session.execute(sql, {"user":user, "answer":answer})
    db.session.commit()