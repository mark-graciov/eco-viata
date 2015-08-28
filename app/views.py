from app import app
from app.forms import SignupForm, CommentForm
from app.models import Article, Comment, Contact, Event

from datetime import datetime

from flask import render_template

from babel.dates import format_datetime

# Jinja template functions
def fmt_datetime(value, format='short'):
    if format == 'full':
        format="EEEE, d. MMMM y 'at' HH:mm"
    elif format == 'short':
        format="dd.MM.yyyy"
    return format_datetime(value, format)

app.jinja_env.filters['datetime'] = fmt_datetime

# Jinja template functions END.

@app.route('/')
def index():
	animals_list = ['Enot','Elefant','Enot2', 'Zebra']
	return render_template('index.html', animals=animals_list, best_animal='Mark')
	
@app.route ('/signup', methods=['GET','POST'])
def signup():
	form= SignupForm()
	if form.validate_on_submit():
		print form.nume.data, form.varsta.data
		return render_template ('index.html')
	return render_template('signup.html', form = form)

@app.route('/article/<id>', methods=['GET', 'POST'])
def article(id):
	a = Article.query.get(id)

	form = CommentForm()
	if form.validate_on_submit():
		c = Comment(user_id = 1, message = form.message.data,article = a )
		c.save()

	comments = Comment.query.filter_by(article_id = id)
	return render_template('article.html', article = a, comments = comments, form=form)

@app.route("/contacts")
def contacts():
	contacts_list = Contact.query.all()
	return render_template("contacts.html", contacts=contacts_list)

@app.route("/events")
def events():
	event_list = Event.query.all()
	return render_template("events.html", events =event_list)