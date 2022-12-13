import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-manufacture-reporting",
    description="Meta package for oca-manufacture-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-mrp_bom_current_stock',
        'odoo13-addon-mrp_bom_matrix_report',
        'odoo13-addon-mrp_bom_structure_report_level_1',
        'odoo13-addon-mrp_bom_structure_xlsx',
        'odoo13-addon-mrp_bom_structure_xlsx_level_1',
        'odoo13-addon-mrp_flattened_bom_xlsx',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 13.0',
    ]
)
