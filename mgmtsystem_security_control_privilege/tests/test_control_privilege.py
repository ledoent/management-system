# Copyright 2026 Ledoweb
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.addons.base.tests.common import BaseCommon


class TestControlPrivilege(BaseCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.privilege = cls.env["res.groups.privilege"].create({"name": "ISMS Test"})
        cls.group = cls.env["res.groups"].create(
            {"name": "ISMS Control Group", "privilege_id": cls.privilege.id}
        )
        cls.system = cls.env["mgmtsystem.system"].create({"name": "Test ISMS"})
        cls.control = cls.env["mgmtsystem.security.control"].create(
            {
                "name": "Access control",
                "iso27001_ref": "A.5.15",
                "system_id": cls.system.id,
            }
        )

    def test_no_groups_without_privilege(self):
        self.assertFalse(self.control.privilege_ids)
        self.assertFalse(self.control.group_ids)

    def test_groups_resolved_from_privileges(self):
        self.control.privilege_ids = self.privilege
        # group_ids is the audit traceability surface: every group under the
        # mapped privilege(s).
        self.assertIn(self.group, self.control.group_ids)
