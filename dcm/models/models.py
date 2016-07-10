# -*- coding: utf-8 -*-

from openerp import models, fields, api
from odoo.tools import html2plaintext

class Question(models.Model):
    _name = 'dcm.question'
    # _inherit = ['mail.thread']
    _description = "Question"

    name       = fields.Text(compute='_compute_name', string='Question Summary', store=True)
    user_id    = fields.Many2one('res.users', string='Owner', default=lambda self: self.env.uid)
    memo       = fields.Html('Question Content')

    @api.depends('memo')
    def _compute_name(self):
        """ Read the first line of the memo to determine the question name """
        for question in self:
            text = html2plaintext(question.memo) if question.memo else ''
            question.name = text.strip().replace('*', '').split("\n")[0]
