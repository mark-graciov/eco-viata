from flask.ext.wtf import Form
from wtforms import TextField, IntegerField, PasswordField, SubmitField, TextAreaField, DateField
from wtforms.validators import Required

class SignupForm(Form):
	nume = TextField('Nume')
	specie = TextField('Specie')
	varsta = IntegerField('Varsta')
	parola = PasswordField('Parola')
	confirma_parola= PasswordField ('Confirma parola')
	submit = SubmitField('Sign Up')

class CommentForm(Form):
	message = TextAreaField('Mesaj', [Required()])
	submit = SubmitField('Adauga un comentariu')

class CreateArticleForm(Form):
	title = TextField('Titlu', [Required()])
	image = TextField('Imagine')
	content = TextAreaField('Continutul', [Required()])
	submit = SubmitField('Salveaza')

class EventForm(Form):
	title = TextField('Titlu', [Required()])
	address = TextField('Adresa', [Required()])
	date = DateField('Data Inceput', format='%d.%m.%Y')
	content = TextAreaField('Continutul', [Required()])
	submit = SubmitField('Salveaza')
