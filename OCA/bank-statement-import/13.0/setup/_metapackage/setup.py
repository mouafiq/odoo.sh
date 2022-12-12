import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-bank-statement-import",
    description="Meta package for oca-bank-statement-import Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-account_bank_statement_clear_partner',
        'odoo13-addon-account_bank_statement_import_camt_oca',
        'odoo13-addon-account_bank_statement_import_guess_partner',
        'odoo13-addon-account_bank_statement_import_move_line',
        'odoo13-addon-account_bank_statement_import_oca_camt54',
        'odoo13-addon-account_bank_statement_import_ofx',
        'odoo13-addon-account_bank_statement_import_online',
        'odoo13-addon-account_bank_statement_import_online_paypal',
        'odoo13-addon-account_bank_statement_import_online_ponto',
        'odoo13-addon-account_bank_statement_import_online_qonto',
        'odoo13-addon-account_bank_statement_import_online_transferwise',
        'odoo13-addon-account_bank_statement_import_paypal',
        'odoo13-addon-account_bank_statement_import_qif',
        'odoo13-addon-account_bank_statement_import_split',
        'odoo13-addon-account_bank_statement_import_transfer_move',
        'odoo13-addon-account_bank_statement_import_txt_xlsx',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 13.0',
    ]
)
