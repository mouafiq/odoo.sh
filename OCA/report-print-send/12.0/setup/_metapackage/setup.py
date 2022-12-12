import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-report-print-send",
    description="Meta package for oca-report-print-send Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-base_report_to_printer',
        'odoo12-addon-base_report_to_printer_mail',
        'odoo12-addon-printer_zpl2',
        'odoo12-addon-remote_report_to_printer',
        'odoo12-addon-server_env_printing_server',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
