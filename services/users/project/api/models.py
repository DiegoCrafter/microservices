from sqlalchemy.sql import func
from project import db


class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
<<<<<<< HEAD
    password = db.Column(db.String(256), nullable=False)
=======
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
<<<<<<< HEAD
            'password': self.password,
            'active': self.active
        }
=======
            'active': self.active
        }
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
