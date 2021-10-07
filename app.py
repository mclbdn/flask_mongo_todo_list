from flask import Flask, render_template
from flask.helpers import url_for
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)

app.config['SECRET_KEY'] = "mysecreto1"

class TodoForm(FlaskForm):
    todo_input = StringField(label="Enter the text of TODO", validators=[DataRequired(), Length(min=1, max=100)])
    submit = SubmitField(label="Submit")

@app.route("/", methods=["GET", "POST"])
def home():
    form = TodoForm()
    if form.validate_on_submit():
        return redirect(url_for("home"))

    return render_template("home.html", form=form)

@app.route("/create", methods=["GET", "POST"])
def create():
    form = TodoForm()
    form.todo_input.render_kw = {"placeholder": "Create a new TODO"}
    if form.validate_on_submit():
        return redirect(url_for("index"))

    return render_template("create.html", form=form, title="Create")

@app.route("/read", methods=["GET", "POST"])
def read():
    form = TodoForm()
    form.todo_input.render_kw = {"placeholder": "Search by text"}
    if form.validate_on_submit():
        return redirect(url_for("index"))

    return render_template("read.html", form=form, title="Read")

@app.route("/update", methods=["GET", "POST"])
def update():
    form = TodoForm()
    form.todo_input.render_kw = {"placeholder": "Update by ID"}
    if form.validate_on_submit():
        return redirect(url_for("index"))

    return render_template("update.html", form=form, title="Update")

@app.route("/delete", methods=["GET", "POST"])
def delete():
    form = TodoForm()
    form.todo_input.render_kw = {"placeholder": "Delete by ID"}
    if form.validate_on_submit():
        return redirect(url_for("index"))

    return render_template("delete.html", form=form, title="Delete")

if __name__ == "__main__":
    app.run(debug=True)