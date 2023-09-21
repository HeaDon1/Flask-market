from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)# a limitation of the length of the name.
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item{self.name}'



@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market') 
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)


#from market import app,db
 #   app.app_context().push()
  #  db.create_all()
###