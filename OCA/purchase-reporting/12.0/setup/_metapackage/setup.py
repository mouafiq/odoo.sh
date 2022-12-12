import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-purchase-reporting",
    description="Meta package for oca-purchase-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-purchase_backorder',
        'odoo12-addon-purchase_comment_template',
        'odoo12-addon-purchase_report_extension',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
