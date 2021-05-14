from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Student:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate_student(student):
        is_valid = True
        if len(student['name']) < 1:
            flash("Must enter Name")
            is_valid = False
        return is_valid
    
    @classmethod
    def create(cls,data):
        query = "INSERT INTO dojos (name,location,language,comment,created_at,updated_at) \
        VALUES (%(name)s,%(location)s,%(language)s,%(comment)s,NOW(),NOW());"
        return connectToMySQL('dojo_survey_schema').query_db(query,data)
    
    @classmethod
    def show(cls,data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojo_survey_schema').query_db(query,data)
        return cls(results[0])
