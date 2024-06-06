# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

from odoo import models, fields, api, _
from datetime import datetime, timedelta


class GitCommit(models.Model):
    _name = 'project.git.commit'
    _order = 'create_date DESC'

    name = fields.Char(
        string='Name',
        compute='_compute_name'
    )

    message = fields.Text(
        string='Message',
        required=True,
    )

    url = fields.Char(
        string='URL',
        required=True
    )

    hash = fields.Char(
        string='HASH',
        required=True
    )

    repository_id = fields.Many2one(
        'project.git.repository',
        'Repository',
        required=True
    )

    partner_id = fields.Many2one(
        'res.partner',
        'Owner',
        ondelete='cascade',
        default=lambda self: self.env.user.partner_id
    )

    def _compute_name(self):
        for rec in self:
            rec.name = rec.message and rec.message[:20] + '...' or ''

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('repository_id'):
                repository = self.env['project.git.repository'].browse(vals['repository_id'])
                repository.last_commit_date = fields.Datetime.now()
        return super().create(vals_list)
