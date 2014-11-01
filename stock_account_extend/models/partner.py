# -*- coding: utf-8 -*-
###############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2014-Today Trey, Kilobytes de Soluciones <www.trey.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from openerp import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    picking_to_invoice = fields.Float(
        string='Total',
        compute='compute_picking_to_invoice')

    @api.one
    def compute_picking_to_invoice(self):
        picking_ob = self.env['stock.picking']
        self.picking_to_invoice = 0
        for picking in picking_ob.search([('partner_id', '=', self.id)]):
            self.picking_to_invoice += picking.invoice_total
