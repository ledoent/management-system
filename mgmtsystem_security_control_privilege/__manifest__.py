# Copyright 2026 Ledoweb
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "ISMS Security Controls - Privilege Mapping (POC)",
    "summary": "Map ISO 27001 controls to the Odoo privileges implementing them",
    "version": "19.0.1.0.0",
    "development_status": "Alpha",
    "category": "Management System",
    "author": "Ledoweb, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/management-system",
    "license": "AGPL-3",
    "maintainers": ["dnplkndll"],
    "depends": [
        "mgmtsystem_security_event",
    ],
    "data": [
        "views/mgmtsystem_security_control_views.xml",
    ],
    "demo": [
        "demo/iso27001_controls.xml",
    ],
    "installable": True,
}
