from odoo import models, fields, api

class TiendaPublisher(models.Model):
    _name = 'tienda.publisher'
    _description = 'Publishers de videojuegos'

    _order = 'id, nombre'
    _rec_name = 'nombre'
    id = fields.Integer("Id")
    nombre = fields.Char("Nombre")
    pais = fields.Char("País")

    _sql_constraints = [
        ('id_uniq', 'UNIQUE (id)', 'El número de id debe ser único.')
    ]

