import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-multi-company",
    description="Meta package for oca-multi-company Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-account_invoice_consolidated',
        'odoo14-addon-account_invoice_inter_company',
        'odoo14-addon-account_invoice_inter_company_queued',
        'odoo14-addon-account_invoice_inter_company_sale',
        'odoo14-addon-account_multicompany_easy_creation',
        'odoo14-addon-account_payment_other_company',
        'odoo14-addon-base_multi_company',
        'odoo14-addon-company_dependent_attribute',
        'odoo14-addon-intercompany_shared_contact',
        'odoo14-addon-mail_multicompany',
        'odoo14-addon-mail_template_multi_company',
        'odoo14-addon-partner_contact_company_propagation',
        'odoo14-addon-product_category_inter_company',
        'odoo14-addon-product_multi_company',
        'odoo14-addon-product_supplierinfo_group_intercompany',
        'odoo14-addon-product_supplierinfo_intercompany',
        'odoo14-addon-product_tax_multicompany_default',
        'odoo14-addon-purchase_quick_intercompany',
        'odoo14-addon-purchase_sale_inter_company',
        'odoo14-addon-res_company_code',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
