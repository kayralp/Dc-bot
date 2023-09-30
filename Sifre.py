import random
semboller = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

uzunluk = int(input("Şifrenizin uzunluğunu giriniz =>"))
parola = ""
for i in range(uzunluk):
    parola += random.choice(semboller)

print(parola)