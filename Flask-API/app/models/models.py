from flask_sqlalchemy import SQLAlchemy
# from api import app, db
db = SQLAlchemy()

import jwt
import datetime as dt
from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import app, db, login_manager
