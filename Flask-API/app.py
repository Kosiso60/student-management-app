from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from app import api, app
from app.resources import Index
from app.resources.auth import UserLogin, UserRegister
from app.resources.students import StudentListAPI, StudentAPI
from app.resources.lecturers import TeacherListAPI, TeacherAPI
from app.resources.courses import SubjectListAPI, SubjectAPI

api.add_resource(Index, "")
api.add_resource(UserRegister, "/auth/register")
api.add_resource(UserLogin, "/auth/login")
api.add_resource(StudentListAPI, "/students")
api.add_resource(StudentAPI, "/students/<string:id>")
api.add_resource(TeacherListAPI, "/lecturers")
api.add_resource(TeacherAPI, "/lecturers/<string:id>")
api.add_resource(SubjectListAPI, "/courses")
api.add_resource(SubjectAPI, "/courses/<string:id>")



if __name__ == "__main__":
    # app = create_app()
    app.run(debug=True)


#from flask import Flask   
        # import flask
#app = Flask(__name__)             # create an app instance

#@app.route("/")                   # at the end point /
# def hello():                      # call method hello
#     return "Hello World!"         # which returns "hello world"
# if __name__ == "__main__":        # on running python app.py
#     app.run(debug=True)                    # run the flask app