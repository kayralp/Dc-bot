meme_dict = {
        "Crınge": "Garip ya da utandırıcı bir şey",
        "Lol": "Komik bir şeye verilen cevap",
        }
while True:
    word = input("Anlamadığınız bir kelime yazın (İlk harfi büyük yazıp diğerlerini küçük yazınız!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Bu kelime bulunamadı")
