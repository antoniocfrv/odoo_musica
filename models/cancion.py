# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cancion(models.Model):
    _name = "odoo_musica.cancion" # IMPORTANTE é o nome que vai ter a táboa
    _description = "Cancións"

    name = fields.Char(required=True, size=30, string="Cancións") #IMPORTANTE o campo ten que chamarse name para visualizalo
    interprete_id = fields.Many2one("odoo_musica.interprete",string="Intérprete", ondelete='cascade')


