# -*- coding: utf-8 -*- 
from odoo import models, fields 
class TodoTask(models.Model): 
    _name = 'todo.task' 
    _description = 'To-do Task'
    name = fields.Char('Description', required=False) 

    nombreSocio = fields.Char('Nombre Socio', required=True) 
    lugar = fields.Char('Lugar', required=True) 
    dia = fields.Char('Dia', required=True) 
    horaInicio = fields.Char('Hora inicio', required=True) 
    horaFin = fields.Char('Hora fin', required=True) 
    tipoPedido = fields.Char('Tipo de Pedido', required=True) 

    is_done = fields.Boolean('Done?') 
    active = fields.Boolean('Active?', default=True)
    def do_marcar(self):
        self.is_done = not self.is_done
        return True
    def do_limpiar(self):
        done_recs = self.search([('is_done', '=', True)])
        done_recs.write({'active': False})
        return True

 #Nombre_cliente 

# Lugar 

# Día 

# Hora Inicio 

# Hora Fin 

# Tipo de pedido 