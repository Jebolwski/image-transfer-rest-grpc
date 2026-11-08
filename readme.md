<p align="right">

[![Read in English](https://img.shields.io/badge/Read%20in-English-blue?style=for-the-badge)](readme.en.md)

</p>
# Mikroservis Mimarisinde Görüntü/Medya Aktarımı: REST (Base64) ve gRPC Karşılaştırması

**Ders:** Temel Ağ Protokolleri
**Ekip:**

- Sabir Süleymanlı (502531019)
- Mert Gökmen (502631009)

## Proje Özeti

Bu proje, büyük boyutlu görüntü dosyalarının (1MB, 5MB, 10MB kaplan görselleri) mikroservisler arasında aktarımında REST ve gRPC protokollerinin ağ performansı ve kaynak tüketimi açısından karşılaştırmayı amaçlamaktadır. REST mimarisinde görüntülerin Base64 formatına çevrilmesinin yarattığı boyut artışı ve ekstra işlemci/bellek yükü, gRPC'nin doğrudan ham bayt akışı (binary stream) yeteneğiyle kıyaslanacaktır.

## Kullanılan Teknolojiler

- **REST Servisi:** Python, FastAPI
- **gRPC Servisi:** Python, gRPC, Protocol Buffers
- **Altyapı:** Docker & Docker Compose
- **Yük Testi ve Analiz:** k6, Wireshark

## Planlanan Klasör Yapısı

- `rest-service/`: FastAPI kodları ve REST API Dockerfile'ı
- `grpc-service/`: gRPC kodları, Protobuf tanımları ve Dockerfile'ı
- `load-tests/`: k6 yük testi senaryoları
- `data/`: Testte kullanılacak 1MB, 5MB ve 10MB'lık görseller
- `scripts/`: Test verilerini milimetrik boyutlarda üreten Python scriptleri
- `docs/`: Wireshark .pcap kayıtları ve nihai raporlar

## İş-Zaman Planı

| Hafta | Faaliyet                                                                                             |
| :---- | :--------------------------------------------------------------------------------------------------- |
| 1     | Literatür taraması; gRPC ve Protocol Buffers öğrenimi; 1, 5 ve 10 MB test görsellerinin hazırlanması |
| 2     | Docker Compose iskeletinin kurulması; ölçüm protokolünün ve metriklerin kesinleştirilmesi            |
| 3-4   | REST (Base64) servisinin ve k6 senaryosunun geliştirilmesi; erken pilot Wireshark yakalaması         |
| 5-6   | gRPC servislerinin (unary ve streaming) geliştirilmesi; ileti boyutu limiti ve parça boyutu ayarları |
| 7-8   | Tam yük testlerinin uygulanması; pcap dosyalarının ve docker stats verilerinin toplanması            |
| 9     | Verilerin analizi, grafiklerin ve karşılaştırma tablolarının hazırlanması                            |
| 10    | Nihai raporun, sunumun ve GitHub reposunun tamamlanması                                              |
