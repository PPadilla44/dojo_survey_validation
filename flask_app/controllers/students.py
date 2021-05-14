from flask_app import app
from flask import render_template,redirect,request,session,flash

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.student import Student

@app.route("/")
def show_form():
    return render_template("index.html")

@app.route("/result", methods=['POST'])
def show_result():

    if not Student.validate_student(request.form):
        return redirect('/')
    
    student = Student.create(request.form)
    print(student)
    return redirect(f"/results/{student}")

@app.route('/results/<dojoid>')
def show_student(dojoid):
    data = {
        'id': dojoid
    }
    return render_template('result.html', student=Student.show(data))