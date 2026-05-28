from odoo import models, fields


class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'

    student_id = fields.Char(string="Student ID")

    name = fields.Char(string="Name")

    age = fields.Integer(string="Age")

    course = fields.Char(string="Course")