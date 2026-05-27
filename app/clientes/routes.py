from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.clientes.models import Cliente

bp_clientes = Blueprint('bp_clientes', __name__)

@bp_clientes.route('/')
def index():
    clientes = Cliente.query.all()
    return render_template('clientes/index.html', clientes=clientes)

@bp_clientes.route('/crear',methods=['GET','POST'])
def crear():
    if request.method == "POST":
        nombre = request.form.get('nombre')
        telefono = request.form.get('telefono')

        nuevo_cliente = Cliente(nombre=nombre,telefono=telefono)

        db.session.add(nuevo_cliente)
        db.session.commit()
        return redirect(url_for('bp_clientes.index'))
    
    return render_template('clientes/crear.html')


@bp_clientes.route('/editar/<int:id>',methods=['GET','POST'])
def editar(id):
    cliente = Cliente.query.get_or_404(id)

    if request.method == 'POST':
        cliente.nombre = request.form.get('nombre')
        cliente.telefono = request.form.get('telefono')

        db.session.commit()
        return redirect(url_for('bp_clientes.index'))
    
    return render_template('clientes/editar.html')


@bp_clientes.route('/eliminar/<int:id>')
def eliminar(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()

    return redirect(url_for('bp_clientes.index'))