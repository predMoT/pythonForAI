def hesap_makinesi():
    # Kullanıcıdan iki sayı alalım
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))

    # İşlemleri yapalım
    toplam = sayi1 + sayi2
    fark = sayi1 - sayi2
    carpim = sayi1 * sayi2
    if sayi2 != 0:
        bolum = sayi1 / sayi2
    else:
        bolum = "Tanımsız (bölme işlemi sıfıra yapılamaz)"

    # Sonuçları yazdıralım
    print(f"Toplam: {toplam}")
    print(f"Fark: {fark}")
    print(f"Çarpım: {carpim}")
    print(f"Bölüm: {bolum}")


def palindrom_kontrol():
    kelime = input("Bir kelime girin: ").lower()

    # Kelimenin tersini alıp karşılaştıralım
    if kelime == kelime[::-1]:
        print(f"'{kelime}' bir palindromdur.")
    else:
        print(f"'{kelime}' bir palindrom değildir.")


def yasanin_100_olmasi():
    yas = int(input("Yaşınızı girin: "))

    # 100 yaşına ulaşmak için gereken yıl sayısını hesaplayalım
    if yas < 100:
        yil_sonra = 100 - yas
        print(f"{yil_sonra} yıl sonra 100 yaşına ulaşacaksınız.")
    elif yas == 100:
        print("Zaten 100 yaşına ulaştınız!")
    else:
        print("100 yaşını geçmişsiniz.")


def main():
    print("Hesap Makinesi Programı")
    while True:
        print("\nSeçim yapın:")
        print("1. Hesap Makinesi (Toplama, çıkarma, çarpma, bölme)")
        print("2. Palindrom Kontrolü")
        print("3. Yaşınızı girerek 100 yaşına ulaşmak için gereken yılı hesapla")
        print("4. Çıkış")

        secim = input("Seçiminizi yapın (1/2/3/4): ")

        if secim == "1":
            hesap_makinesi()
        elif secim == "2":
            palindrom_kontrol()
        elif secim == "3":
            yasanin_100_olmasi()
        elif secim == "4":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek, tekrar deneyin.")


if __name__ == "__main__":
    main()

#python şubat 1.hafta ödevi