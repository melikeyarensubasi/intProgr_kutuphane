# 📚 Kütüphane Yönetim Sistemi

Bu proje, bir kütüphane içerisindeki kitapların, kullanıcıların ve ödünç alma işlemlerinin yönetimini kolaylaştırmak amacıyla geliştirilmiş modern bir **Flask Web Uygulamasıdır**. Uygulama Render.com üzerinden kolayca dağıtılabilir yapıdadır.

## 🚀 Özellikler

- 📘 Kitapları kapak fotoğraflarıyla birlikte listeleme
- 🔎 Kitap arama ve filtreleme (isim/kategori)
- ➕ Yeni kitap ekleme ve düzenleme (sadece admin)
- 👤 Kullanıcı kayıt ve takibi
- 📅 Kitap ödünç alma ve geri getirme takibi
- ⚠️ Süresi dolan kitaplara uyarı sistemi
- 📊 İstatistik paneli (günlük tüketim, haftalık dolum, azalan stoklar)
- 🎨 Açık/Karanlık tema desteği
- 🔐 Sadece admin girişi destekler
- 🛠️ Admin panelinden sistem ayarları (ceza gün/süre oranı vs.)

## 🛠️ Kurulum (Yerel)

### Gereksinimler

- Python 3.8+
- pip

### Adımlar

```bash

 eğer lochalden çalıştırıyorsanız
   
git clone https://github.com/kullanici_adi/kutuphane_yonetim_sistemi.git

cd kutuphane_yonetim_sistemi

pip install -r requirements.txt
python app.py


Uygulama `http://127.0.0.1:5000` adresinde çalışacaktır.

```





## 📁 Proje Yapısı

```
kutuphane_yonetim_sistemi/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── utils.py
│   └── static/...
├── templates/
├── app.py         <-- Render uyumlu giriş noktası
├── requirements.txt
├── config.py
└── README.md
```


## 👨‍💻 Geliştirici

- Ad: melike yaren 
- github repo linki :
- Render Yayın Adresi: [https://kutuphane-xyz.onrender.com](#)