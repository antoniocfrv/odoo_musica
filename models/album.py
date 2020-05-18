# -*- coding: utf-8 -*-

from odoo import models, fields, api

class album(models.Model):
    _name = "odoo_musica.album" # IMPORTANTE é o nome que vai ter a táboa
    _description = "Albumes"
    _sql_constraints = [('nome unico', 'unique(name)', 'O Nome do Album. Non se pode repetir')]

    name = fields.Char(required=True, size=30,string="Álbum")  # IMPORTANTE o campo ten que chamarse name para visualizalo
    cancion_ids = fields.Many2many("odoo_musica.cancion", string="Cancións do Álbum",
                                   relation="odoo_musica_album_cancion", column1="album", column2="cancion",
                                   ondelete="set null")
    interprete_ids = fields.Many2many("odoo_musica.interprete", string="Intérpretes do Álbum",
                                 relation="odoo_musica_album_interprete", column1="album", column2="interprete",
                                 ondelete="cascade", compute="_determina_interpretes", store=True)

    def _actualiza_interpretes_do_album(self,album_a_revisar):
        lista = []
        for unha_cancion in album_a_revisar.cancion_ids:
            id_da_cancion = unha_cancion[0].id
            obxeto_cancion = self.env['odoo_musica.cancion'].search([('id', '=', id_da_cancion)])
            lista.append(obxeto_cancion.interprete_id.id)  # Obtemos o id do intérprete e engadimolo na lista
        album_a_revisar.update({'interprete_ids': [(6, 0, tuple(lista))]})  # Actualizamos os novos intérpretes

    @api.depends('cancion_ids')
    def _determina_interpretes(self):
        # for rexistro in self:
        #     rexistro._actualiza_interpretes_do_album(rexistro)
        self._actualiza_interpretes_do_album(self) # se non queremos que funcione para todos os rexistros de album

    def _recalcula_interpretes_se_cambiou_o_interprete_da_cancion(self,cancion_cambiada):
        for rexistro_album in self:
            if cancion_cambiada in rexistro_album.cancion_ids:
                rexistro_album._actualiza_interpretes_do_album(rexistro_album)
