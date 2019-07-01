from sqlalchemy.sql import func
from project import db


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)
    rating = db.relationship("Rating")

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'active': self.active
        }


class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    teachername = db.Column(db.String(128), nullable=False)
    teacherlastname = db.Column(db.String(128), nullable=False)
    teachercareer = db.Column(db.String(128), nullable=False)
    teacherfaculty = db.Column(db.String(128), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.teachername,
            'lastname': self.teacherlastname,
            'career': self.teachercareer,
            'faculty': self.teacherfaculty
        }


class Rating(db.Model):
    __tablename__ = 'rating'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    votes = db.Column(db.Integer)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    review_id = db.Column(db.Integer, db.ForeignKey('review.id'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    teacher = db.relationship('Teacher')

    def __init__(self, votes, student_id, review_id, teacher_id):
        self.votes = votes
        self.student_id = student_id
        self.review_id = review_id
        self.teacher_id = teacher_id


class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String(256), nullable=False)
    update_at = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, comment):
        self.comment = comment
