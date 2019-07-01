from project import db
from project.api.models import User


<<<<<<< HEAD
def add_user(username, email, password):
    user = User(username=username, email=email, password=password)
=======
def add_user(username, email):
    user = User(username=username, email=email)
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
    db.session.add(user)
    db.session.commit()

    return user
