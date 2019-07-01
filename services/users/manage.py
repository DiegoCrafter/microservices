# services/users/manage.py

import unittest
import coverage

COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py',
    ]
)
COV.start()

from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import User

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command()
def test():
    """Ejecutar los tests sin covertura de codigo"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('seed_db')
def seed_db():
<<<<<<< HEAD
    db.session.add(User(username='luis', email='luis@upeu.edu.pe', password='greathethaneight'))
    db.session.add(User(username='daniel', email='daniel@upeu.edu.pe', password='greathethaneight'))
=======
    db.session.add(User(username='luis', email='luis@upeu.edu.pe'))
    db.session.add(User(username='daniel', email='daniel@upeu.edu.pe'))
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
    db.session.commit()

@cli.command()
def cov():
    """Unitary test with coverage"""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage resume')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    sys.exit(result)

if __name__ == '__main__':
    cli()
