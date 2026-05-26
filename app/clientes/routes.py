from flask import Blueprint

bp_clientes = Blueprint('bp_clientes', __name__)
@bp_clientes.route('/')
def index():
    return "<h1>Módulo de Clientes</h1><p>En construcción...</p>"