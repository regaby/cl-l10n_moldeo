{
    'name': 'l10n_moldeo',
    'version': '13.0.0.0',
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
        'https://github.com/regaby/odoo-custom.git',
        ## localización
        'https://github.com/ctmil/odoo-argentina.git',
        #'https://github.com/ingadhoc/odoo-argentina-ee.git',
        'https://github.com/ingadhoc/product.git ingadhoc-product',
        'https://github.com/OCA/reporting-engine.git oca-reporting-engine',
        'https://github.com/OCA/brand.git oca-brand',
        'https://github.com/OCA/pos.git oca-pos',
        'https://github.com/OCA/product-attribute.git oca-product-attribute',
        'https://github.com/OCA/web.git oca-web',
        ## itpp-labs
        'https://github.com/itpp-labs/pos-addons.git',
        ## contract
        'https://github.com/ctmil/contract.git ctmil/contract',
        'https://github.com/regaby/l10n_ar_fe_qr ctmil/l10n_ar_fe_qr',
        'https://github.com/jcelguerablas/odoo.git jcelguerablas',
        'https://github.com/CybroOdoo/CybroAddons.git',
        'https://github.com/regaby/mercadopago.git',
    ],

    'docker-images': [
        'odoo regaby/odoo-ce:13.0',
        'postgres postgres:10.1-alpine',
        'nginx nginx'
    ]
}
