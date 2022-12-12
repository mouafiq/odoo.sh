import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-l10n-belgium",
    description="Meta package for oca-l10n-belgium Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-account_statement_import_coda',
        'odoo14-addon-companyweb_base',
        'odoo14-addon-companyweb_payment_info',
        'odoo14-addon-l10n_be_cooperator',
        'odoo14-addon-l10n_be_intrastat_product',
        'odoo14-addon-l10n_be_mis_reports',
        'odoo14-addon-l10n_be_partner_kbo_bce',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
