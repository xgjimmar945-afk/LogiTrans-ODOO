# -*- coding: utf-8 -*-
{
    'name': "logitrans",

    'summary': """
        Gestión y Logística de Transportes""",

    'description': """
        Módulo para la gestión de logística de los transportes
    """,

    'author': "Alan Fernandez Diosdado, Guillermo Jiménez Martínez, Gabriela María Celano Díaz",
    'website': "http://www.logitrans.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/conductor.xml',
        'views/administrativo.xml',
        'views/persona.xml',
        'views/informes.xml',
        'views/menu_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
