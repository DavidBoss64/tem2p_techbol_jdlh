from flask import Blueprint

bp_pedidos = Blueprint('bp_pedidos', __name__)

@bp_pedidos.route('/')
def index():
    return "<h1>Módulo de Pedidos</h1><p>En construcción...</p>"