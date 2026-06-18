# Copyright 2019 Marcelo Frare (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# Copyright 2019 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.exceptions import ValidationError
from odoo.tests import common


class TestActionEfficacy(common.TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        cls.action = cls.env["mgmtsystem.action"].create(
            {"name": "Test Action", "type_action": "immediate"}
        )

    def test_change_efficacy(self):
        record = self.action

        record.efficacy_value = 50
        record._onchange_efficacy_value()
        self.assertEqual(50, record.efficacy_value)

        with self.assertRaises(ValidationError) as e:
            record.efficacy_value = 200
            record._onchange_efficacy_value()

        self.assertIn(self.env._("Rating must be between 0 and 100"), str(e.exception))
