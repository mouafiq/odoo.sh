import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-account-payment",
    description="Meta package for oca-account-payment Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-account_check_printing_report_base>=15.0dev,<15.1dev',
        'odoo-addon-account_due_list>=15.0dev,<15.1dev',
        'odoo-addon-account_due_list_payment_mode>=15.0dev,<15.1dev',
        'odoo-addon-account_payment_batch_process>=15.0dev,<15.1dev',
        'odoo-addon-account_payment_notification>=15.0dev,<15.1dev',
        'odoo-addon-account_payment_promissory_note>=15.0dev,<15.1dev',
        'odoo-addon-account_payment_term_extension>=15.0dev,<15.1dev',
        'odoo-addon-account_payment_term_partner_holiday>=15.0dev,<15.1dev',
        'odoo-addon-account_payment_widget_amount>=15.0dev,<15.1dev',
        'odoo-addon-partner_aging>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
