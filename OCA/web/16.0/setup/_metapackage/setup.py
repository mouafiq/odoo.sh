import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-web",
    description="Meta package for oca-web Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-web_dark_mode>=16.0dev,<16.1dev',
        'odoo-addon-web_domain_field>=16.0dev,<16.1dev',
        'odoo-addon-web_environment_ribbon>=16.0dev,<16.1dev',
        'odoo-addon-web_refresher>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
