from odoo import models, fields

class WebsiteNoindexLog(models.Model):
    _name = 'website.noindex.log'

    page_url = fields.Char(string="Page URL", required=True)
    has_noindex = fields.Boolean(string="Has Noindex")
    check_date = fields.Datetime(string="Check Date", default=fields.Datetime.now)
