from app import app, db
from data import __init__
from data.models import *

__init__.init_db(app, db)

