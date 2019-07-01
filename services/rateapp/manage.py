from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import Student
from project.api.models import Teacher
from project.api.models import Review
from project.api.models import Rating
import coverage
import unittest

COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py'
    ]
)
COV.start()

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('seed_db')
def seed_db():
    db.session.add(Student(username='luis', email='luis@upeu.edu.pe', password='greathethaneight'))
    db.session.add(Student(username='daniel', email='daniel@upeu.edu.pe', password='greathethaneight'))
    db.session.add(Teacher(teachername='Armando', teacherlastname='Puertas Escobar', 
                            teachercareer='Ing. de Sonido', teacherfaculty='FIAG'))
    db.session.add(Teacher(teachername='Jhanx', teacherlastname='Chipi Taps', 
                            teachercareer='Ing. de Sonido', teacherfaculty='FIAG'))
    db.session.add(Teacher(teachername='Armando', teacherlastname='Puertas Escobar', 
                            teachercareer='Ing. de Sonido', teacherfaculty='FIAG'))
    db.session.add(Review(comment='Excelente el mejor de biblia'))
    db.session.add(Review(comment='Excelente el mejor de los psicologos'))
    db.session.add(Rating(votes=5, student_id=1, review_id=1, teacher_id=1))
    db.session.add(Rating(votes=5, student_id=2, review_id=2, teacher_id=1))
    db.session.add(Rating(votes=5, student_id=2, review_id=2, teacher_id=2))
    db.session.commit()

@cli.command()
def test():
   """ Ejecutar las pruebas sin covertura de codigo"""
   tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
   result = unittest.TextTestRunner(verbosity=2).run(tests)
   if result.wasSuccessful():
       return 0
   return 1

@cli.command()
def cov():
    """Ejecuta las pruebas unitarias"""
    tests = unittest.TestLoader.discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Resume')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    sys.exit(result)

if __name__ == '__main__':
    cli()