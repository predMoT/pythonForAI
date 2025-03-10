def metin_kaydet_yazdir():
    # Kullanıcıdan alınan metni kaydetmek için
    text = input("Lütfen metninizi girin: ")

    # Metni .txt dosyasına yazmak için
    with open("metin.txt", "w") as file:
        file.write(text)

def satir_kaydet_yazdir():
    # Kullanıcıdan alınan 5satır verisini kaydetmek için
    numbers = []
    for i in range(5):
        while True:
            try:
                number = int(input(f"Satır {i+1} numarasını girin: "))
                if number < 0 or number > 100:
                    print("Lütfen bir sayı Girin.")
                else:
                    numbers.append(number)
                    break
            except ValueError:
                print("Lütfen bir sayı Girin.")

    # Kaydedilen satırları .txt dosyasına yazmak için
    with open("satirlar.txt", "w") as file:
        for number in numbers:
            file.write(str(number) + "\n")

def metin_yazdir():
    try:
        # Metni .txt dosyasını okumasak için
        with open("metin.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Dosya bulunamadı.")

def satir_yazdir():
    try:
        # Satırları .txt dosyasını okumasak için
        with open("satirlar.txt", "r") as file:
            for i, number in enumerate(file.readlines()):
                if i == 0:
                    print(f"Satır {i+1}: ", end="")
                else:
                    print(f"Satır {i+1}: ", end="")
                print(number.strip())
    except FileNotFoundError:
        print("Dosya bulunamadı.")

def main():
    while True:
        print("\n1. Metni Kaydet & Yazdır")
        print("2. Satırları Kaydet & Yazdır")
        print("3. Çıkış Yap")
        choice = input("Lütfen bir sayı seçin: ")
        if choice == "1":
            metin_kaydet_yazdir()
            metin_yazdir()
        elif choice == "2":
            satir_kaydet_yazdir()
            satir_yazdir()
        elif choice == "3":
            break
        else:
            print("Lütfen bir sayı Girin.")

if __name__ == "__main__":
    main()
