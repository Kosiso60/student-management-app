from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Score(db.Model):
    __tablename__='scores'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.Integer())
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(model, id):
        return model.query.get_or_404(id)

    def delete(self):
        db.session.add(self)
        db.session.commit()