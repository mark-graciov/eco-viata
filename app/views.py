from app import app
from app.forms import SignupForm, CommentForm, CreateArticleForm
from app.models import Article, Comment, Contact, Event

from datetime import datetime

from flask import render_template, request

from babel.dates import format_datetime
from sqlalchemy import distinct, desc

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
	active_district = request.args.get('distr')

	contacts = None
	if active_district:
		contacts = Contact.query.filter_by(district_name = active_district).all()

	districts_list = Contact.query.with_entities(Contact.district_name).distinct()
	districts = []
	for d_list in districts_list:
		districts.append(d_list[0])

	articles = Article.query.order_by(desc(Article.date)).limit(3)

	return render_template('index.html', active_district = active_district, districts = districts, articles = articles, contacts = contacts)
	
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
	return render_template("contacts.html", contacts = contacts_list)

@app.route("/events")
def events():
	event_list = Event.query.all()
	return render_template("events.html", events = event_list)

@app.route('/edit-article/<id>', defaults={'id' : None}, methods=['GET', 'POST'])
def create_article(id):
	form = CreateArticleForm()

	if id != None:
		a = Article.query.get(id)
		form.title.data = a.title
		form.content.data = a.content
		form.image.data = a.imagine

	if form.validate_on_submit():
		a = Article(id = id, title = form.title.data, content = form.content.data, imagine = form.image.data)
		a.save()
		return redirect(url_for('article', id=a.id))

	return render_template('edit-article.html', form = form, article_id = id)
	
@app.route('/articles')
def articles():
	articles = Article.query.all()
	return render_template('article-list.html', articles = articles)

@app.route ("/about")
def about():
	return render_template("about.html")
