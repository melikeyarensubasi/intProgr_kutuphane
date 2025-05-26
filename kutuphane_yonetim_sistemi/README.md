
# Kütüphane Yönetim Sistemi

## Proje Tanımı

Bu proje, kullanıcıların kitap ödünç alıp verebildiği, kitap ekleyip silebildiği, kullanıcılar hakkında bilgiler tutan bir kütüphane yönetim sistemini içerir. Sistem, admin paneli üzerinden kitap ve kullanıcı işlemleri yapılabilmesini sağlar. Ayrıca, kullanıcıların kitap ödünç alma geçmişi ve mevcut ödünç alım durumları da takip edilir.

## Kullanılan Teknolojiler

- **Python**: Flask framework
- **Veritabanı**: SQLite
- **HTML/CSS**: Temel web tasarımı için
- **Jinja2**: Dinamik içerik rendering
- **Flask**: Python web framework
- **Bootstrap**: Arayüz tasarımı

## Kurulum Adımları

1. **Proje Dosyalarını İndirme**
   ```bash
   git clone <repo_link>ile indirebilirsiniz
   
   cd kutuphane_yonetim_sistemi
   ```

2. **Sanal Ortam Kurulumu**
   Python ve pip kuruluysa:
   ```bash
   python -m venv venv
   venv\Scriptsctivate  # Windows
   source venv/bin/activate  # Linux / Mac
   ```

3. **Gerekli Kütüphanelerin Yüklenmesi**
   `requirements.txt` dosyasını kullanarak gerekli kütüphaneleri yükleyin.
   ```bash
   pip install -r requirements.txt
   ```

4. **Veritabanının Yapılandırılması**
   Proje ilk kez çalıştırıldığında otomatik olarak veritabanı oluşturulacaktır. Eğer veritabanı oluşturulmadıysa `init_db()` fonksiyonunu çalıştırarak veritabanını başlatabilirsiniz.

5. **Uygulamayı Başlatma**
   Flask uygulamasını başlatmak için:
   ```bash
   python app.py
   ```

6. **Tarayıcıda Uygulama Erişimi**
   Uygulama, `http://127.0.0.1:5000` adresinde çalışacaktır.

## Ana Özellikler

- **Admin Paneli**: Adminler kitap ekleyebilir, silebilir ve kullanıcıları yönetebilir.
- **Kitaplar**: Kullanıcılar, mevcut kitapları görüntüleyebilir, ödünç alabilir.
- **Kullanıcı Yönetimi**: Admin kullanıcıları düzenleyebilir ve silebilir.
- **Ödünç Sistemi**: Kullanıcılar kitapları ödünç alabilir ve geri verebilir.
- **Raporlar**: Admin, ödünç verilen kitapları ve durumları izleyebilir.

## Uygulama Arayüzü

1. **Ana Sayfa**: Kullanıcılar mevcut kitapları görebilir, ödünç alabilir.
2. **Admin Paneli**: Admin kullanıcıları ve kitapları yönetebilir.
3. **Kullanıcı Düzenle**: Admin kullanıcı bilgilerini düzenleyebilir.
4. **Raporlar**: Admin, ödünç kitaplarla ilgili raporları görüntüleyebilir.


