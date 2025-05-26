# Flask uygulaması başlangıç noktası - app.py
import os
from flask import Flask
from app.routes import main
from veritabani import init_db

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.secret_key = "guvenli_anahtar"
app.template_folder = os.path.join(BASE_DIR, 'app', 'templates')
app.static_folder = os.path.join(BASE_DIR, 'app', 'static')

app.register_blueprint(main)

init_db()

#if __name__ == "__main__":
 #   print("🚀 Kütüphane sistemi başlatılıyor...")
  #  app.run(debug=False)

import os
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
