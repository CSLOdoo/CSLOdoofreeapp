# -- encoding: utf-8 --
##############################################################################
#
#    Cloud Science Labs
#    Copyright (C) 2024 (https://www.cloudsciencelabs.com/)
#
##############################################################################
from odoo import api, fields, models, _


class Sales_pricelist_line(models.Model):
    _inherit = 'product.pricelist.item'

    applied_on = fields.Selection([
        ('3_global', 'All Products'),
        ('2_product_category', 'Product Category'),
        ('1_product', 'Product'),
        ('0_product_variant', 'Product Variant')], "Apply On",
        default='1_product', required=True,
        help='Pricelist Item applicable on selected option')