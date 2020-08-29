from db import db
import users

def get_all_quizzes():
    sql = "SELECT topic, id FROM quizzes"
    result = db.session.execute(sql)
    return result.fetchall()

def get_undone_quizzes():
    user = users.user_id()
    sql = "SELECT quizzes.topic, quizzes.id FROM quizzes WHERE quizzes.id NOT IN \
        (SELECT quizzes.id FROM quizzes \
        JOIN questions ON quizzes.id = questions.quiz_id \
        JOIN answers ON questions.id = answers.question_id \
        JOIN user_answers ON answers.id = user_answers.answer_id \
        JOIN users ON user_answers.user_id = users.id \
        WHERE users.id = :user)"
    result = db.session.execute(sql, {"user":user})
    return result.fetchall()

def get_number_of_quizzes():
    sql = "SELECT COUNT(*) FROM quizzes"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def is_done(quiz):
    user = users.user_id()
    sql = "SELECT quizzes.id FROM quizzes \
        JOIN questions ON quizzes.id = questions.quiz_id \
        JOIN answers ON questions.id = answers.question_id \
        JOIN user_answers ON answers.id = user_answers.answer_id \
        JOIN users ON user_answers.user_id = users.id\
        WHERE users.id = :user AND quizzes.id = :quiz"
    result = db.session.execute(sql, {"user":user, "quiz":quiz})
    if result.fetchone() != None:
        return True
    return False

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

def get_done_answers():
    done_quizzes = get_done_quizzes()
    if not done_quizzes:
        return 0
    quiz_ids = []
    for quiz in done_quizzes:
        quiz_ids.append(quiz[1])
    sql = "SELECT COUNT(questions.id) FROM questions \
        JOIN quizzes ON questions.quiz_id = quizzes.id \
        WHERE quizzes.id IN :quizzes"
    result = db.session.execute(sql, {"quizzes":tuple(quiz_ids)})
    return result.fetchone()[0]        

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
        WHERE quizzes.id = :id AND answers.correct AND users.id = :user"
    result = db.session.execute(sql, {"id":id, "user":user})
    return result.fetchone()[0]

def get_all_correct_answers():
    user = users.user_id()
    sql = "SELECT COUNT(*) FROM answers \
        JOIN user_answers ON answers.id = user_answers.answer_id \
        JOIN users ON user_answers.user_id = users.id \
        WHERE answers.correct AND users.id = :user"
    result = db.session.execute(sql, {"user":user})
    return result.fetchone()[0]
 
def get_answers_info(questions):
    question_ids = []
    for question in questions:
        question_ids.append(question[0])
    sql = "SELECT id, content, question_id, correct FROM answers \
        WHERE question_id IN :questions"
    result = db.session.execute(sql, {"questions":tuple(question_ids)})
    return result.fetchall()
    

def set_answers(answer_ids):
    user = users.user_id()
    for answer in answer_ids:
        sql = "INSERT INTO user_answers (user_id, answer_id) VALUES (:user, :answer);"
        db.session.execute(sql, {"user":user, "answer":answer})
    db.session.commit()

def create_quiz(topic):
    sql = "INSERT INTO quizzes (topic) VALUES (:topic) RETURNING id"
    result = db.session.execute(sql, {"topic":topic})
    db.session.commit()
    return result.fetchone()[0]

def create_question(question, quiz_id):
    sql = "INSERT INTO questions (content, quiz_id) VALUES (:content, :quiz) RETURNING id"
    result = db.session.execute(sql, {"content":question, "quiz":quiz_id})
    db.session.commit()
    return result.fetchone()[0]

def create_answer(answer, question_id, correct):
    sql = "INSERT INTO answers (content, question_id, correct) VALUES (:content, :quiz, :correct)"
    db.session.execute(sql, {"content":answer, "quiz":question_id, "correct":correct})
    db.session.commit()

def get_top5_users():
    sql = "SELECT users.username, COUNT(answers.id) AS TOTAL FROM users \
        JOIN user_answers ON users.id = user_answers.user_id \
        JOIN answers ON answers.id = user_answers.answer_id \
        WHERE answers.correct \
        GROUP BY users.username \
        ORDER BY TOTAL DESC LIMIT 5"
    result = db.session.execute(sql)
    return result.fetchall()

