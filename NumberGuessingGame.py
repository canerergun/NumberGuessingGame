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
