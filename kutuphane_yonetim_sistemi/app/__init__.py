from flask import Flask
import sqlite3
import os

def create_app():
    app = Flask(__name__,
                template_folder=os.path.join('app', 'templates'),
                static_folder=os.path.join('app', 'static'))

    app.secret_key = 'gizli-anahtar'

    # Veritabanı bağlantısı (SQLite)
    def get_db():
        db_path = os.path.join(os.path.dirname(__file__), '..', 'kutuphane.db')
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn

    app.db_connection = get_db()

    # Blueprint ekleme
    from app.routes import main
    app.register_blueprint(main)

    return app
