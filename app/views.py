from app import app
from app.forms import SignupForm, CommentForm, CreateArticleForm
from app.models import Article, Comment, Contact, Event

from datetime import datetime

from flask import render_template, request, redirect, url_for

from babel.dates import format_datetime
from sqlalchemy import distinct, desc

# Jinja template functions
@app.context_processor
def active_provider():
	def print_active(category):
		if category in request.path:
			return "active"
		return ""
	return dict(print_active = print_active)

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
	active_district = request.args.get('distr')

	contacts = []
	if active_district:
		contacts = Contact.query.filter_by(district_name = active_district).all()

	districts_list = Contact.query.with_entities(Contact.district_name).distinct().all()
	districts = []
	for d_list in districts_list:
		districts.append(d_list[0])

	articles = Article.query.order_by(desc(Article.date)).limit(3).all()

	# event = None
	event_list = Event.query.filter(Event.date >= datetime.now()).order_by(desc(Event.date)).limit(1).all()
	event = None
	if len(event_list) > 0:
		event = event_list[0]

	return render_template('index.html', active_district = active_district, districts = districts, articles = articles, contacts = contacts, event = event)
	
@app.route('/articles')
def articles():
	articles = Article.query.order_by(desc(Article.date)).all()
	return render_template('article-list.html', articles = articles)

@app.route('/article/<id>', methods=['GET', 'POST'])
def article(id):
	a = Article.query.get(id)
	form = CommentForm()

	if form.validate_on_submit():
		c = Comment(user_id = 1, message = form.message.data,article = a )
		

		c.save()

	comments = Comment.query.filter_by(article_id = id)
	return render_template('article.html', article = a, comments = comments, form=form)

@app.route('/create-article', defaults={'id' : None}, methods=['GET', 'POST'])
@app.route('/edit-article/<id>', methods=['GET', 'POST'])
def edit_article(id):
	form = CreateArticleForm()

	if form.validate_on_submit():
		print form.title.data
		a = Article(id=id, title=form.title.data, content=form.content.data, imagine=form.image.data)
		a.method_save()
		return redirect(url_for('article', id=a.id))

	if id != None:
		a = Article.query.get(id)
		form.title.data = a.title
		form.content.data = a.content
		form.image.data = a.imagine

	return render_template('edit-article.html', form = form, article_id = id)
	
@app.route("/events")
def events():
	event_list = Event.query.order_by(desc(Event.date)).all()
	return render_template("events.html", events = event_list)

@app.route("/contacts")
def contacts():
	contacts_list = Contact.query.all()
	return render_template("contacts.html", contacts = contacts_list)

@app.route ("/about")
def about():
	return render_template("about.html")
