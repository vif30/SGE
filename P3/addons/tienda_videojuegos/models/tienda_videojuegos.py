from odoo import models, fields, api

class TiendaVideojuegos(models.Model):
    _name = 'tienda.videojuegos'
    _description = 'Videojuegos de la tienda'

    _order = 'fecha_publicacion desc, titulo'
    _rec_name = 'titulo'
    titulo = fields.Char("Título")
    genero = fields.Char("Género")
    fecha_publicacion = fields.Date('Fecha publicación')
    publisher = fields.Many2one('tienda.publisher', string="Publisher")
    precio = fields.Float('Precio')
    precioIVA = fields.Float('Precio con IVA')

    @api.onchange('precio')
    def _suma_iva(self):
        for record in self:
            record.precioIVA = (record.precio * 21)/100 + record.precio

