# -*- coding: utf-8 -*-

from odoo import models, fields, api

class album(models.Model):
    _name = "odoo_musica.album" # IMPORTANTE é o nome que vai ter a táboa
    _description = "Albumes"
    _sql_constraints = [('nome_unico', 'unique(name)', 'O Nome do Album. Non se pode repetir')]

    name = fields.Char(required=True, size=30,string="Álbum")  # IMPORTANTE o campo ten que chamarse name para visualizalo
    cancion_ids = fields.Many2many("odoo_musica.cancion", string="Cancións do Álbum",
                                   relation="odoo_musica_album_cancion", column1="album", column2="cancion")
    interprete_ids = fields.Many2many("odoo_musica.interprete", string="Intérpretes do Álbum",
                                 relation="odoo_musica_album_interprete", column1="album", column2="interprete",ondelete="cascade",
                                 compute="_determina_interpretes", store=False)


    @api.depends('cancion_ids')
    def _determina_interpretes(self):
        for rexistro in self:
            lista = []
            for unha_cancion in rexistro.cancion_ids:
                id_da_cancion = unha_cancion[0].id
                obxeto_cancion = self.env['odoo_musica.cancion'].search([('id', '=', id_da_cancion)])
                if obxeto_cancion.interprete_id.id:
                    lista.append(obxeto_cancion.interprete_id.id)  # Obtemos o id do intérprete e engadimolo na lista
            rexistro.update({'interprete_ids': [(6, 0, tuple(lista))]})  # Actualizamos os novos intérpretes
