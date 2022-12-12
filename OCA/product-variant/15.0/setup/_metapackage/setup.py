import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-product-variant",
    description="Meta package for oca-product-variant Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-product_variant_configurator>=15.0dev,<15.1dev',
        'odoo-addon-product_variant_configurator_manual_creation>=15.0dev,<15.1dev',
        'odoo-addon-product_variant_sale_price>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_line_variant_description>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
