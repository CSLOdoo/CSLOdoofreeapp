# -*- coding: utf-8 -*-
{
    'name': 'CSL Import Sales Pricelist',
    'version': '17.0.0.1',
    'category': 'Sales',
    'sequence': 4,
    'summary': 'Sales Pricelist',
    'description': "",
    'author': 'Cloud Science Labs',
    'website': 'https://www.cloudsciencelabs.com',
    'depends': [
        'base','product','sale','sale_management',
    ],
    'data': [
        'security/user_groups.xml',
        'views/pricelist_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
