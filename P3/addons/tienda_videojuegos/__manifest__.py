# -*- coding: utf-8 -*-
{
    'name': "Tienda de Videojuegos",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,
    'application': True,
    'author': "Vicente Izquierdo",
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/tienda_videojuegos.xml',
        'views/tienda_publisher.xml'
    ],
}
