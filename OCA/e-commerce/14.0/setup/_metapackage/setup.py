import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-e-commerce",
    description="Meta package for oca-e-commerce Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-product_template_multi_link',
        'odoo14-addon-product_template_multi_link_date_span',
        'odoo14-addon-product_variant_multi_link',
        'odoo14-addon-website_sale_attribute_filter_form_submit',
        'odoo14-addon-website_sale_attribute_filter_multiselect',
        'odoo14-addon-website_sale_attribute_filter_price',
        'odoo14-addon-website_sale_b2x_alt_price',
        'odoo14-addon-website_sale_cart_expire',
        'odoo14-addon-website_sale_category_breadcrumb',
        'odoo14-addon-website_sale_checkout_country_vat',
        'odoo14-addon-website_sale_checkout_skip_payment',
        'odoo14-addon-website_sale_delivery_group',
        'odoo14-addon-website_sale_hide_price',
        'odoo14-addon-website_sale_order_type',
        'odoo14-addon-website_sale_product_assortment',
        'odoo14-addon-website_sale_product_attribute_filter_category',
        'odoo14-addon-website_sale_product_attribute_filter_visibility',
        'odoo14-addon-website_sale_product_attribute_value_filter_existing',
        'odoo14-addon-website_sale_product_brand',
        'odoo14-addon-website_sale_product_description',
        'odoo14-addon-website_sale_product_detail_attribute_image',
        'odoo14-addon-website_sale_product_detail_attribute_value_image',
        'odoo14-addon-website_sale_product_minimal_price',
        'odoo14-addon-website_sale_require_legal',
        'odoo14-addon-website_sale_show_company_data',
        'odoo14-addon-website_sale_stock_available',
        'odoo14-addon-website_sale_stock_provisioning_date',
        'odoo14-addon-website_sale_suggest_create_account',
        'odoo14-addon-website_sale_tax_toggle',
        'odoo14-addon-website_sale_wishlist_keep',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
