from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from veritabani import get_db
import bcrypt
import os
from werkzeug.utils import secure_filename
from datetime import datetime

main = Blueprint("main", __name__)
UPLOAD_FOLDER = "app/static/img/kitap_kapaklari"

# Giriş Sayfası
@main.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        kullanici_adi = request.form["kullanici_adi"]
        sifre = request.form["sifre"]
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM admin WHERE kullanici_adi = ?", (kullanici_adi,))
        admin = cur.fetchone()
        if admin and bcrypt.checkpw(sifre.encode("utf-8"), admin["sifre_hash"]):
            session["admin_giris"] = True
            return redirect("/admin")
        flash("Hatalı giriş", "danger")
    return render_template("login.html")

# Admin Paneli
@main.route("/admin")
def admin_dashboard():
    if not session.get("admin_giris"):
        return redirect("/")
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM kitap")
    kitaplar = cur.fetchall()
    cur.execute("SELECT * FROM kullanici")
    kullanicilar = cur.fetchall()
    cur.execute("""
        SELECT o.*, k.baslik, k.kapak_yolu, ku.ad || ' ' || ku.soyad AS kullanici_ad
        FROM odunc o
        JOIN kitap k ON o.kitap_id = k.id
        JOIN kullanici ku ON o.kullanici_id = ku.id
    """)
    oduncler = cur.fetchall()
    return render_template("admin_dashboard.html", kitaplar=kitaplar, kullanicilar=kullanicilar, oduncler=oduncler)

# Ana Sayfa (Kitap Galerisi)
@main.route("/index")
def index():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM kitap")
    kitaplar = cur.fetchall()
    return render_template("index.html", kitaplar=kitaplar)

# Çıkış
@main.route("/logout")
def logout():
    session.pop("admin_giris", None)
    flash("Çıkış yapıldı.", "info")
    return redirect("/")


@main.route("/kitap_ekle", methods=["POST"])
def kitap_ekle():
    if not session.get("admin_giris"):
        return redirect("/")

    baslik = request.form["baslik"]
    yazar = request.form["yazar"]
    yayin_tarihi = request.form["yayin_tarihi"]
    kategori = request.form["kategori"]
    stok = int(request.form["stok"])
    sayfa_sayisi = int(request.form["sayfa_sayisi"])
    
    dosya = request.files.get("kapak_dosyasi")
    kapak_yolu = "varsayilan.jpg"
    if dosya and dosya.filename != "":
        dosya_ad = secure_filename(dosya.filename)
        dosya_yolu = os.path.join(UPLOAD_FOLDER, dosya_ad)
        dosya.save(dosya_yolu)
        kapak_yolu = dosya_ad

    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO kitap (baslik, yazar, yayin_tarihi, kategori, stok, sayfa_sayisi, kapak_yolu)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (baslik, yazar, yayin_tarihi, kategori, stok, sayfa_sayisi, kapak_yolu))
    conn.commit()
    flash("📘 Kitap başarıyla eklendi!", "success")
    return redirect("/admin")

@main.route("/kitap_sil/<int:kitap_id>", methods=["POST"])
def kitap_sil(kitap_id):
    if not session.get("admin_giris"):
        return redirect("/")
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM kitap WHERE id = ?", (kitap_id,))
    conn.commit()
    flash("🗑️ Kitap silindi.", "warning")
    return redirect("/admin")

@main.route("/kullanici_ekle", methods=["GET", "POST"])
def kullanici_ekle():
    if request.method == "POST":
        ad = request.form["ad"]
        soyad = request.form["soyad"]
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO kullanici (ad, soyad) VALUES (?, ?)", (ad, soyad))
        conn.commit()
        flash("👤 Yeni kullanıcı eklendi.", "success")
        return redirect("/admin")

    return render_template("kullanici_ekle.html")  # GET için form göster



@main.route("/kitap_odunc_al/<int:kitap_id>", methods=["POST"])
def kitap_odunc_al(kitap_id):
    ad_soyad = request.form["ad_soyad"]
    ad, soyad = ad_soyad.strip().split(" ", 1) if " " in ad_soyad else (ad_soyad, "")
    
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id FROM kullanici WHERE ad = ? AND soyad = ?", (ad, soyad))
    kullanici = cur.fetchone()

    if not kullanici:
        flash("⚠️ Kullanıcı bulunamadı, lütfen önce kayıt edin.", "danger")
        return redirect("/admin")

    cur.execute("SELECT stok FROM kitap WHERE id = ?", (kitap_id,))
    kitap = cur.fetchone()
    if kitap["stok"] <= 0:
        flash("❌ Bu kitap stokta yok!", "danger")
        return redirect("/admin")

    cur.execute("INSERT INTO odunc (kitap_id, kullanici_id, odunc_tarihi) VALUES (?, ?, ?)",
                (kitap_id, kullanici["id"], datetime.now().date()))
    cur.execute("UPDATE kitap SET stok = stok - 1 WHERE id = ?", (kitap_id,))
    conn.commit()
    flash("✅ Kitap ödünç verildi.", "success")
    return redirect("/admin")

