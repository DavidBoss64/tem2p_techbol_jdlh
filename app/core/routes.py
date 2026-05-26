from flask import Blueprint, render_template

bp_core = Blueprint('bp_core', __name__)

@bp_core.route('/')
def index():
    return render_template('index.html')