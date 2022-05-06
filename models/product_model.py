#from config.app_config import db
from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@localhost/xyz'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Product(db.Model):                                             #Model -- a class --> which is aware it ORM --> Object relation mapping -->  table -- Product
    pid = db.Column('prod_id',db.Integer,primary_key = True)        #pid object ch attribute -- python side la
    prod_name = db.Column('prod_name',db.String(30))                #prod_id column at database side..
    prod_price = db.Column('prod_price',db.Float)
    prod_qty = db.Column('prod_qty', db.Integer)
    prod_ven = db.Column('prod_ven',db.String(30))



#db.create_all() # equivalent --> create table -->



#crud operations -->

'''
create table
db.create_all()

drop table
db.drop_all()

insert into
Product(namedparams) 
p1 = Product(pid = 101,prod_name = 'XXX')    #python attributes, not a column names
db.session.add(p1)
db.session.commit()     # insert..


update tablename

fetch -- by primary key

fetch  -- by non-primary key

delete the records -->



'''

'''
class Product:
    def __init__(self,pid,pnm,pqty,pven,pric):
        self.prod_id = pid
        self.prod_name = pnm
        self.prod_qty = pqty
        self.prod_ven = pven
        self.prod_price = pric
'''