# -*- coding: utf-8 -*-
import calendar
from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta
from datetime import date, timedelta
from odoo.tools import float_compare, float_is_zero, float_round
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
from datetime import datetime
from math import copysign

from odoo.tools.populate import compute

class accountAsset(models.Model):
    _inherit = 'account.asset'
