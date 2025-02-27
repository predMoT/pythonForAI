from human import Human
import mathematics as math

print(math.bol(50,3))


print("Hello")

faiz = 1.59
vade = "36"
krediadi = "ihtiyaç kredisi"

print(type(faiz))
print(type(vade))
print(type(krediadi))

print(int(vade)+12)
#print(int(krediadi))
faiz = str(faiz)
print(type(faiz))

vade = input("lütfen istediğiniz vade sayısını giriniz: ")
print(type(vade))
#18.satırda hata var düzeltemedim :)
vade = int(vade) + 12

#string interpolation
#seçtiğiniz vade sonucu ortaya çıkan vade
print("seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))


isim = "Müslüm"
metin = "Hello {name}".format(name="Halit")
print(metin)

#f-string
metin = f"hoşgeldiniz {1+1}"
print(metin)

#listeler
#döngüler
#fonksiyonlar

dizi = ["ihtiyaç kredisi", 10, 5.2, True]
print(dizi)

krediler = ["ihtiyaç krdisi", "taşıt kredisi", "konut kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler)) #length
#print(krediler[3]) => hata verir

krediler.append("özel kredi")
print(krediler)

krediler.append("X kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("taşıt kredisi")
print(krediler)


krediler.remove("taşıt kredisi")
print(krediler)

krediler.extend("Y kredisi, Z kredisi")
print(krediler)

#for
# i=0, i<10

x=10
for i in range(x):
    print("xx")
    print(i)
    
print("********************")
for i in range(5,10):
    print(i)
print("********************")
for i in range(0,51,10):
    print(i)
print("********************")
#for i in range(0.1,0.5):
#   print(i)
krediler = ["ihtiyaç kredisi", "taşıt kredisi", "konut kredisi"]
for kredi in krediler:
    print(kredi)
print("********************")
for i in range(len(krediler)):
    print(krediler[i])
print("********************")


#sonsuz döngü
i = 0
while i < 10:
    print("x")
    i += 1
print("y")

print("********************")

while True:
    print("X")
    break


print("****son döngü****")

i = 0
while i < len(krediler):
    i += 1
    print(krediler[i])
    print(i)    
    if krediler[i] == "konut kredisi":
        break
    
#fonksiyonlar

fiyat = 100
indirim = 20
#defination define
def calculate():
    print(100-20)

def calculateWithParams(fiyat, indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba {name}")
    
calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Halit")
sayHello("Müslüm")



def calculateAndReturn(fiyat,indirim):
    return fiyat-indirim

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)

#void
def calculateprice(price, discount):
    print(price-discount)
    
def calculatePriceandReturn(price, discount):
    return price-discount

print("*******************")
def calculateprice(length, price):
    try:
        return int(length) + price
    except ValueError:
        print(f"Error calculating {length} for price: {price}")
        return None

print(f"148.satir: {calculateprice(100, 50)}")
print(f"151.satir: {calculateprice(200, 25)}")
print("****************")


#sınıflar
#modules
#paket yönetimi


#instance => örnek
human1 = Human("Merve")
human1.talk("Merhaba")
human1.walk()


human2 = Human("Cem")
human2.talk("Selam")
human2.walk()