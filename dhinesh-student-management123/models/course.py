from odoo import models, fields


class StudentCourse(models.Model):
    _name = 'student.course'
    _description = 'Course'

    name = fields.Char(required=True)

    code = fields.Char()

    duration = fields.Integer()

    student_ids = fields.One2many(
        'student.student',
        'course_id'
    )