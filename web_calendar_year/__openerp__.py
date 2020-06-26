# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Onestein (<http://www.onestein.nl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': "Web Calendar Year",
    'images': ['static/description/main_screenshot.png'],
    'summary': """Year view on Odoo calendar""",
    'description': """
Year calendar view
==================
Extends the default calendar widget with a year view.
""",
    'author': "Onestein",
    'website': "http://www.onestein.eu",
    'category': 'Extra Tools',
    'version': '1.0',
    'depends': ['web_calendar'],
    'data': [
        'views/web_calendar_year.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
