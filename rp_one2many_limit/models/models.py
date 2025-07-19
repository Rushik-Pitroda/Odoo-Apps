# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class X2manyLimit(models.Model):
    _name = 'x2many.limit'
    _description = 'X2Many Limit'
    _rec_name = 'models_name'
    
    models_name = fields.Many2one('ir.model',string="Select Model")
    fields_list = fields.Many2many('ir.model.fields', string="Select Fields")
    fields_list_domain = fields.Binary(default=[])
    limit = fields.Integer(string="Limit", help="Maximum number of records allowed in the one2many field")

    @api.constrains('limit','fields_list')
    def _check_limit(self):
        for record in self:
            if not record.fields_list:
                raise models.ValidationError("Please select at least one field.")
            if record.limit <= 0:
                raise models.ValidationError("Limit must be a positive integer.")
            

    @api.onchange('models_name')
    def _onchange_models_name(self):
        for res in self: 
            if res.models_name:
                res.fields_list_domain = [
                    ('model', '=', res.models_name.model),('ttype', '=', 'one2many')
                ]
                res.fields_list = self.env['ir.model.fields'].search([
                  ('model', '=', res.models_name.model),('ttype', '=', 'one2many')  
                ])
                _logger.info("Fields List Domain Field Updated : %s", res.fields_list_domain)