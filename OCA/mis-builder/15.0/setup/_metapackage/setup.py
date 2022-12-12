import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-mis-builder",
    description="Meta package for oca-mis-builder Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-mis_builder>=15.0dev,<15.1dev',
        'odoo-addon-mis_builder_budget>=15.0dev,<15.1dev',
        'odoo-addon-mis_builder_demo>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
