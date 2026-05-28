{
    'name': 'Student Management',

    'version': '2.0',

    'depends': ['base'],

    'data': [

        'security/ir.model.access.csv',

        'data/sequence.xml',

        'views/student_views.xml',

    ],

    'installable': True,

    'application': True,
}