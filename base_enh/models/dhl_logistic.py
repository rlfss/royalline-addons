# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import Warning

class DHLLogistic(models.Model):
    _name='dhl.logistic'
    _description = "DHL Logistic"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
#   Shipment from fields  
    name = fields.Char(readonly=True)
    company_from_id = fields.Many2one('res.partner', string='Contact Name')
    date_from = fields.Datetime('Date Time Pick-Up')
    country_from_id = fields.Many2one('res.country', string="Country", related='company_from_id.country_id')
    state_from_id = fields.Many2one('res.country.state', string="State", related='company_from_id.state_id')
    city_from_id = fields.Many2one('res.city', string="City", related='company_from_id.city_id')
    phone_from = fields.Char(string='Phone', related='company_from_id.phone')
    add_one_from = fields.Char(string='Address (1)', related='company_from_id.street_name')
    add_two_from = fields.Char(string='Address (2)', related='company_from_id.street2')
    contact_person_from_ids = fields.One2many(comodel_name='res.partner',inverse_name='dhl_log_id', 
                                              related='company_from_id.child_ids')
    
    company_to_id = fields.Many2one('res.partner', string='Contact Name')
    country_to_id = fields.Many2one('res.country', string="Country", related='company_to_id.country_id')
    state_to_id = fields.Many2one('res.country.state', string="State", related='company_to_id.state_id')
    city_to_id = fields.Many2one('res.city', string="City", related='company_to_id.city_id')
    phone_to = fields.Char(string='Phone', related='company_to_id.phone')
    add_one_to = fields.Char(string='Address (1)', related='company_to_id.street_name')
    add_two_to = fields.Char(string='Address (2)', related='company_to_id.street2')
    space_btwn = fields.Char(string='     ')
    contact_person_to_ids = fields.One2many(comodel_name='res.partner',inverse_name='dhl_log_to_id', 
                                              related='company_to_id.child_ids')
    document_type_ids = fields.One2many(comodel_name='document.type', inverse_name='dhl_doc_id')
    
#     @api.multi
#     def name_get(self):
#         result = []
#         for record in self:
#             result.append((record.id, '%s | %s'%(record.company_from_id,record.country_from_id)))
#         return result
    @api.model_create_multi
    @api.returns('self', lambda value:value.id)
    def create(self, vals_list):
        for val in vals_list:
            val['name'] = self.env['ir.sequence'].next_by_code('courier.seq')
        return super(DHLLogistic, self).create(vals_list)
    
                
class DocumentType(models.Model):
    _name='document.type'
    _description = "Document Type"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    
    qty = fields.Integer(string='QTY', default='1')
    weight = fields.Float(default='0.5')
    dimensions_cm = fields.Char(default='47.50 x 38.00 x 1.00')
    dhl_doc_id = fields.Many2one('dhl.logistic')
    
    
    
    