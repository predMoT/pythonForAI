# sayısal notu harf notuna çevirme
dersnot = int(input("sınav puanınızı giriniz: "))

if 90 <= dersnot <=100:
    print("Harf notu = A")
elif 80<= dersnot < 90:
    print("Harf notu = B")
elif 70<= dersnot < 80:
    print("Harf notu = C")
elif 60<= dersnot < 70:
    print("Harf notu = D")
elif 50<= dersnot < 60:
    print("Harf notu = E")
elif 0<= dersnot < 50:
    print("Harf notu = F")