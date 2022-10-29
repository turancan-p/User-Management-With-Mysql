print("Quiz uygulamama hosgeldin!")
meslek_secim = None
secim_1 = None
while True:
    if meslek_secim is not None:
        secim_1 = input(f"{meslek_secim} olarak giris yaptin, eger geri donmek istiyorsan `g` yaz\n")
        if secim_1 != "g":
            print(f"{meslek_secim} olarak devam ediyorsun")
        else:
            meslek_secim = None
    else:
        meslek_secim = input("Ogretmen olarak giris yapmak istiyorsan `ogretmen` ,ogrenci olarak giris yapmak istiyorsan `ogrenci` yaz\n")