# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.http import root
import time
import os
session_store = root.session_store
class IdleLlogout(models.TransientModel):
    _name = 'idle.logout'

    @api.model
    def check_session(self,minutes):
        print(33333333333333)
        dd = time.time() - minutes * 60
        for fname in os.listdir(session_store.path):
            path = os.path.join(session_store.path, fname)
            try:
                if os.path.getmtime(path) < dd:
                    os.unlink(path)
            except OSError:
                pass
        