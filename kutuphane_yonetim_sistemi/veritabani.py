# Veritabanı bağlantısı ve başlangıç işlemleri - veritabani.py
import sqlite3
import os
import bcrypt

DB_PATH = "kutuphane.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DB_PATH):
        conn = get_db()
        cur = conn.cursor()

        # Admin tablosu
        cur.execute("""
        CREATE TABLE IF NOT EXISTS admin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kullanici_adi TEXT NOT NULL,
            sifre_hash TEXT NOT NULL
        )
        """)

        # Kitap tablosu
        cur.execute("""
        CREATE TABLE IF NOT EXISTS kitap (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            baslik TEXT NOT NULL,
            yazar TEXT,
            yayin_tarihi TEXT,
            kategori TEXT,
            stok INTEGER,
            sayfa_sayisi INTEGER,
            kapak_yolu TEXT
        )
        """)

        # Kullanici tablosu
        cur.execute("""
        CREATE TABLE IF NOT EXISTS kullanici (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad TEXT NOT NULL,
            soyad TEXT NOT NULL,
            kayit_tarihi TEXT DEFAULT (DATE('now'))
        )
        """)

        # Odunc tablosu
        cur.execute("""
        CREATE TABLE IF NOT EXISTS odunc (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kitap_id INTEGER,
            kullanici_id INTEGER,
            odunc_tarihi TEXT DEFAULT (DATE('now')),
            iade_tarihi TEXT,
            teslim_edildi INTEGER DEFAULT 0,
            FOREIGN KEY(kitap_id) REFERENCES kitap(id),
            FOREIGN KEY(kullanici_id) REFERENCES kullanici(id)
        )
        """)
        

        # Ayar tablosu
        cur.execute("""
        CREATE TABLE IF NOT EXISTS ayar (
            id INTEGER PRIMARY KEY,
            sayfa_basina_gun INTEGER,
            gunluk_ceza REAL
        )
        """)
        cur.execute("INSERT INTO ayar (id, sayfa_basina_gun, gunluk_ceza) VALUES (1, 3, 1.5)")

        # Varsayılan admin
        sifre = "1234"
        sifre_hash = bcrypt.hashpw(sifre.encode('utf-8'), bcrypt.gensalt())
        cur.execute("INSERT INTO admin (kullanici_adi, sifre_hash) VALUES (?, ?)", ("admin", sifre_hash))

        conn.commit()
        conn.close()
        print("✅ Veritabanı oluşturuldu ve admin eklendi.")
    else:
        print("✅ Veritabanı zaten mevcut.")
