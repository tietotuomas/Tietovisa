from app import app
from flask import render_template, request, redirect
import users, quizzes, utilities

@app.route("/")
def index():
    all = quizzes.get_all_quizzes()
    done = quizzes.get_done_quizzes()
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
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Rekisteröinti ei onnistunut")

@app.route("/quiz/<int:id>")
def quiz(id):
    done = quizzes.get_done_quizzes()
    for quiz in done:
        if quiz[1] == id:
            return render_template("error.html",message="Olet jo vastannut tähän kyselyyn")
    topic = quizzes.get_quiz_topic(id)
    questions = quizzes.get_question_content_and_ids(id)
    answers = quizzes.get_answers_info(questions)
    return render_template("quiz.html", id=id, topic=topic, questions=questions, answers=answers)

@app.route("/answer", methods=["POST"])
def answer():
    quiz_id = request.form["id"]
    done = quizzes.get_done_quizzes()
    for quiz in done:
        if quiz[1] == int(quiz_id):
            message = "Olet jo vastannut tähän kyselyyn" #(*)ilmeisesti täältä
            return render_template("error.html",message=message)
    question_ids = request.form.getlist("question")
    answer_ids = []
    for q in question_ids:
        if q in request.form:
            answer_ids.append(request.form[q])
    if not answer_ids: #tämä antaa kummallisesti väärän messagen(*)
        message = "Et vastannut yhteenkään kysymykseen? Yritä edes arvalla."
        return render_template("error.html",message=message)
    quizzes.set_answers(answer_ids)
    return redirect("/result/"+str(quiz_id))

@app.route("/result/<int:id>")
def result(id):
    topic = quizzes.get_quiz_topic(id)
    questions = quizzes.get_question_content_and_ids(id)
    answers = quizzes.get_answers_info(questions)
    user_answers = quizzes.get_user_answers(id)
    correct = quizzes.get_correct_answers(id)
    points = correct/len(questions)
    message = utilities.get_feedback(points)
    return render_template("result.html", topic=topic, correct=correct, answers=answers, \
        amount=len(questions), questions=questions, user_answers = user_answers, message = message)