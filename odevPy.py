def dikdortgen_cizdir(genislik, yukseklik):
    for i in range(yukseklik):
        print('*' * genislik)

def paralel_kenar_cizdir(kenar_uzunlugu, yukseklik):
    for i in range(yukseklik):
        print(' ' * i + '*' * kenar_uzunlugu)

def ikizkenar_dik_ucgen_cizdir(kenar_uzunlugu):
    for i in range(1, kenar_uzunlugu + 1):
        print('*' * i)

while True:
    print("\n(1) Dikdörtgen Çizdirme")
    print("(2) Paralel Kenar Çizdirme")
    print("(3) İkizkenar Dik Üçgen Çizdirme")
    print("Çıkmak için -1'e basınız.")
    
    secim = int(input("Seçiminizi Giriniz (1/2/3): "))
    
    if secim == -1:
        print("Çıkılıyor...")
        break

    elif secim == 1:
        genislik = int(input("Dikdörtgenin genişliğini giriniz: "))
        yukseklik = int(input("Dikdörtgenin yüksekliğini giriniz: "))
        dikdortgen_cizdir(genislik, yukseklik)

    elif secim == 2:
        kenar_uzunlugu = int(input("Paralel kenarın uzunluğunu giriniz: "))
        yukseklik = int(input("Paralel kenarın yüksekliğini giriniz: "))
        paralel_kenar_cizdir(kenar_uzunlugu, yukseklik)

    elif secim == 3:
        kenar_uzunlugu = int(input("İkizkenar dik üçgenin kenar uzunluğunu giriniz: "))
        ikizkenar_dik_ucgen_cizdir(kenar_uzunlugu)

    else:
        print("Yanlış değer girdiniz, lütfen tekrar deneyiniz.")
