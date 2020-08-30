from app import app
from flask import render_template, request, redirect
import users, quizzes, utilities
from flask import session

@app.route("/")
def index():
    all = quizzes.get_number_of_quizzes()
    visible = quizzes.get_undone_quizzes()
    return render_template("index.html", all=all, available=len(visible),\
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
    if not users.is_admin():
        return render_template("error.html", error_message="Sinulla ei ole oikeutta luoda uutta visaa!", \
            random_message = utilities.get_random_message())
    return render_template("draft.html")

@app.route("/new", methods=["POST"])
def new():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    if not users.is_admin():
        return render_template("error.html", error_message="Sinulla ei ole oikeutta luoda uutta visaa!", \
            random_message = utilities.get_random_message())
    topic = request.form["topic"]
    if topic == "":
        return render_template("error.html",error_message="Et antanut visalle nimeä.", \
            random_message = utilities.get_random_message())
    if len(topic) > 100:
        return render_template("error.html",error_message="Liian pitkä syöte, \
            nimi saa sisältää korkeintaan 100 merkkiä.", random_message = utilities.get_random_message())
    number_of_questions = int(request.form["questions"])
    number_of_choices = int(request.form["choices"])
    return render_template("new.html", topic=topic, choices = number_of_choices, \
        questions = number_of_questions)

@app.route("/create", methods=["POST"])
def create():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
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
    quiz_id = quizzes.create_quiz(topic)
    answer_index=0
    for question in questions:
        question_id = quizzes.create_question(question, quiz_id)
        for choice in range (int(number_of_choices)):
            quizzes.create_answer(choices[answer_index], question_id, correct[answer_index])
            answer_index += 1
    return redirect("/")

@app.route("/register", methods=["get","post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not users.test_length(username, password):
            return render_template("error.html", error_message="Rekisteröinti ei onnistunut, \
                tarkista käyttäjätunnuksen ja salasanan pituus.", random_message = utilities.get_random_message())
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html", error_message="Rekisteröinti ei onnistunut, \
                käyttäjätunnus on jo käytössä.", random_message = utilities.get_random_message())

@app.route("/quiz/<int:id>")
def quiz(id):
    if quizzes.is_done(id):
        return render_template("error.html",error_message="Olet jo vastannut tähän kyselyyn!", \
            random_message = utilities.get_random_message())
    topic = quizzes.get_quiz_topic(id)
    questions = quizzes.get_question_content_and_ids(id)
    answers = quizzes.get_answers_info(questions)
    return render_template("quiz.html", id=id, topic=topic, questions=questions, answers=answers)

@app.route("/answer", methods=["POST"])
def answer():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    quiz_id = request.form["id"]
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
    if not quizzes.is_done(id):
        return render_template("error.html",error_message="Et voi tarkastella tämän kyselyn tuloksia.", \
            random_message = utilities.get_random_message())
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
    done_quizzes = quizzes.get_done_quizzes()
    registration_time = users.get_registration_time()
    registration_number = users.get_ordinal()
    return render_template("stats.html", ordinal = registration_number, top5 = top5, personal = personal_stats, \
        time = registration_time, done = done_quizzes)

@app.route("/administration")
def administration():
    if not users.is_admin():
        return render_template("error.html", error_message="Sinulla ei ole ylläpitäjän oikeuksia!", \
            random_message = utilities.get_random_message())
    non_admin_users = users.get_non_admin_users()
    return render_template("administration.html", users = non_admin_users)

@app.route("/administrate", methods=["POST"])
def administrate():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    if "user" not in request.form:
        return render_template("error.html",error_message="Et valinnut käyttäjää.", \
            random_message = utilities.get_random_message())
    user = request.form["user"]
    action = request.form["action"]
    if action == "delete":
        users.delete_user(user)
    elif action == "admin":
        users.set_admin(user)
    else:
        return render_template("error.html",error_message="Et valinnut toimintoa.", \
            random_message = utilities.get_random_message())
    return redirect("/")
 