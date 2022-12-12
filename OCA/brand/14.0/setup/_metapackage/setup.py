import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-brand",
    description="Meta package for oca-brand Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-account_brand',
        'odoo14-addon-analytic_brand',
        'odoo14-addon-brand',
        'odoo14-addon-brand_external_report_layout',
        'odoo14-addon-contract_brand',
        'odoo14-addon-product_brand',
        'odoo14-addon-product_brand_multicompany',
        'odoo14-addon-product_brand_social_responsibility',
        'odoo14-addon-product_brand_tag',
        'odoo14-addon-product_brand_tag_secondary',
        'odoo14-addon-sale_brand',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
