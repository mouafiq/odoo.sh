import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-event",
    description="Meta package for oca-event Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-crm_event',
        'odoo12-addon-crm_lead_to_event_registration',
        'odoo12-addon-event_activity',
        'odoo12-addon-event_contact',
        'odoo12-addon-event_email_reminder',
        'odoo12-addon-event_mail',
        'odoo12-addon-event_project',
        'odoo12-addon-event_registration_cancel_reason',
        'odoo12-addon-event_registration_mass_mailing',
        'odoo12-addon-event_registration_multi_qty',
        'odoo12-addon-event_registration_partner_unique',
        'odoo12-addon-event_sale_registration_multi_qty',
        'odoo12-addon-event_sale_reservation',
        'odoo12-addon-event_sale_session',
        'odoo12-addon-event_session',
        'odoo12-addon-event_session_registration_multi_qty',
        'odoo12-addon-event_track_location_overlap',
        'odoo12-addon-partner_event',
        'odoo12-addon-sale_crm_event_reservation',
        'odoo12-addon-website_event_crm',
        'odoo12-addon-website_event_excerpt_img',
        'odoo12-addon-website_event_filter_organizer',
        'odoo12-addon-website_event_filter_selector',
        'odoo12-addon-website_event_questions_free_text',
        'odoo12-addon-website_event_questions_template',
        'odoo12-addon-website_event_require_login',
        'odoo12-addon-website_event_sale_b2x_alt_price',
        'odoo12-addon-website_event_share',
        'odoo12-addon-website_event_snippet_calendar',
        'odoo12-addon-website_event_type_description',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
