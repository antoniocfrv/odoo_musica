# -*- coding: utf-8 -*-

from odoo import models, fields, api

class interprete(models.Model):
    _name = "odoo_musica.interprete" # IMPORTANTE é o nome que vai ter a táboa
    _description = "Interpretes"
    _sql_constraints = [('nome_unico', 'unique(name)', 'O Nome do Intérprete. Non se pode repetir')]

    name = fields.Char(required=True, size=30, string="Intérprete") #IMPORTANTE o campo ten que chamarse name para visualizalo
    cancion_ids = fields.One2many("odoo_musica.cancion", 'interprete_id',string="Cancións")
