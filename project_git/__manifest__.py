# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

{
    "name": "Project Git",
    "summary": "Integrates your projects with git based services",
    "category": "Project",
    "version": "17.0.1.0.0",
    "author": "Juan Camilo Sandoval Garcia",
    "website": "",
    "depends": [
        "base",
        "web",
        "contacts",
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",

        "report/ir_actions_report.xml",
        
        "views/git_repository_views.xml",
        "views/git_commit_views.xml",
        "views/res_partner_views.xml",
        "views/git_menus_views.xml",
    ],

    "demo": [],
    "application": True,
}
