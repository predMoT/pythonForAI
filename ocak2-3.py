yas = int(input("yaşınızı girin: "))

if 0<= yas <=12:
    print("çocuk")
elif 12< yas <18:
    print("genç")
elif 18<= yas <65:
    print("Yetişkin")
elif 65<= yas:
    print("Yaşlı")