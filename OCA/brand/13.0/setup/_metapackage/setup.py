import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-brand",
    description="Meta package for oca-brand Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-account_brand',
        'odoo13-addon-analytic_brand',
        'odoo13-addon-brand',
        'odoo13-addon-brand_external_report_layout',
        'odoo13-addon-brand_stock_account',
        'odoo13-addon-contract_brand',
        'odoo13-addon-pricelist_brand',
        'odoo13-addon-product_brand',
        'odoo13-addon-product_brand_purchase_report',
        'odoo13-addon-project_task_brand',
        'odoo13-addon-sale_brand',
        'odoo13-addon-sale_timesheet_brand',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 13.0',
    ]
)
