{
    'name': 'POS Discount Fixed',
    'author': 'technoindo.com',
    'version': '1.1',
    'category': 'Point Of Sale',
    'description': """
Modul POS Discount Fixed Flectra
""",
    'depends': ['point_of_sale', 'pos_discount'],
    'data': [
        'views/pos_discount_fixed_templates.xml',
    ],
    'qweb': [
        'static/src/xml/pos_discount_fixed.xml',
    ],
    'installable': True,
    'auto_install': False,
}