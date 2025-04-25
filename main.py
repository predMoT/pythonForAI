print("kodlamaio")
baslik = "Taşıt Kredisi"
print(baslik)
#string => metinsel ifade
baslik = "ihtiyaç kredisi"
print(baslik)
#int, integer => tam sayı
vade = 36
ekvade = 6

#float, decimal, double
aylikodeme = 250.50

#bool, boolean => true or false
yukselistemi = True

#mathematical operators

# +
print(12+5)
print(vade + 12)
print(vade + ekvade)
print(36 + 6)

# -
print(5-3)
print(vade - 12)
print(vade - ekvade)
print(36-12)

# *
print(5*4)
print(vade * 2)
print(vade * ekvade)
print(36*12)

# /
print(12/6)
print(vade / 4)
print(vade / ekvade)
print(25/5)


yenivade = vade / 2
fiyat = 120
indirimlifiyat = fiyat - 20

print(yenivade)
print(indirimlifiyat)

# % => mod operator
print(10%3)
print(vade % 5)
print(vade % ekvade)
print(30%10)

#logical operators
print(1 == 1)
print(1 == 2)


#ctrl + k, ctrl + c
# print(1 > 2)
# print(3 > 1)
# print(1 > 1)
# print(1 >= 1)

print(1 < 1)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

print(1 != 1)
print(1 != 2)

#or and

print(1 > 2 or 5 > 2)
print(1 < 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 > 2 and 3 > 2)

print(2 > 1 or 1 > 2 and 3 > 2)


#karar yapıları
#if else
sayi1 = 10
sayi2 = 15
#sayı 1 sayı 2 den daha büyük çıkarsa ekrana sayı 1 daha büyük yazdır
#condition

#indent
if sayi1 <= sayi2:
    print("sayi1 sayi2 den daha küçük")
#eğer if blogguna girmez ise
elif sayi1 == sayi2:
    print ("iki sayi esittir")
#eğer if ve else if bloklarında hiç birbirine girmez ise
else:
    print("sayi1 sayi2 den büyüktür")
    
print("*******************************")
    
if sayi1 <= sayi2:
    print("sayi1 sayi2 den küçüktür")
if sayi1 == sayi2:
    print("iki sayı eşittir")
else:
    print("sayı1 sayı2'den büyüktür")
    
    
print("burasi if blogunun disidir")