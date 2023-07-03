{
    'name': 'Website Noindex',
    'description': 'Add noindex tag to website pages',
    'version': '1.0',
    'author': 'Your Name',
    'category': 'Website',
    'depends': ['website'],
    'data': [
    'security/ir.model.access.csv',  # add this line
    'views/website_noindex_views.xml',
    'views/website_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
}
