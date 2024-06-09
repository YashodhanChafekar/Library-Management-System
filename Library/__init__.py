from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def library():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .books import books
    from .members import members

    app.register_blueprint(books, url_prefix='/')
    app.register_blueprint(members, url_prefix='/')

    from .models import Book,Member,Transaction,BookRecord

    with app.app_context():
        if path.exists('Library/' + DB_NAME):
            db.create_all()
            print('Created Database!')

    return app