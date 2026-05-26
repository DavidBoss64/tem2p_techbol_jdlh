from flask import Blueprint

bp_core = Blueprint('bp_core', __name__)

@bp_core.route('/')
def index():
    return "<h1>Bienvenido a TechBol</h1>"