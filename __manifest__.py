# -*- coding: utf-8 -*-
{
    'name': "odoo_musica",

    'summary': """
        Música""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Antonio Crespo Riveira. IES Teis",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/interprete.xml',
        'views/cancion.xml',
        'views/album.xml',
        'views/menu.xml',
        'views/templates.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}