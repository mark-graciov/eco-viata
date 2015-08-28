from app import app

from app.forms import SignupForm, CommentForm

from app.models import Article, Comment, Contact

from datetime import datetime

from flask import render_template

@app.route('/')
def index():
	a = Article.query.get(1)
	return render_template('index.html', article = a)
	
@app.route ('/signup', methods=['GET','POST'])
def signup():
	form= SignupForm()
	if form.validate_on_submit():
		print form.nume.data, form.varsta.data
		return render_template ('index.html')
	return render_template('signup.html', form = form)

@app.route ('/article/<id>', methods=['GET', 'POST'])
def article(id):
	a = Article.query.get(id)

	form = CommentForm()
	if form.validate_on_submit():
		c = Comment(user_id = 1, message = form.message.data,article = a )
		

		c.save()

	comments = Comment.query.filter_by(article_id = id)


	return render_template('article.html', article = a, comments = comments, form=form)

@app.route  ("/contacts")
def contacts():
	contacts_list = Contact.query.all()
	print contacts_list 
	

	return render_template("contacts.html", contacts=contacts_list)