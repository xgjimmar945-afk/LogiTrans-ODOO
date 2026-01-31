{
    "name": "LogiTrans",
    "version": "0.1",
    "summary": "Gestión de logística y flota",
    "description": """
        Módulo LogiTrans
        Gestion de envios, vehiculos, y personal.
    """,
    "author": "Guillermo Jiménez, Alan Fernández, Gabriela Celano",
    "category": "Operations",
    "depends": ["base"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "reports/reports.xml",
        # Vistas
        "views/conductor.xml",
        "views/administrativo.xml",
        "views/persona.xml",
        "views/vehiculo_views.xml",
        "views/mantenimiento_views.xml",
        "views/tipo_carga_views.xml",
        "views/vehiculo_tipo_carga_views.xml",
        "views/envios_views.xml",
        "views/rutas_views.xml",
        "views/ubicacion_views.xml",
        "views/menu_views.xml",
        # Informes
        "reports/report_plantilla.xml",
        "reports/mantenimiento_report.xml",
        "reports/vehiculo_report.xml",
        "reports/report_envios.xml",
        # Datos DEMO
        "demo/demo.xml",
    ],
    "installable": True,
    "application": True,
}
