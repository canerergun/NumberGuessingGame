# Random Sayı Tahmin Oyunu

Bu kod, bilgisayarın belirlediği rastgele bir sayıyı tahmin etmeye çalışan bir oyundur. Oyuncunun belirli bir sayıda tahmin hakkı vardır. Her tahminde, oyuncuya bilgisayarın tuttuğu sayının büyük mü, küçük mü olduğu bilgisi verilir. Oyuncu, belirlenen hakkınız içinde bilgisayarın tuttuğu sayıyı bulmaya çalışır.

## Gereksinimler

- Python 3.x
- `random` modülü


## Kod Açıklaması

Bu kod, Python dilinde yazılmıştır ve rastgele sayı üretmek için `random` modülünü kullanır. Oyuncuya, tahmin hakkı belirli bir sayıda (burada 5) verilir. Oyuncunun girdiği sayı, bilgisayarın belirlediği rastgele sayı ile karşılaştırılır. Her tahminde, oyuncuya bilgi verilir ve kalan hakkı gösterilir. Eğer oyuncu belirlenen hakkını kullanmadan doğru sayıyı bulursa, oyun sona erer.

```python
import random

tutulanSayi = random.randint(1, 10)
hak = 5

while hak > 0:
    sayı = input("Tahmin Ettiğiniz Sayıyı Giriniz: ")
    
    if sayı.isdigit():
        sayı = int(sayı)
        if sayı == tutulanSayi:
            print(f"Tebrikler Bildiniz! Bilgisayarın Tuttuğu Sayı: {tutulanSayi}")
            break
        elif sayı > tutulanSayi:
            print("Tuttuğum Sayı Daha Küçük")
        elif sayı < tutulanSayi:
            print("Tuttuğum Sayı Daha Büyük")
        hak -= 1
        print(f"Kalan Hakkınız: {hak}")
    else:
        print("Lütfen geçerli bir sayı giriniz!")

if hak == 0:
    print("Hakkınız Kalmadı Oyun Bitti")
```

## Örnek Kullanım

1. Oyuncu tarafından bir tahmin girilir.
2. Bilgisayar, tuttuğu sayı ile oyuncunun tahmin ettiği sayıyı karşılaştırır.
3. Doğru sayı bulunana kadar adımlar 1 ve 2 tekrarlanır.
4. Tahmin hakkı kalmadığında oyun sona erer.

## Notlar

- Oyuncunun tahmin hakkı belirli bir sayıda (burada 5) sınırlıdır.
- Oyuncu her tahminde, kalan hakkını gösterilir.
- Tahmin edilen sayının rastgele olması için random modülü kullanılmıştır.
- Kullanıcıdan alınan input'un bir sayı olup olmadığı kontrol edilmiştir.
- Kodun daha karmaşık hale getirilmesi için ekstra özellikler eklenebilir, örneğin istatistiksel analiz.
