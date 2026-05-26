from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.productos.models import Producto

bp_productos = Blueprint('bp_productos', __name__)

@bp_productos.route('/')
def index():
    productos = Producto.query.all()
    return render_template('productos/index.html', productos=productos)

@bp_productos.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        precio = request.form.get('precio')
        stock = request.form.get('stock')
        
        nuevo_producto = Producto(nombre=nombre, precio=precio, stock=stock)
        db.session.add(nuevo_producto)
        db.session.commit()
        return redirect(url_for('bp_productos.index'))
        
    return render_template('productos/crear.html')

@bp_productos.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    producto = Producto.query.get_or_404(id)
    
    if request.method == 'POST':
        producto.nombre = request.form.get('nombre')
        producto.precio = request.form.get('precio')
        producto.stock = request.form.get('stock')
        
        db.session.commit()
        return redirect(url_for('bp_productos.index'))
        
    return render_template('productos/editar.html', producto=producto)

@bp_productos.route('/eliminar/<int:id>')
def eliminar(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('bp_productos.index'))