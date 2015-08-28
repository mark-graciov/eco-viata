from app import db

from datetime import datetime

class Article(db.Model):
	__tablename__='article'

	id 	= db.Column(db.Integer, primary_key=True)
	title =db.Column(db.String(255))
	content = db.Column(db.UnicodeText()) 
	date = db.Column(db.DateTime(), default = datetime.now)
	imagine = db.Column(db.String(255))

	def save(self):
		db.session.add(self)
		db.session.commit()


class User(db.Model):
	__tablename__='user'

	id = db.Column(db.Integer, primary_key=True)
	nume = db.Column(db.String(255))
	email = db.Column(db.String(255))
	parola = db.Column(db.String(255))

class Comment(db.Model):
	__tablename__='comment'
	
	id = db.Column(db.Integer, primary_key=True)
	message = db.Column(db.String(255))
	user_id = db.Column (db.Integer(), db.ForeignKey('user.id'))
	user = db.relationship('User')
	article_id = db.Column (db.Integer(), db.ForeignKey('article.id'))
	article = db.relationship('Article')
	date = db.Column(db.DateTime(), default = datetime.now)

class Event(db.Model):
	__tablename__="event"
	
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255))
	content = db.Column(db.UnicodeText()) 
	date = db.Column(db.DateTime(), default = datetime.now)
	address = db.Column(db.String(255))
	longitude = db.Column(db.String(255))
	latitude = db.Column(db.String(255))

	def save(self):
		db.session.add(self)
		db.session.commit()
	
class Contact(db.Model):
	__tablename__="contacts"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	location = db.Column(db.String(255))
	district_name = db.Column(db.String(255))
	longitude = db.Column(db.String(255))
	latitude = db.Column(db.String(255))
	phone_number =db.Column(db.String(255))
	activities = db.Column(db.UnicodeText())
