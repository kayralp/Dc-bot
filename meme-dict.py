dictionary_of_abbreviations = {
        "Gg": "İyi oyun demek için kullanılan kısaltma",
        "Ez": "Kolaydı demek için kullanılan kısaltma",
        "Gt": "Geri takip demek için kullanılan kısaltma",
        "Ty": "Teşekkür ederim demek için kullanılan kısaltma",
        }
while True:
    word = input("Anlamadığınız bir kelime yazın (İlk harfi büyük yazıp diğerlerini küçük yazınız!): ")
    if word in dictionary_of_abbreviations.keys():
        print(dictionary_of_abbreviations[word])
    else:
        print("Bu kelime bulunamadı")
