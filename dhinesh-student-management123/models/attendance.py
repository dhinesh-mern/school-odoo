from odoo import models, fields


class StudentAttendance(models.Model):
    _name = 'student.attendance'
    _description = 'Attendance'

    student_id = fields.Many2one(
        'student.student',
        required=True
    )

    date = fields.Date()

    status = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent')
    ], default='present')