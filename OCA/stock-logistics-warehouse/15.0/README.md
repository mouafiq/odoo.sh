
[![Runboat](https://img.shields.io/badge/runboat-Try%20me-875A7B.png)](https://runboat.odoo-community.org/builds?repo=OCA/stock-logistics-warehouse&target_branch=15.0)
[![Pre-commit Status](https://github.com/OCA/stock-logistics-warehouse/actions/workflows/pre-commit.yml/badge.svg?branch=15.0)](https://github.com/OCA/stock-logistics-warehouse/actions/workflows/pre-commit.yml?query=branch%3A15.0)
[![Build Status](https://github.com/OCA/stock-logistics-warehouse/actions/workflows/test.yml/badge.svg?branch=15.0)](https://github.com/OCA/stock-logistics-warehouse/actions/workflows/test.yml?query=branch%3A15.0)
[![codecov](https://codecov.io/gh/OCA/stock-logistics-warehouse/branch/15.0/graph/badge.svg)](https://codecov.io/gh/OCA/stock-logistics-warehouse)
[![Translation Status](https://translation.odoo-community.org/widgets/stock-logistics-warehouse-15-0/-/svg-badge.svg)](https://translation.odoo-community.org/engage/stock-logistics-warehouse-15-0/?utm_source=widget)

<!-- /!\ do not modify above this line -->

# stock-logistics-warehouse

TODO: add repo description.

<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[account_move_line_product](account_move_line_product/) | 15.0.1.0.1 |  | Displays the product in the journal entries and items
[account_move_line_stock_info](account_move_line_stock_info/) | 15.0.1.0.0 |  | Account Move Line Stock Info
[procurement_auto_create_group](procurement_auto_create_group/) | 15.0.1.0.0 |  | Allows to configure the system to propose automatically new procurement groups during the procurement run.
[sale_stock_available_info_popup](sale_stock_available_info_popup/) | 15.0.1.0.0 |  | Adds an 'Available to promise' quantity to the popover shown in sale order line that display stock info of the product
[scrap_reason_code](scrap_reason_code/) | 15.0.1.0.1 | [![bodedra](https://github.com/bodedra.png?size=30px)](https://github.com/bodedra) | Reason code for scrapping
[stock_archive_constraint](stock_archive_constraint/) | 15.0.1.0.1 | [![victoralmau](https://github.com/victoralmau.png?size=30px)](https://github.com/victoralmau) | Stock archive constraint
[stock_available](stock_available/) | 15.0.1.0.0 |  | Stock available to promise
[stock_available_mrp](stock_available_mrp/) | 15.0.1.0.1 |  | Consider the production potential is available to promise
[stock_available_unreserved](stock_available_unreserved/) | 15.0.1.0.0 | [![LoisRForgeFlow](https://github.com/LoisRForgeFlow.png?size=30px)](https://github.com/LoisRForgeFlow) | Quantity of stock available for immediate use
[stock_demand_estimate](stock_demand_estimate/) | 15.0.1.0.1 |  | Allows to create demand estimates.
[stock_demand_estimate_matrix](stock_demand_estimate_matrix/) | 15.0.1.1.1 |  | Allows to create demand estimates.
[stock_helper](stock_helper/) | 15.0.1.0.0 |  | Add methods shared between various stock modules
[stock_location_lockdown](stock_location_lockdown/) | 15.0.1.0.1 |  | Prevent to add stock on locked locations
[stock_location_route_description](stock_location_route_description/) | 15.0.1.0.0 |  | Add description field on stock routes.
[stock_lot_filter_available](stock_lot_filter_available/) | 15.0.1.0.0 | [![CarlosRoca13](https://github.com/CarlosRoca13.png?size=30px)](https://github.com/CarlosRoca13) | Allow to filter lots by available on stock
[stock_move_location](stock_move_location/) | 15.0.1.0.2 |  | This module allows to move all stock in a stock location to an other one.
[stock_mts_mto_rule](stock_mts_mto_rule/) | 15.0.1.0.1 |  | Add a MTS+MTO route
[stock_orderpoint_move_link](stock_orderpoint_move_link/) | 15.0.1.0.0 |  | Link Reordering rules to stock moves
[stock_orderpoint_purchase_link](stock_orderpoint_purchase_link/) | 15.0.1.0.0 |  | Link Reordering rules to purchase orders
[stock_orderpoint_uom](stock_orderpoint_uom/) | 15.0.1.0.0 |  | Allows to create procurement orders in the UoM indicated in the orderpoint
[stock_packaging_calculator](stock_packaging_calculator/) | 15.0.1.0.0 |  | Compute product quantity to pick by packaging
[stock_putaway_product_template](stock_putaway_product_template/) | 15.0.1.0.1 | [![kevinkhao](https://github.com/kevinkhao.png?size=30px)](https://github.com/kevinkhao) [![sebastienbeau](https://github.com/sebastienbeau.png?size=30px)](https://github.com/sebastienbeau) | Add product template in putaway strategies from the product view
[stock_quant_manual_assign](stock_quant_manual_assign/) | 15.0.1.2.1 |  | Stock - Manual Quant Assignment
[stock_request](stock_request/) | 15.0.1.0.3 |  | Internal request for stock
[stock_request_purchase](stock_request_purchase/) | 15.0.1.0.1 |  | Internal request for stock
[stock_reserve](stock_reserve/) | 15.0.1.0.1 |  | Stock reservations on products
[stock_secondary_unit](stock_secondary_unit/) | 15.0.1.0.0 |  | Get product quantities in a secondary unit
[stock_warehouse_calendar](stock_warehouse_calendar/) | 15.0.1.0.0 | [![JordiBForgeFlow](https://github.com/JordiBForgeFlow.png?size=30px)](https://github.com/JordiBForgeFlow) | Adds a calendar to the Warehouse

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
