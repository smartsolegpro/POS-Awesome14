# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    import frappe
except ImportError:
    frappe = None

__version__ = "6.3.0"


def console(*data):
    if frappe and hasattr(frappe, "session") and hasattr(frappe.session, "user"):
        try:
            frappe.publish_realtime("toconsole", data, user=frappe.session.user)
        except Exception:
            pass
