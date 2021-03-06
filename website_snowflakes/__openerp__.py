# -*- coding: utf-8 -*-
# Copyright 2016 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Website Snowflakes',
    'images': [],
    'summary': '''Christmas landscape on your Odoo Website''',
    'license': 'AGPL-3',
    'author': 'Onestein',
    'website': 'http://www.onestein.eu',
    'category': 'Web',
    'version': '8.0.1.0.0',
    'depends': [
        'web_snowflakes',
        'website',
    ],
    'data': [
        'views/web_snowflakes.xml',
        'views/web_layout.xml',
    ],
    'auto_install': True,
}
