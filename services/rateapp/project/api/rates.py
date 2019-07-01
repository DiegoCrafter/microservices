from flask import Blueprint, jsonify, request, render_template, redirect
from project.api.models import Student, Teacher, db

rates_blueprint = Blueprint('rates', __name__, template_folder='./templates')


@rates_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        teachername = request.form['teachername']
        teacherlastname = request.form['teacherlastname']
        teachercareer = request.form['teachercareer']
        teacherfaculty = request.form['teacherfaculty']
        db.session.add(Teacher(
            teachername=teachername, teacherlastname=teacherlastname, 
            teachercareer=teachercareer, teacherfaculty=teacherfaculty
        ))
        db.session.commit()
    teachers = Teacher.query.all()
    return render_template('index.html', teachers=teachers)


@rates_blueprint.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


@rates_blueprint.route('/teachers', methods=['GET'])
def get_all_teachers():
    response_object = {
        'status': 'success',
        'data': {
            'teachers': [teacher.to_json() for teacher in Teacher.query.all()]
        }
    }
    return jsonify(response_object), 200


@rates_blueprint.route('/students', methods=['GET'])
def get_all_students():
    response_object = {
        'status': 'success',
        'data': {
            'students': [student.to_json() for student in Student.query.all()]
        }
    }
    return jsonify(response_object), 200


@rates_blueprint.route('/delete/<teacher_id>', methods=['POST', 'GET'])
def delete_teacher(teacher_id):
    teacher = Teacher.query.filter_by(id=int(teacher_id)).first()
    db.session.delete(teacher)
    db.session.commit()
    return redirect("/")


@rates_blueprint.route('/show/<teacher_id>', methods=['GET'])
def show_user(teacher_id):
    teacher = Teacher.query.filter_by(id=int(teacher_id)).first()
    return render_template('form.html', teacher=teacher)


@rates_blueprint.route('/update/<teacher_id>', methods=['POST', 'GET'])
def update_teacher(teacher_id):
    teacher = Teacher.query.filter_by(id=int(teacher_id)).first()
    teachername = request.form['teachername']
    teacherlastname = request.form['teacherlastname']
    teachercareer = request.form['teachercareer']
    teacherfaculty = request.form['teacherfaculty']

    teacher.teachername = teachername
    teacher.teacherlastname = teacherlastname
    teacher.teachercareer = teachercareer
    teacher.teacherfaculty = teacherfaculty

    db.session.commit()
    return redirect("/")

@rates_blueprint.route('/teachers', methods=['POST'])
def add_teacher():
    post_data = request.get_json()
    response_object = {
        'status': 'fail',
        'message': 'Invalid payload'
    }
    if not post_data:
        return jsonify(response_object), 400
    name = post_data.get('teachername')
    lastname = post_data.get('teacherlastname')
    career = post_data.get('teachercareer')
    faculty = post_data.get('teacherfaculty')
    db.session.add(
        Teacher(teachername=name, teacherlastname=lastname, teachercareer=career, teacherfaculty=faculty))
    db.session.commit()
    response_object['status'] = 'success'
    response_object['message'] = f'was added!'
    return jsonify(response_object), 201
