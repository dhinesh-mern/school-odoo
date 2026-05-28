from odoo import models, fields


class StudentDepartment(models.Model):
    _name = 'student.department'
    _description = 'Department'

    name = fields.Char(required=True)

    hod_name = fields.Char()

    student_ids = fields.One2many(
        'student.student',
        'department_id'
    )