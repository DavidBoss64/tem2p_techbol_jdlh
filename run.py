from app import create_app, db

app = create_app()

# PARA CREAR LAS TABLAS AL MOMENTO DE DESPLEGAR EN RENDER
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)