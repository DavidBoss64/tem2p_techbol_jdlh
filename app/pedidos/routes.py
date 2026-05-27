from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.pedidos.models import Pedido
from app.clientes.models import Cliente
from app.productos.models import Producto


bp_pedidos = Blueprint('bp_pedidos', __name__)

@bp_pedidos.route('/')
def index():
    pedidos = Pedido.query.order_by(Pedido.fecha.desc()).all()
    return render_template('pedidos/index.html',pedidos=pedidos)

@bp_pedidos.route('/crear',methods=['GET','POST'])
def crear():
    
    if request.method == 'POST':
        cliente_id = request.form.get('cliente_id')
        producto_id = request.form.get('producto_id')
        monto =request.form.get('monto')
        cantidad = request.form.get('cantidad')


        producto = Producto.query.get_or_404(producto_id)
        print("CANTIDAD: ",cantidad)
        producto.stock -=int(cantidad); 
        
        nuevo_pedido = Pedido(cliente_id=cliente_id,producto_id=producto_id,monto=monto)
        db.session.add(nuevo_pedido)
        db.session.commit()
        return redirect(url_for('bp_pedidos.index'))
    
    clientes = Cliente.query.all()
    productos = Producto.query.all()
    return render_template('pedidos/crear.html',clientes=clientes, productos=productos)

@bp_pedidos.route('/editar/<int:id>', methods = ['GET','POST'])
def editar(id):
    pedido = Pedido.query.get_or_404(id)

    if request.method == "POST":
        pedido.cliente_id = request.form.get('cliente_id')
        pedido.producto_id = request.form.get('producto_id')
        pedido.monto = request.form.get('monto')

        db.session.commit()

        return redirect(url_for('bp_pedidos.index'))
    
    clientes = Cliente.query.all()
    productos = Producto.query.all()

    return render_template('pedidos/editar.html',pedido=pedido,clientes=clientes,productos=productos)

@bp_pedidos.route('/eliminar/<int:id>')
def eliminar(id):
    pedido = Pedido.query.get_or_404(id)
    db.session.delete(pedido)
    db.session.commit()
    return redirect(url_for('bp_pedidos.index'))
