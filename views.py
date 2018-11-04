import sqlite3

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from flask import Flask
app = Flask(__name__)

db = sqlite.connect("skill_test.db")

app.route("/create_quiz")
def create_quiz():

    db.execute("""

    """)

app.route("/delete")
@login_required
def delete_quiz(quiz_id):

    if request.method == 'POST':
        db.execute("""
            DELETE FROM quiz WHERE id = ?
        """, quiz_id)

    return render_template('blog/update.html', post=post)


app.route("/report")
@login_required
def make_user_report():

    pass


app.route("/start")
@login_required
def start_quiz(quiz_id):

    db.execute("""
        INSERT INTO user_history VALUES (

        )
    """)

    db.commit()

    return render_template()


app.route("/complete")
@login_required
def complete_quiz():

    answers = request.form['answers']

    db.execute("""
        UPDATE INTO user_history VALUES (

        )
    """)

    for a in answers:

       db.execute("""
        INSERT INTO user_answers VALUES (

        )
    """) 

    db.commit()

    return 