-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 25 May 2025, 23:01:50
-- Sunucu sürümü: 10.4.32-MariaDB
-- PHP Sürümü: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `kutuphane_db`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `kullanici_adi` varchar(100) NOT NULL,
  `sifre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `ayar`
--

CREATE TABLE `ayar` (
  `id` int(11) NOT NULL,
  `gunluk_ceza` float NOT NULL DEFAULT 2
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Tablo döküm verisi `ayar`
--

INSERT INTO `ayar` (`id`, `gunluk_ceza`) VALUES
(1, 2);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kitap`
--

CREATE TABLE `kitap` (
  `id` int(11) NOT NULL,
  `baslik` varchar(255) NOT NULL,
  `yazar` varchar(255) NOT NULL,
  `yayin_yili` date NOT NULL,
  `kategori` varchar(100) NOT NULL,
  `stok` int(11) NOT NULL DEFAULT 0,
  `kapak_yolu` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Tablo döküm verisi `kitap`
--

INSERT INTO `kitap` (`id`, `baslik`, `yazar`, `yayin_yili`, `kategori`, `stok`, `kapak_yolu`) VALUES
(3, 'Sinekli Bakkal', 'Halide Edib Adıvar', '2011-06-25', 'Roman', 1, 'wi_800.jpeg'),
(4, 'Ateşten Gömlek', 'Halide Edib Adıvar', '2013-06-25', 'Kurgu', 2, 'wi_800_1.jpeg'),
(5, 'Suç ve Ceza', 'Fyodor Dostoyevski', '2020-06-25', 'Roman, Polisiye, Psikolojik Kurgu, Felsefi Kurgu', 3, '61Ez0InFj-L._AC_UF10001000_QL80__1.jpg'),
(6, 'Harry Potter ve Felsefe Taşı', 'Chris Columbus', '2000-06-25', 'Çocuk, Aksiyon, Komedi, Fantastik Film, Macera, Bilim Kurgu, Aile filmi, Dram, Gizem, Kurgusal, Doğa', 0, 'wi_800_2.jpeg'),
(7, 'Tutunamayanlar', 'Oğuz Atay', '1997-08-25', 'Kurgu, Bilinç Akışı', 4, 'tutunamaynlar-ekitap.jpg'),
(8, 'Elflerin Kanı', 'Andrzej Sapkowski', '2025-04-30', 'Fantezi, Roman, Fantastik Kurgu, Epik Fantezi', 5, 'indir_1.jpeg'),
(9, 'Saatleri Ayarlama Enstitüsü', 'Ahmet Hamdi Tanpınar', '2005-06-25', 'Hiciv, Edebi Kurgu', 0, '0000000027135-1.jpg'),
(10, 'Aşk-ı Memnu', 'Halit Ziya Uşaklıgil', '2025-05-01', 'Kurgu', 1, '71EHvmRnycL._AC_UF10001000_QL80_.jpg');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kullanici`
--

CREATE TABLE `kullanici` (
  `id` int(11) NOT NULL,
  `ad_soyad` varchar(255) NOT NULL,
  `kayit_tarihi` date NOT NULL DEFAULT curdate()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Tablo döküm verisi `kullanici`
--

INSERT INTO `kullanici` (`id`, `ad_soyad`, `kayit_tarihi`) VALUES
(4, 'melike', '2025-05-26'),
(5, 'sıla', '2025-05-26'),
(6, 'damla', '2025-05-26'),
(7, 'özlem', '2025-05-26'),
(8, 'sude', '2025-05-26'),
(9, 'ahmet', '2025-05-26');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `odunc`
--

CREATE TABLE `odunc` (
  `id` int(11) NOT NULL,
  `kitap_id` int(11) NOT NULL,
  `kullanici_id` int(11) NOT NULL,
  `odunc_tarihi` date NOT NULL DEFAULT curdate(),
  `teslim_edildi` tinyint(1) NOT NULL DEFAULT 0,
  `iade_tarihi` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Tablo döküm verisi `odunc`
--

INSERT INTO `odunc` (`id`, `kitap_id`, `kullanici_id`, `odunc_tarihi`, `teslim_edildi`, `iade_tarihi`) VALUES
(4, 4, 9, '2025-05-26', 0, NULL),
(5, 6, 6, '2025-05-26', 0, NULL),
(6, 9, 5, '2025-05-26', 0, NULL),
(7, 3, 7, '2025-05-26', 0, NULL),
(8, 9, 4, '2025-05-26', 0, NULL);

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kullanici_adi` (`kullanici_adi`);

--
-- Tablo için indeksler `ayar`
--
ALTER TABLE `ayar`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `kitap`
--
ALTER TABLE `kitap`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `kullanici`
--
ALTER TABLE `kullanici`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `odunc`
--
ALTER TABLE `odunc`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kitap_id` (`kitap_id`),
  ADD KEY `kullanici_id` (`kullanici_id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `kitap`
--
ALTER TABLE `kitap`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Tablo için AUTO_INCREMENT değeri `kullanici`
--
ALTER TABLE `kullanici`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Tablo için AUTO_INCREMENT değeri `odunc`
--
ALTER TABLE `odunc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Dökümü yapılmış tablolar için kısıtlamalar
--

--
-- Tablo kısıtlamaları `odunc`
--
ALTER TABLE `odunc`
  ADD CONSTRAINT `odunc_ibfk_1` FOREIGN KEY (`kitap_id`) REFERENCES `kitap` (`id`),
  ADD CONSTRAINT `odunc_ibfk_2` FOREIGN KEY (`kullanici_id`) REFERENCES `kullanici` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
