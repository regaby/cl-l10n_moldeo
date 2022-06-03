{
    'name': 'l10n_moldeo_15',
    'version': '15.0.0.0',
    'category': 'Tools',
    'summary': "Proyecto Localización Argentina de Moldeo",
    'author': 'Ing. Gabriela Rivero',
    'depends': [
        'base',
    ],
    'data': [
    ],
    'installable': True,
    'application': False,

    'limit_request': '8196',
    'limit_memory_soft': '640000000',
    'limit_memory_hard': '760000000',
    'limit_time_cpu': '60',
    'limit_time_real': '120',

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'CE',

    # port where odoo starts serving pages
    'port': '8069',

    # list of url repos to install in the form 'repo-url directory'
    'git-repos': [
        'https://github.com/regaby/cl-l10n_moldeo.git',
        'https://github.com/regaby/odoo-custom.git -b 15.0-moldeo',
        'https://github.com/regaby/l10n_ar_fe_qr ctmil/l10n_ar_fe_qr',
        'https://github.com/regaby/odoo-argentina.git',
        'https://github.com/OCA/reporting-engine.git',
        'https://github.com/OCA/stock-logistics-warehouse.git',
        'https://github.com/odoo/design-themes.git',
    ],

    'docker-images': [
        'odoo regaby/odoo-ce:15.0',
        'postgres postgres:10.1-alpine',
    ]
}
