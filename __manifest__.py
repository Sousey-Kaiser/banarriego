# -*- coding: utf-8 -*-
{
    'name': "h4o_banariego",

    'summary': """
        Modulo Visual Actualizado para Banarriego""",

    'description': """
        paquete de visuales para sitio web banarriego
    """,

    'author': "H4O-Studio",
    'website': "http://www.h4o-studio.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Modulos_Visuales',
    'version': '1.6',

    # any module necessary for this one to work correctly
    'depends': ['base','website','theme_clarico_vega'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates/assets.xml',
        'views/views.xml',
        'views/templates.xml',
        'templates/bana_home.xml',
        'templates/bana_nosotros.xml',
        'templates/bana_proyectos.xml',
        'templates/bana_servicios.xml',
        'templates/bana_contact.xml',
        'templates/bana_sucursales.xml',
        'templates/bana_insucursales.xml',
        'templates/bana_tree_block.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
