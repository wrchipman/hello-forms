from app import app
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)  

@app.route('/user/<name>')
def user(name):
    val = 5
    return render_template('user.html', name=name, val=val)