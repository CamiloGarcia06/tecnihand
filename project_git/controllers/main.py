from odoo import http
from odoo.http import request
import json


class RepositoryController(http.Controller):

    @http.route('/api/repositories/<int:partner_id>',
                auth="public",
                website=False,
                type="http",
                csrf=False,
                methods=['GET'])
    def get_partner_repositories(self, partner_id):
        partner_env = request.env['res.partner'].sudo()
        repository_env = request.env['project.git.repository'].sudo()
        commit_env = request.env['project.git.commit'].sudo()

        partner = partner_env.browse(partner_id)
        if not partner.exists():
            return request.make_response(
                json.dumps({'error': 'Partner not found'}),
                headers={'Content-Type': 'application/json'}
            )

        repositories = repository_env.search([('partner_id', '=', partner_id)])
        repos_data = []

        for repo in repositories:
            commits = commit_env.search(
                [('repository_id', '=', repo.id)], limit=10, order='create_date desc')
            commits_data = [{
                'date': commit.create_date.strftime('%d-%m-%Y'),
                'message': commit.message,
                'url': commit.url
            } for commit in commits]

            repos_data.append({
                'repository_name': repo.name,
                'repository_largest_contributor': repo.largest_contributor.name,
                'commits': commits_data
            })

        response_data = {
            'partner': {
                'id': partner.id,
                'name': partner.name,
                'email': partner.email
            },
            'repositories': repos_data
        }

        return request.make_response(
            json.dumps(response_data),
            headers={'Content-Type': 'application/json'}
        )
