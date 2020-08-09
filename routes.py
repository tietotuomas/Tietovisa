from app import app
from flask import render_template, request, redirect
from db import db # kirjautumisen ja rekisteröinnin tietokantatoiminnot eriytetty
# jo kokonaan omaan moduuliin, tarkoitus eriyttää loputkin tietokantatoiminnot myöhemmin
from flask import session
import users, quizzes

# init.init() #Väliaikainen kökkö tapa poistaa käynnistäessä vanha tietokanta 
# ja luoda uusi (tyhjä). Tämä ei tietysti lopullisessa versiossa toivottava
# ominaisuus, mutta helpottanut kehitystä/testausta alkuvaiheessa.
# init.create() #Tämä lisää tietokantaan pari tietovisaa.

@app.route("/")
def index():
    all = quizzes.get_all()
    done = quizzes.get_done()
    visible = []
    for row in all:
        if row in done:
            continue
        visible.append(row)

    return render_template("index.html", all=len(all), available=len(visible),\
        visible=visible)

@app.route("/login", methods=["get","post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["get","post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if 0 < len(username) <= 15 and 0 < len(password) <= 15 and \
            users.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Rekisteröinti ei onnistunut")

@app.route("/quiz/<int:id>")
def quiz(id):
    sql = "SELECT topic FROM quizzes WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    topic = result.fetchone()[0]
    sql = "SELECT id, content FROM questions WHERE quiz_id=:id"
    result = db.session.execute(sql, {"id":id})
    questions = result.fetchall()
    answers = []
    for q in questions:
        sql = "SELECT id, content, correct, question_id FROM answers WHERE question_id=:q_id"
        result = db.session.execute(sql, {"q_id":q[0]})
        answers += result   
    return render_template("quiz.html", id=id, topic=topic, questions=questions, answers=answers)

@app.route("/answer", methods=["POST"])
def answer():
    quiz_id = request.form["id"]
    question_ids = request.form.getlist("question")
    answer_ids = []
    for q in question_ids:
        print(q)
        answer_ids.append(request.form[q])
    user_id = users.user_id()
    for a in answer_ids:
        sql = "INSERT INTO user_answers (user_id, answer_id) VALUES (:user, :answer);"
        db.session.execute(sql, {"user":user_id, "answer":a})
    db.session.commit()
    return redirect("/result/"+str(quiz_id))

@app.route("/result/<int:id>")
def result(id):
    sql = "SELECT COUNT(questions.id), quizzes.topic FROM questions \
        JOIN quizzes ON questions.quiz_id = quizzes.id WHERE quizzes.id = :id \
        GROUP BY quizzes.topic"
    result = db.session.execute(sql, {"id":id})
    q_and_topic = result.fetchone()
    user_id = users.user_id()
    sql = "SELECT COUNT(answers.id) FROM answers \
    JOIN user_answers ON answers.id = user_answers.answer_id \
    JOIN users ON user_answers.user_id = users.id \
    JOIN questions ON answers.question_id = questions.id \
    JOIN quizzes ON questions.quiz_id = quizzes.id \
    WHERE quizzes.id = :quiz AND answers.correct = TRUE AND users.id = :user"
    result = db.session.execute(sql, {"quiz":id, "user":user_id})
    correct = result.fetchone()[0]
    return render_template("result.html", topic=q_and_topic[1], correct=correct, questions=q_and_topic[0])