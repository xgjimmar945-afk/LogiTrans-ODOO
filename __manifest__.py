{
    "name": "LogiTrans",
    "summary": """Gestion del modulo LogiTrans""",
    "description": """Gestion de envios, vehiculos, conductores, etc""",
    "author": "Guillermo Jiménez, Alan Fernández, Gabriela Celano",
    "category": "Uncategorized",
    "version": "0.1",
    "depends": ["base", "base_address_city"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/envios_views.xml",
        "views/rutas_views.xml",
        "views/ubicacion_views.xml",
        "views/report.xml",
        "views/report_envios.xml",
        "views/menu_views.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],
    "application": True,
}
