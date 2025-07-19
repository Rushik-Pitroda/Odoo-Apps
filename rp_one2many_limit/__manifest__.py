# -*- coding: utf-8 -*-
{
    'name': "One2many Record Limit",
    'version' : '18.0.0.1',
    'summary': "Restrict the number of records allowed in One2many fields.",
    'description': """
            This module allows you to set a maximum record limit for One2many fields.
            🔧 How it works:
            - Select any model (e.g., Sale Order)
            - Choose its One2many fields
            - Set a maximum limit (e.g., 5)
            - The system will restrict creating more than that number of records
            - Works for any model and any One2many field
    """,
    'author': "Rushik Pitroda",
    'website': "https://www.odoo.com/profile/user/6107106", 
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    'application': True,
    'installable': True,
    'auto_install': False,
    'depends': ['base','web'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'images': ['static/description/icon.png'],
    'assets': {
        'web.assets_backend': [
            'rp_one2many_limit/static/src/xml/list_render_inherit.xml',
            'rp_one2many_limit/static/src/js/patch_listrender.js',
        ],
    },
}
