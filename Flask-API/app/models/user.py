from .models import db
from datetime import datetime

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.Integer())
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    password_hash = db.Column(db.String(64) , nullable=False )
    password_reset_token = db.Column(db.String(64) , nullable=True )
    created_at = db.Column(db.DateTime() , nullable=False , default=datetime.utcnow)

    user_type = db.Column(db.String(10))
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(model, id):
        return model.query.get_or_404(id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()