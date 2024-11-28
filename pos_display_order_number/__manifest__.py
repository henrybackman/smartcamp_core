# Copyright 2024 Camptocamp SA (https://www.camptocamp.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "POS Display Order Number",
    "summary": "POS - Display order number in order summary",
    "version": "17.0.1.0.1",
    "development_status": "Beta",
    "category": "Point Of Sale",
    "website": "https://github.com/OCA/pos",
    "author": "Camptocamp, Odoo Community Association (OCA)",
    "maintainers": ["henrybackman"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["pos_divide_order_summary"],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_display_order_number/static/src/xml/pos_display_order_number.xml",
            "pos_display_order_number/static/src/js/overrides/components/order_widget/order_widget.js",
        ],
    },
    "sequence": 30,
}