import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-report-print-send",
    description="Meta package for oca-report-print-send Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-base_report_to_printer',
        'odoo13-addon-base_report_to_printer_mail',
        'odoo13-addon-printer_zpl2',
        'odoo13-addon-remote_report_to_printer',
        'odoo13-addon-stock_picking_auto_print',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 13.0',
    ]
)
