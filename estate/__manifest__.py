# -*- coding: utf-8 -*-

{
    'name': 'estate',
    'depends': [
        'base_setup',
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ],
    'application': True,
}