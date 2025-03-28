{
    'name': 'Cloud Management',
    'version': '1.0',
    'author': 'Alondra Gutierrez',
    'category': 'Management',
    'summary': 'Gestiona información de Data Centers, SLA, Pagos, Cloud y Soluciones',
    'description': """
        Este módulo permite gestionar información de:
        - Data Centers
        - SLA (Service Level Agreement)
        - Tipos de Pagos
        - Cloud Powerback
        - Soluciones
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/data_center_views.xml',
        'views/sla_views.xml',
        'views/payment_type_views.xml',
        'views/cloud_powerback_views.xml',
        'views/solution_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
