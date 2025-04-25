# 1. Kullanıcıdan dosya adını alalım
filename = "metinyazma.txt"

# Kullanıcıdan metin aldığımız kısım
user_input = input("Bir metin girin ve dosyaya yazalım: ")

# Dosyayı yazma moduna aldık
with open(filename, 'w') as file:
    file.write(user_input)

# 2. Yazılan dosyayı okuyup ekrana yazdır
print("\nDosya içeriği:")
with open(filename, 'r') as file:
    content = file.read()
    print(content)

# 3. Kullanıcıdan 5 farklı satır alalım ve bu satırları dosyaya ekleyelim.
print("\n5 farklı satır girin (her satırdan sonra Enter'a basın):")
lines = []
for i in range(5):
    line = input(f"Satır {i+1}:")
    lines.append(line)

# Dosyaya satır satır yazma işlemi (append)
with open(filename, 'a') as file:
    for line in lines:
        file.write(line + '\n')

# 4. Dosyayı tekrar okuyalım ve satır satır ekrana yazdıralım
print("\nDosya içeriği (satır satır):")
with open(filename, 'r') as file:
    lines_in_file = file.readlines()
    for line in lines_in_file:
        print(line.strip())
