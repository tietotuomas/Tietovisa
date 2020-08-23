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
            return render_template("error.html",error_message="Väärä tunnus tai salasana", \
                random_message = utilities.get_random_message())

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/draft")
def draft():
    if not users.is_admin:
        return render_template("error.html", error_message="Sinulla ei ole oikeutta luoda uutta visaa!", \
            random_message = utilities.get_random_message())
    return render_template("draft.html")

@app.route("/new", methods=["POST"])
def new():
    if not users.is_admin:
        return render_template("error.html", error_message="Sinulla ei ole oikeutta luoda uutta visaa!", \
            random_message = utilities.get_random_message())
    topic = request.form["topic"]
    number_of_questions = int(request.form["questions"])
    number_of_choices = int(request.form["choices"])
    return render_template("new.html", topic=topic, choices = number_of_choices, \
        questions = number_of_questions)

@app.route("/create", methods=["POST"])
def create():
    topic = request.form["topic"]
    number_of_choices = request.form["choices"]
    questions = request.form.getlist("question")
    choices = request.form.getlist("choice")
    correct = request.form.getlist("correct")

    for question in questions:
        if question == "":
            return render_template("error.html",error_message="Et täyttänyt kaikkia kenttiä!", \
                random_message = utilities.get_random_message())
        if len(question) > 200:
            return render_template("error.html",error_message="Liian pitkä syöte kysymyksessä, \
                kysymys saa sisältää korkeintaan 200 merkkiä.", random_message = utilities.get_random_message())
    for choice in choices:
        if choice == "":
            return render_template("error.html",error_message="Et täyttänyt kaikkia kenttiä!", \
                random_message = utilities.get_random_message())
        if len(choice) > 100:
            return render_template("error.html",error_message="Liian pitkä syöte vaihtoehdossa, \
                vaihtoehto saa sisältää korkeintaan 100 merkkiä.", random_message = utilities.get_random_message())    
    print(quizzes.get_number_of_questions())
    quizzes.create_quiz(topic)
    quiz_id = quizzes.get_number_of_quizzes()
    question_id = quizzes.get_number_of_questions()
    
    j=0
    for question in questions:
        i=0
        question_id += 1
        quizzes.create_question(question, quiz_id)
        print(question, quiz_id)
        while i < int(number_of_choices):
            quizzes.create_answer(choices[j], question_id, correct[j])
            print(choices[j], correct[j], question_id)
            i += 1
            j += 1

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
            return render_template("error.html",error_message="Rekisteröinti ei onnistunut", \
                random_message = utilities.get_random_message())

@app.route("/quiz/<int:id>")
def quiz(id):
    done = quizzes.get_done_quizzes()
    for quiz in done:
        if quiz[1] == id:
            return render_template("error.html",error_message="Olet jo vastannut tähän kyselyyn!", \
                random_message = utilities.get_random_message())
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
            return render_template("error.html",error_message="Olet jo vastannut tähän kyselyyn!", \
                random_message = utilities.get_random_message())
    question_ids = request.form.getlist("question")
    answer_ids = []
    for question in question_ids:
        if question in request.form:
            answer_ids.append(request.form[question])
    if not answer_ids:
        return render_template("error.html",error_message="Et vastannut yhteenkään kysymykseen? Yritä edes arvalla!", \
            random_message = utilities.get_random_message())
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
    feedback_message = utilities.get_feedback(points)
    return render_template("result.html", topic=topic, correct=correct, answers=answers, \
        amount=len(questions), questions=questions, user_answers = user_answers, message = feedback_message)

@app.route("/stats")
def stats():
    top5 = quizzes.get_top5_users()
    personal_stats = [quizzes.get_all_correct_answers(), quizzes.get_done_answers()]
    registration_time = users.get_registration_time()
    return render_template("stats.html", top5 = top5, personal = personal_stats, time = registration_time)