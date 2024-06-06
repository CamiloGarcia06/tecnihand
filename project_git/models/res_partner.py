# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    repository_ids = fields.One2many(
        'project.git.repository',
        'partner_id',
        'repositorys',
        readonly=True
    )