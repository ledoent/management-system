Shape study (not a merge candidate). Adds an **audit traceability** link from
OCA's ISMS security controls (`mgmtsystem.security.control`, OCA#804) to Odoo
19.0's `res.groups.privilege`.

For an access-control-family ISO/IEC 27001:2022 control (A.5.15, A.5.18, A.8.2,
A.8.3), it records *which Odoo privileges operationally implement it* — so an
auditor can walk **control → privileges → groups → users**. A control usually
maps to several privileges across apps, hence Many2many.

It is deliberately a *link, not enforcement*: it documents the access that
realises a control, it does not constrain anything. Built to compare design
approaches on OCA/management-system#810 — see the PR description.
