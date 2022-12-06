import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-delivery-carrier",
    description="Meta package for oca-delivery-carrier Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-connector_routific>=15.0dev,<15.1dev',
        'odoo-addon-delivery_carrier_info>=15.0dev,<15.1dev',
        'odoo-addon-delivery_carrier_multi_zip>=15.0dev,<15.1dev',
        'odoo-addon-delivery_cttexpress>=15.0dev,<15.1dev',
        'odoo-addon-delivery_free_fee_removal>=15.0dev,<15.1dev',
        'odoo-addon-delivery_multi_destination>=15.0dev,<15.1dev',
        'odoo-addon-delivery_package_number>=15.0dev,<15.1dev',
        'odoo-addon-delivery_price_method>=15.0dev,<15.1dev',
        'odoo-addon-delivery_state>=15.0dev,<15.1dev',
        'odoo-addon-delivery_translatable>=15.0dev,<15.1dev',
        'odoo-addon-partner_delivery_schedule>=15.0dev,<15.1dev',
        'odoo-addon-partner_delivery_zone>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_delivery_link>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
