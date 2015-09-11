from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ecoviata/eco-viata/app.db'

if __name__=='__main__':
	app.run()