@main.route("/ayar", methods=["GET", "POST"])
def ayar():
    if not session.get("admin_giris"):
        return redirect("/")

    conn = get_db()
    cur = conn.cursor()

    if request.method == "POST":
        gunluk_ceza = float(request.form["gunluk_ceza"])
        sayfa_basina_gun = int(request.form["sayfa_basina_gun"])
        cur.execute("UPDATE ayar SET gunluk_ceza = ?, sayfa_basina_gun = ? WHERE id = 1", (gunluk_ceza, sayfa_basina_gun))
        conn.commit()
        flash("✅ Ayarlar güncellendi.", "success")
        return redirect("/ayar")

    cur.execute("SELECT * FROM ayar WHERE id = 1")
    ayar = cur.fetchone()
    return render_template("ayar.html", ayar=ayar)

@main.route('/odunc_ver', methods=['GET', 'POST'])
def odunc_ver():
    conn = get_db()
    cur = conn.cursor()

    if request.method == 'POST':
        kitap_id = request.form['kitap_id']
        kullanici_id = request.form['kullanici_id']
        odunc_tarihi = request.form['odunc_tarihi']

        # Ödünç verme işlemi
        cur.execute("""
            INSERT INTO odunc (kitap_id, kullanici_id, odunc_tarihi)
            VALUES (?, ?, ?)
        """, (kitap_id, kullanici_id, odunc_tarihi))
        conn.commit()
        flash("📚 Kitap başarıyla ödünç verildi.", "success")
        return redirect(url_for('main.index'))

    # Kitapları ve kullanıcıları al
    cur.execute("SELECT * FROM kitap")
    kitaplar = cur.fetchall()

    cur.execute("SELECT * FROM kullanici")
    kullanicilar = cur.fetchall()

    return render_template("odunc_ver.html", kitaplar=kitaplar, kullanicilar=kullanicilar)



@main.route('/raporlar')
def raporlar():
    conn = get_db()
    cur = conn.cursor()

    # Örnek raporlar (Kütüphane raporu, ödünç verilen kitaplar vs.)
    cur.execute("SELECT kitap_id, COUNT(*) FROM odunc GROUP BY kitap_id ORDER BY COUNT(*) DESC LIMIT 5")
    en_cok_odunc_verilenler = cur.fetchall()

    # Raporlar verilerini kullanarak raporu görüntüleyin
    return render_template('raporlar.html', en_cok_odunc_verilenler=en_cok_odunc_verilenler)



@main.route("/kullanicilar")
def kullanici_listesi():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM kullanici")
    kullanicilar = cur.fetchall()
    return render_template("kullanici_listesi.html", kullanicilar=kullanicilar)

@main.route('/kullanici_sil/<int:id>', methods=['POST'])
def kullanici_sil(id):
    try:
        conn = get_db()  # Veritabanı bağlantısı get_db() ile yapılıyor
        cur = conn.cursor()
        
        # Kullanıcıyı silme işlemi
        cur.execute("DELETE FROM kullanici WHERE id = ?", (id,))
        conn.commit()
        
        cur.close()
        flash("Kullanıcı başarıyla silindi.", "success")
        return redirect(url_for('main.kullanici_listesi'))

    except Exception as e:
        flash(f"Bir hata oluştu: {e}", "danger")
        return redirect(url_for('main.kullanici_listesi'))


@main.route('/kullanici_duzenle/<int:id>', methods=['GET', 'POST'])
def kullanici_duzenle(id):
    conn = get_db()  # <-- Burayı değiştirdik
    cur = conn.cursor()

    if request.method == 'POST':
        yeni_ad = request.form['ad']
        yeni_soyad = request.form['soyad']
        cur.execute("UPDATE kullanici SET ad = ?, soyad = ? WHERE id = ?", (yeni_ad, yeni_soyad, id))
        conn.commit()
        cur.close()
        flash("👤 Kullanıcı bilgileri güncellendi.", "success")
        return redirect(url_for('main.kullanici_listesi'))

    cur.execute("SELECT * FROM kullanici WHERE id = ?", (id,))
    kullanici = cur.fetchone()
    cur.close()
    return render_template("kullanici_duzenle.html", kullanici=kullanici)


