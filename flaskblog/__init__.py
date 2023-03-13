from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app= Flask(__name__)



app.config['SECRET_KEY'] = 'bd73c0dd78b2092e561807c2f9c76d40'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# the 3 forward slashes are a relative path from current file

#database instance has been created, we can structure our 
# database using classes in sqlalchemy called modals
db= SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_messsage_category='info'

app.app_context().push()

from flaskblog import routes