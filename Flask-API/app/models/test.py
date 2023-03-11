# from flask import Flask
# from flask_restx import Api, Resource, fields
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
# db = SQLAlchemy(app)

# api = Api(app, version='1.0', title='Student Management API', description='A simple student management API')

# student_model = api.model('Student', {
#     'id': fields.Integer(readonly=True, description='The student unique identifier'),
#     'name': fields.String(required=True, description='The student name'),
#     'email': fields.String(required=True, description='The student email'),
#     'phone': fields.String(required=True, description='The student phone number')
# })

# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(50), nullable=False)
#     phone = db.Column(db.String(20), nullable=False)
#     courses = db.relationship('Course', backref='student', lazy=True)

# class Course(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

# @api.route('/students')
# class StudentList(Resource):
#     @api.doc('list_students')
#     @api.marshal_list_with(student_model)
#     def get(self):
#         students = Student.query.all()
#         return students, 200

#     @api.doc('create_student')
#     @api.expect(student_model)
#     @api.marshal_with(student_model, code=201)
#     def post(self):
#         data = api.payload
#         student = Student(name=data['name'], email=data['email'], phone=data['phone'])
#         db.session.add(student)
#         db.session.commit()
#         return student, 201

# @api.route('/students/<int:id>')
# class StudentDetail(Resource):
#     @api.doc('get_student')
#     @api.marshal_with(student_model)
#     def get(self, id):
#         student = Student.query.get_or_404(id)
#         return student, 200

#     @api.doc('update_student')
#     @api.expect(student_model)
#     @api.marshal_with(student_model)
#     def put(self, id):
#         student = Student.query.get_or_404(id)
#         data = api.payload
#         student.name = data['name']
#         student.email = data['email']
#         student.phone = data['phone']
#         db.session.commit()
#         return student, 200

#     @api.doc('delete_student')
#     @api.response(204, 'Student deleted')
#     def delete(self, id):
#         student = Student.query.get_or_404(id)
#         db.session.delete(student)
#         db.session.commit()
#         return '', 204

# if __name__ == '__main__':
#     app.run(debug=True)
