import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-stock-logistics-workflow",
    description="Meta package for oca-stock-logistics-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-stock_move_line_auto_fill>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_auto_create_lot>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_back2draft>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_sale_order_link>=16.0dev,<16.1dev',
        'odoo-addon-stock_putaway_hook>=16.0dev,<16.1dev',
        'odoo-addon-stock_quant_package_dimension>=16.0dev,<16.1dev',
        'odoo-addon-stock_quant_package_product_packaging>=16.0dev,<16.1dev',
        'odoo-addon-stock_receipt_lot_info>=16.0dev,<16.1dev',
        'odoo-addon-stock_restrict_lot>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
