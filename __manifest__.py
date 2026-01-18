{
    'name': 'LogiTrans',
    'version': '0.1',
    'summary': 'Gestión de logística y flota',
    'description': """
        Módulo LogiTrans
        Gestión de vehículos, mantenimiento y tipos de carga.
    """,
    'author': 'Equipo LogiTrans',
    'category': 'Operations',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/vehiculo_views.xml',
        'views/mantenimiento_views.xml',
        'views/tipo_carga_views.xml',
        'views/vehiculo_tipo_carga_views.xml'
    ],
    'demo': [
    'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}