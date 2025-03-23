def sayı_islemleri():
    # Kullanıcıdan 5 adet sayı alalım
    sayılar = []
    for i in range(5):
        sayi = float(input(f"{i+1}. sayıyı girin: "))
        sayılar.append(sayi)

    # Liste ile ilgili işlemler
    toplam = sum(sayılar)
    ortalama = toplam / len(sayılar)
    en_büyük = max(sayılar)
    en_küçük = min(sayılar)

    # Sonuçları yazdıralım
    print("\n--- Sayı İşlemleri ---")
    print(f"Liste: {sayılar}")
    print(f"Toplam: {toplam}")
    print(f"Ortalama: {ortalama}")
    print(f"En büyük sayı: {en_büyük}")
    print(f"En küçük sayı: {en_küçük}")


def kelime_islemleri():
    # Kullanıcıdan kelimeleri alalım
    kelimeler = []
    while True:
        kelime = input("Bir kelime girin (çıkmak için 'q' tuşuna basın): ")
        if kelime.lower() == 'q':
            break
        kelimeler.append(kelime)

    # Kelimeleri ters sıralayalım
    kelimeler.reverse()

    # Sonuçları yazdıralım
    print("\n--- Kelime İşlemleri ---")
    print("Ters sıralanmış kelimeler:")
    for kelime in kelimeler:
        print(kelime)


def tekrar_edenleri_kaldırma():
    # Kullanıcıdan bir liste alalım
    liste = []
    n = int(input("\nKaç adet eleman ekleyeceksiniz? "))
    for i in range(n):
        eleman = input(f"{i+1}. elemanı girin: ")
        liste.append(eleman)

    # Tekrar eden elemanları kaldırmak için set() kullanıyoruz
    benzersiz_liste = list(set(liste))

    # Sonuçları yazdıralım
    print("\n--- Tekrar Eden Elemanları Kaldırma ---")
    print("Tekrar eden elemanlar kaldırıldı:", benzersiz_liste)


# Programı çalıştırma
def main():
    sayı_islemleri()
    kelime_islemleri()
    tekrar_edenleri_kaldırma()

if __name__ == "__main__":
    main()

#ocak 4.hafta