{
    'name': 'LogiTrans',
    'version': '0.1',
    'summary': 'Gestión de logística y flota',
    'description': """
        Módulo LogiTrans
        Gestion de envios, vehiculos, y personal.
    """,
    'author': 'Guillermo Jiménez, Alan Fernández, Gabriela Celano',
    'category': 'Operations',
    'depends': ['base','base_address_city'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        #Vistas
        'views/vehiculo_views.xml',
        'views/mantenimiento_views.xml',
        'views/tipo_carga_views.xml',
        'views/vehiculo_tipo_carga_views.xml',
        "views/envios_views.xml",
        "views/rutas_views.xml",
        "views/ubicacion_views.xml",
        "views/report.xml",
        "views/report_envios.xml",
        "views/menu_views.xml",

        #Informes
        'reports/reports.xml',
        'reports/mantenimiento_report.xml',
        'reports/vehiculo_report.xml',

        #Datos DEMO
        'demo/demo.xml',
        
    ],
    
    'installable': True,
    'application': True,
}
