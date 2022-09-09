# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Library Management',
    'version' : '1.1',
    'summary': 'Library Management',
    'sequence': 10,
    'description': """Library Management""",
    'depends' : ['base','mail'],
    'data': ['security/ir.model.access.csv',
             'views/visitor.xml',
             'views/library_management.xml',
             'views/librarian.xml',
             'views/book.xml'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
