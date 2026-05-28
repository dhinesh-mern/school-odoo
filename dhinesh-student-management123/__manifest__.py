{
    'name': 'dhinesh-student-management123',

    'version': '2.0',

    'summary': 'Student Management System',

    'description': """
Student Management Module for Odoo 17
====================================

Features:
- Student Records
- Student ID Generation
- Access Management
- Student Management Views
""",

    'author': 'Dhinesh Kumar',

    'website': 'https://github.com/dhinesh-mern',

    'category': 'Education',

    'license': 'LGPL-3',

    'price': 499.00,

    'currency': 'USD',

    'depends': ['base'],

    'data': [

        'security/ir.model.access.csv',

        'data/sequence.xml',

        'views/student_views.xml',

    ],

    'images': [
        'static/description/banner.png',
    ],

    'installable': True,

    'application': True,
}