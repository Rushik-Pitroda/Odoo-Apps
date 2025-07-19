# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)

class One2ManyLimitController(http.Controller):
    @http.route('/get/limit',type='json', auth='user')
    def get_limit(self, field_name, field_model):
        _logger.info("Fetching limit for model: %s, field: %s", field_model, field_name)
        limit_record = request.env['x2many.limit'].search([
            ('models_name.model', '=', field_model),
            ('fields_list.name', '=', field_name)
        ], limit=1)
        
        _logger.info("return limit %s", limit_record.limit)
        if limit_record:
            return limit_record.limit
        return False