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
    if form.validate_on_submit():
        return redirect(url_for("index"))

    return render_template("create.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)