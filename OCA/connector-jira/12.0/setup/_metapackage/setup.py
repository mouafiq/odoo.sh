import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-connector-jira",
    description="Meta package for oca-connector-jira Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-connector_jira',
        'odoo12-addon-connector_jira_tempo',
        'odoo12-addon-connector_jira_tempo_base',
        'odoo12-addon-connector_jira_tempo_project_role',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
