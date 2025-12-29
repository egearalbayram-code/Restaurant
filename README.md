Hızlı Kurulum:
python setup_data.py (Veri klasörünü ve başlangıç verilerini oluşturur).
python main.py (Sistemi başlatır).

Temel Özellikler:
Masa Yönetimi: Masaya müşteri atama, kapasite kontrolü ve durum takibi.
Sipariş Sistemi: Menü öğelerini siparişe ekleme ve mutfak fişi (ticket) oluşturma.
Fatura Hesaplama: Vergi ve bahşiş dahil otomatik hesaplama ve hesap bölme.
Raporlama: Günlük ciro, en çok satan ürünler ve performans analizi.


Teknik Yapı:
OOP: Masa ve Menü öğeleri sınıflar (class) ile temsil edilmiştir.
Veri Saklama: Tüm veriler data/ klasörü altında JSON formatında saklanır ve kalıcıdır.
Modülerlik: Proje PDF'te istenen 6 ayrı modüle (tables, menu, orders, storage, reports, main) bölünmüştür .