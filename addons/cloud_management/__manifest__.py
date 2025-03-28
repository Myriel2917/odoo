{
    'name': 'Cloud Management',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Manage Cloud PowerBack and Solutions',
    'description': """
        Cloud Management Module
        - Manage Data Centers
        - Manage SLA
        - Manage Payment Types
        - Manage Cloud PowerBack
        - Manage Solutions
    """,
    'author': 'Alondra Gutierrez',
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
