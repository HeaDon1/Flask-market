from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)






if __name__ == '__main__':
    app.run(debug=True)


#from market import app,db
 #   app.app_context().push()
  #  db.create_all()
###