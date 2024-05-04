import random

# Yemek listesi
yemekler = {
    "makarna": ["makarna", "domates sosu", "rendelenmiş peynir"],
    "kıymalı patates": ["kıyma", "patates", "soğan", "sarımsak", "domates"],
    "mercimek çorbası": ["kırmızı mercimek", "soğan", "havuç", "tuz", "karabiber", "zeytinyağı"],
    "tavuk sote": ["tavuk göğsü", "biber", "soğan", "mantar", "sarımsak", "tuz", "karabiber"],
    "mantar sote": ["mantar", "soğan", "biber", "sarımsak", "zeytinyağı", "tuz", "karabiber"],
    "karnıyarık": ["patlıcan", "kıyma", "soğan", "domates", "biber", "sarımsak"],
    "kuru fasulye": ["kuru fasulye", "soğan", "sarımsak", "domates salçası", "tuz"],
    "kumpir": ["patates", "mısır", "bezelye", "salatalık", "sosis", "ketçap", "mayonez"],
    "pizza": ["pizza tabanı", "domates sosu", "rendelenmiş kaşar peyniri", "sucuk", "mantar", "biber"],
    "kuzu tandır": ["kuzu eti", "soğan", "sarımsak", "tuz", "karabiber", "kekik"]
}

# Kullanıcıdan istenen yemek türünü al
yemek_turu = input("Hangi tür yemek istersiniz? (örn: makarna, kıymalı patates, tavuk sote): ")

# Kullanıcıya rastgele bir yemek öner
onerilen_yemek = random.choice(list(yemekler.keys()))
print(f"Önerilen yemek: {onerilen_yemek}")

# Önerilen yemeğin malzemelerini listele
malzemeler = yemekler[onerilen_yemek]
print("Malzemeler:")
for malzeme in malzemeler:
    print("-", malzeme)

# Tarifi göster
print("Tarif:")
print(f"{onerilen_yemek} yapmak için gerekli malzemeleri hazırlayın. Sonrasında malzemeleri sırasıyla kullanarak yemeği pişirin. Afiyet olsun!")

# Tarif komutları
if onerilen_yemek == "makarna":
    print("1. Tencerede su kaynatın.")
    print("2. Kaynayan suya makarnayı ekleyin ve pişirin.")
    print("3. Pişen makarnayı süzün.")
    print("4. Domates sosu ve rendelenmiş peyniri ekleyerek karıştırın.")
elif onerilen_yemek == "kıymalı patates":
    print("1. Patatesleri soyun ve küp küp doğrayın.")
    print("2. Soğanı ve sarımsağı doğrayın.")
    print("3. Kıymayı kavurun ve içine doğranmış soğanı ekleyin.")
    print("4. Patatesleri ekleyerek kavurun.")
    print("5. Domatesleri ve baharatları ekleyerek pişirin.")
    print("6. Afiyet olsun!")
# Diğer yemekler için de aynı şekilde tarifleri ekleyebilirsiniz
elif onerilen_yemek == "mercimek çorbası":
    print("1. Mercimeği yıkayıp süzün.")
    print("2. Soğanı ve havucu doğrayın.")
    print("3. Zeytinyağında soğanı ve havucu kavurun.")
    print("4. Mercimeği ekleyin ve suyunu ekleyerek pişirin.")
    print("5. Baharatları ekleyin ve blendırdan geçirerek çorbayı krema kıvamına getirin.")
    print("6. Afiyet olsun!")
elif onerilen_yemek == "tavuk sote":
    print("1. Tavuk göğsünü doğrayın.")
    print("2. Soğanı, biberi ve mantarı doğrayın.")
    print("3. Zeytinyağında tavukları kavurun.")
    print("4. Soğanı ekleyin ve kavurun.")
    print("5. Biber ve mantarı ekleyerek pişirin.")
    print("6. Baharatları ekleyin ve servis yapın.")
    print("7. Afiyet olsun!")
# Diğer yemekler için de aynı şekilde tarifleri ekleyebilirsiniz
elif onerilen_yemek == "karnıyarık":
    print("1. Patlıcanları alacalı soyun ve uzunlamasına ikiye kesin.")
    print("2. İç harcı için kıymayı kavurun, soğanı ve biberleri ekleyin.")
    print("3. Patlıcanların içini oyarak iç harcı ekleyin.")
    print("4. Domatesleri rendeleyip üzerine dökün.")
    print("5. Fırında pişirin ve servis yapın.")
    print("6. Afiyet olsun!")
elif onerilen_yemek == "mantar sote":
    print("1. Mantarları dilimleyin.")
    print("2. Soğanı ve sarımsağı doğrayın.")
    print("3. Zeytinyağında soğanı ve sarımsağı kavurun.")
    print("4. Mantarları ekleyerek soteleyin.")
    print("5. Baharatları ekleyin ve servis yapın.")
    print("6. Afiyet olsun!")
# Diğer yemekler için de aynı şekilde tarifleri ekleyebilirsiniz
elif yemek == "pizza":
            print("1. Pizza tabanını hazırlayın.")
            print("2. Domates sosunu tabana sürün.")
            print("3. Rendelenmiş kaşar peyniri serpin.")
            print("4. Sucuk, mantar ve biber dilimlerini ekleyin.")
            print("5. Önceden ısıtılmış fırında pişirin ve servis yapın.")
            print("6. Afiyet olsun!")
        elif yemek == "karnıyarık":
            print("1. Patlıcanları alacalı soyun ve uzunlamasına ikiye kesin.")
            print("2. İç harcı için kıymayı kavurun, soğanı ve biberleri ekleyin.")
            print("3. Patlıcanların içini oyarak iç harcı ekleyin.")
            print("4. Domatesleri rendeleyip üzerine dökün.")
            print("5. Fırında pişirin ve servis yapın.")
            print("6. Afiyet olsun!")
        elif yemek == "mantar sote":
            print("1. Mantarları dilimleyin.")
            print("2. Soğanı ve sarımsağı doğrayın.")
            print("3. Zeytinyağında soğanı ve sarımsağı kavurun.")
            print("4. Mantarları ekleyerek soteleyin.")
            print("5. Baharatları ekleyin ve servis yapın.")
            print("6. Afiyet olsun!")
