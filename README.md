
# Abdullah Yavuz - Görüntü İşleme Vize Projesi

Bu proje, MediaPipe kullanarak gerçek zamanlı el takibi ile bir "çöp toplama" oyunu sunar. Kamera ile el hareketleriniz algılanır ve ekran üzerindeki nesnelere temas ederek puan toplarsınız.

## Gereksinimler

Bu proje Python 3 ile çalışır. Gerekli kütüphaneler şunlardır:

- OpenCV
- MediaPipe

Kurulum için aşağıdaki komutları çalıştırabilirsiniz:

```bash
pip install opencv-python mediapipe
```

## Projeyi Çalıştırmak

1. Bilgisayarınızda bir webcam bulunmalı.
2. `Abdullah_Yavuz_goruntuisleme_vize.py` dosyasını çalıştırın:

```bash
python Abdullah_Yavuz_goruntuisleme_vize.py
```

3. Oyun başladığında elinizi kameraya gösterin ve sarı nesneye işaret parmağınızla dokunmaya çalışın.
4. Her başarılı dokunuşta puanınız artacaktır.
5. Oyunu durdurmak için `q` tuşuna basabilirsiniz.

## Oyun Mekanikleri

- Sarı daire: Toplanması gereken "çöp".
- Mavi metin: Mevcut skorunuz.
- Elinizin işaret parmağıyla çöp nesnesine dokunarak puan kazanırsınız.

## Notlar

- El tespiti MediaPipe ile sağlanmaktadır. Işık koşulları ve kamera kalitesi performansı etkileyebilir.
