from app import crear_app, db

app = crear_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear tablas en la base de datos
    app.run(debug=True)
