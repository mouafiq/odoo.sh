
[![Runboat](https://img.shields.io/badge/runboat-Try%20me-875A7B.png)](https://runboat.odoo-community.org/builds?repo=OCA/delivery-carrier&target_branch=13.0)
[![Pre-commit Status](https://github.com/OCA/delivery-carrier/actions/workflows/pre-commit.yml/badge.svg?branch=13.0)](https://github.com/OCA/delivery-carrier/actions/workflows/pre-commit.yml?query=branch%3A13.0)
[![Build Status](https://github.com/OCA/delivery-carrier/actions/workflows/test.yml/badge.svg?branch=13.0)](https://github.com/OCA/delivery-carrier/actions/workflows/test.yml?query=branch%3A13.0)
[![codecov](https://codecov.io/gh/OCA/delivery-carrier/branch/13.0/graph/badge.svg)](https://codecov.io/gh/OCA/delivery-carrier)
[![Translation Status](https://translation.odoo-community.org/widgets/delivery-carrier-13-0/-/svg-badge.svg)](https://translation.odoo-community.org/engage/delivery-carrier-13-0/?utm_source=widget)

<!-- /!\ do not modify above this line -->

# Carriers And Deliveries Management

This project aim to deal with modules related to manage carriers and deliveries in a generic way.

<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[base_delivery_carrier_files](base_delivery_carrier_files/) | 13.0.1.0.0 |  | Base module for creation of delivery carrier files
[base_delivery_carrier_label](base_delivery_carrier_label/) | 13.0.2.0.0 |  | Base module for carrier labels
[connector_routific](connector_routific/) | 13.0.1.0.0 | [![CarlosRoca13](https://github.com/CarlosRoca13.png?size=30px)](https://github.com/CarlosRoca13) | Connector for Routific Platform
[delivery_auto_refresh](delivery_auto_refresh/) | 13.0.1.0.7 |  | Auto-refresh delivery price in sales orders
[delivery_carrier_info](delivery_carrier_info/) | 13.0.1.0.0 |  | Add code and description on carrier
[delivery_carrier_multi_zip](delivery_carrier_multi_zip/) | 13.0.1.0.1 |  | Multiple ZIP intervals for the same delivery method
[delivery_carrier_partner](delivery_carrier_partner/) | 13.0.1.0.1 |  | Add a partner in the delivery carrier
[delivery_carrier_pricelist](delivery_carrier_pricelist/) | 13.0.1.0.0 |  | Compute method method fees based on the product's pricelist.
[delivery_carrier_service_level](delivery_carrier_service_level/) | 13.0.1.0.2 |  | Add service levels to carrier
[delivery_cttexpress](delivery_cttexpress/) | 13.0.1.0.0 |  | Delivery Carrier implementation for CTT Express API
[delivery_free_fee_removal](delivery_free_fee_removal/) | 13.0.1.0.3 |  | Hide free fee lines on sales orders
[delivery_local_pickup](delivery_local_pickup/) | 13.0.1.0.0 | [![victoralmau](https://github.com/victoralmau.png?size=30px)](https://github.com/victoralmau) | Delivery Local pickup
[delivery_multi_destination](delivery_multi_destination/) | 13.0.1.1.0 |  | Multiple destinations for the same delivery method
[delivery_package_fee](delivery_package_fee/) | 13.0.1.1.3 |  | Add fees on delivered packages on shipping methods
[delivery_package_number](delivery_package_number/) | 13.0.1.1.0 |  | Set or compute number of packages for a picking
[delivery_postlogistics](delivery_postlogistics/) | 13.0.1.2.1 |  | Print PostLogistics shipping labels using the Barcode web service
[delivery_postlogistics_server_env](delivery_postlogistics_server_env/) | 13.0.1.0.0 |  | Server Environment layer for Delivery Postlogistics
[delivery_price_method](delivery_price_method/) | 13.0.1.0.2 |  | Provides fields to be able to contemplate the tracking statesand also adds a global fields
[delivery_price_rule_volumetric_weight](delivery_price_rule_volumetric_weight/) | 13.0.2.0.0 | [![victoralmau](https://github.com/victoralmau.png?size=30px)](https://github.com/victoralmau) | Delivery Price Rule Volumetric weight
[delivery_purchase](delivery_purchase/) | 13.0.1.0.0 |  | Delivery costs in purchases
[delivery_schenker](delivery_schenker/) | 13.0.1.1.0 |  | Delivery Carrier implementation for DB Schenker API
[delivery_send_to_shipper_at_operation](delivery_send_to_shipper_at_operation/) | 13.0.1.0.0 |  | Send delivery notice to the shipper from any operation.
[delivery_sending](delivery_sending/) | 13.0.1.2.1 |  | Delivery Carrier implementation for Sending API
[delivery_state](delivery_state/) | 13.0.2.0.2 |  | Provides fields to be able to contemplate the tracking statesand also adds a global fields
[delivery_tnt_oca](delivery_tnt_oca/) | 13.0.1.1.1 | [![victoralmau](https://github.com/victoralmau.png?size=30px)](https://github.com/victoralmau) | Integrate TNT webservice
[delivery_ups_oca](delivery_ups_oca/) | 13.0.2.0.0 |  | Integrate UPS webservice
[partner_delivery_schedule](partner_delivery_schedule/) | 13.0.1.0.0 |  | Set on partners a schedule for delivery goods
[partner_delivery_zone](partner_delivery_zone/) | 13.0.1.1.1 |  | Set on partners a zone for delivery goods
[server_environment_delivery](server_environment_delivery/) | 13.0.1.0.0 |  | Configure prod environment for delivery carriers
[stock_picking_carrier_from_rule](stock_picking_carrier_from_rule/) | 13.0.1.0.0 |  | Set the carrier on picking if the stock rule used has a partner address set with a delivery method.
[stock_picking_delivery_link](stock_picking_delivery_link/) | 13.0.1.0.0 |  | Adds link to the delivery on all intermediate operations.
[stock_picking_report_delivery_cost](stock_picking_report_delivery_cost/) | 13.0.1.0.0 |  | Show delivery cost in delivery slip and picking operations reports

[//]: # (end addons)

<!-- prettier-ignore-end -->

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to Odoo Community Association (OCA)
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
OCA, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit
organization whose mission is to support the collaborative development of Odoo features
and promote its widespread use.
