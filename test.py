from app import app
from models import db, connect_db
import unittest

# some different configuration
# turn off flask debug toolbar INTERCEPTS_REQUESTS
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt-test'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()
