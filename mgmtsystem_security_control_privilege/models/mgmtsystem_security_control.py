# Copyright 2026 Ledoweb
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models

# ISO/IEC 27001:2022 Annex A themes (the 2022 revision collapsed the 14 clauses
# into 4 themes).
ISO27001_THEMES = [
    ("organizational", "A.5 Organizational"),
    ("people", "A.6 People"),
    ("physical", "A.7 Physical"),
    ("technological", "A.8 Technological"),
]


class SecurityControl(models.Model):
    """Trace an ISMS security control to the Odoo access that implements it.

    Shape study, not a merge candidate. max3903's
    ``mgmtsystem.security.control`` (OCA#804) is a risk-governance record. This
    adds an *audit traceability* link to 19.0's ``res.groups.privilege``: for an
    access-control-family control (ISO 27001 A.5.15/A.5.18/A.8.2/A.8.3) it
    records *which Odoo privileges operationally realise it*, so an auditor can
    walk control → privileges → groups → users.

    Deliberately framed as a link, not enforcement: it documents the access
    that implements the control, it does not itself constrain anything. A real
    access control spans several privileges across apps, hence Many2many.
    """

    _inherit = "mgmtsystem.security.control"

    iso27001_ref = fields.Char(
        string="ISO 27001:2022 Ref",
        help="Annex A control identifier, e.g. A.5.15 (Access control).",
        index=True,
    )
    iso27001_theme = fields.Selection(
        selection=ISO27001_THEMES,
        string="ISO 27001 Theme",
    )
    privilege_ids = fields.Many2many(
        comodel_name="res.groups.privilege",
        string="Implementing Privileges",
        help="The 19.0 access privileges that operationally realise this "
        "control. A control usually maps to several privileges across apps. "
        "This is an audit traceability link — it records which access "
        "implements the control; it does not itself enforce anything.",
    )
    group_ids = fields.Many2many(
        comodel_name="res.groups",
        string="Resulting Groups",
        compute="_compute_group_ids",
        help="All security groups under the mapped privileges — the concrete "
        "access surface this control is traced to.",
    )

    @api.depends("privilege_ids")
    def _compute_group_ids(self):
        groups = self.env["res.groups"]
        for control in self:
            control.group_ids = (
                groups.search([("privilege_id", "in", control.privilege_ids.ids)])
                if control.privilege_ids
                else groups
            )
