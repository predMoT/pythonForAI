# 1. 1’den 100’e kadar olan sayıları ekrana yazdıran program
def yazdir_1den_100():
    for i in range(1, 101):
        print(i)

# 2. 1’den 100’e kadar sadece çift sayıları ekrana yazdıran program
def yazdir_cift_sayilar():
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)

# 3. Kullanıcıdan bir sayı alıp, bu sayının faktöriyelini hesaplayan program
def faktoriyel(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def hesapla_faktoriyel():
    sayi = int(input("Bir sayı girin: "))
    print(f"{sayi}! = {faktoriyel(sayi)}")

# 4. 1’den 100’e kadar olan tüm asal sayıları bulan program
def asal_mi(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def yazdir_asal_sayilar():
    for i in range(1, 101):
        if asal_mi(i):
            print(i)

# Kullanıcıdan hangi işlemi yapmak istediğini soralım
print("Yapmak istediğiniz işlemi seçin:")
print("1 - 1'den 100'e kadar olan sayıları yazdır")
print("2 - 1'den 100'e kadar olan çift sayıları yazdır")
print("3 - Bir sayının faktöriyelini hesapla")
print("4 - 1'den 100'e kadar olan asal sayıları yazdır")

secim = int(input("Seçiminizi yapın (1-4): "))

if secim == 1:
    yazdir_1den_100()
elif secim == 2:
    yazdir_cift_sayilar()
elif secim == 3:
    hesapla_faktoriyel()
elif secim == 4:
    yazdir_asal_sayilar()
else:
    print("Geçersiz seçim!")
    
#ocak 3.hafta