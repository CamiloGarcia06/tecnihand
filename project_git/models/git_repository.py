# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).


from odoo import models, fields, api
from datetime import datetime, timedelta
from collections import Counter
import csv
import base64
from io import StringIO


class GitRepository(models.Model):
    _name = 'project.git.repository'

    name = fields.Char(
        string='Name',
    )

    url = fields.Char(
        string='URL',
    )

    commit_ids = fields.One2many(
        'project.git.commit',
        'repository_id',
        string='Commits',)

    state = fields.Selection([
        ('inactive', 'Inactive'),
        ('active', 'Active'),
    ], 'inactive', default='inactive', copy=False)

    commit_count = fields.Integer(
        compute='_depends_commit_ids'
    )

    last_commit_date = fields.Datetime('last commit date', readonly=True)
    count_last_commit_date = fields.Integer(
        'Count last commit date', compute='_count_last_commit_date')
    days = fields.Boolean(compute='_count_last_commit_date')

    largest_contributor = fields.Many2one(
        'res.partner',
        'Largest Contributor',
        compute='_depends_commit_ids'
    )
    partner_id = fields.Many2one('res.partner', 'Partner')
    file_data = fields.Binary(string='File Data')

    @api.depends('commit_ids')
    def _depends_commit_ids(self):
        for rec in self:
            rec.commit_count = len(rec.commit_ids)
            partner_ids = [commit.partner_id for commit in rec.commit_ids]
            largest_contributor = False
            if partner_ids:
                contributor_counts = Counter(partner_ids)
                largest_contributor = contributor_counts.most_common(1)[0][0]
            rec.largest_contributor = largest_contributor

    @api.depends('last_commit_date')
    def _count_last_commit_date(self):
        for rec in self:
            last_date = rec.last_commit_date
            now = datetime.now()

            time_difference = now - last_date

            if time_difference < timedelta(days=1):
                hours = time_difference.total_seconds() // 3600
                rec.count_last_commit_date = hours
                rec.days = False
            else:
                days = time_difference.days
                rec.count_last_commit_date = days
                rec.days = True

    def button_activate(self):
        self.state = 'active'

    def button_generate_csv(self):
        csvfile = StringIO()
        fieldnames = ['Date', 'Responsible', 'Message', 'URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for commit in self.commit_ids:
            writer.writerow({
                'Date': commit.create_date,
                'Responsible': commit.partner_id.name,
                'Message': commit.message,
                'URL': commit.url
            })

            # Get CSV content as bytes
        csv_content = csvfile.getvalue().encode('utf-8')

        # Encode to base64 to store in binary field
        self.file_data = base64.b64encode(csv_content)
        return {
            'type': 'ir.actions.act_url',
            'url': 'web/content/?model=project.git.repository&id=%s&field=file_data&download=true&filename=%s' % (self.id, 'commits.csv'),
            'target': 'new',
        }
