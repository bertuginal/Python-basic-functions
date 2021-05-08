sentence = "I don't want to see the back, I want to see the front"
sentence1 = sentence.upper() # tüm karakterler büyük
sentence2 = sentence.lower() # tüm karakterler küçük
sentence3 = sentence.title() # tüm kelimelerin ilk harfi büyük
sentence4 = sentence.capitalize() # Sadece en baştaki harf büyük geri kalan küçük
print(sentence1)
print(sentence2)
print(sentence3)
print(sentence4)


metin = "      Vatanını en çok seven, görevini en iyi yapandır." 
metin1 = metin.strip() # en başta boşluk varsa siler
metin2 = metin.split() # her kelimeyi teker teker ayırır
metin3 = metin.split(',') # her kelimeyi ayırır ve , işaretini siler.
metin4 = metin.split()
metin5 = '-'.join(metin4) # split ile parçalanmış cümleyi birleştirip eski haline getirir ve ayrıca '' içine ne yazılırsa ona göre cümleyi birleştirir.


print(metin1)
print(metin2)
print(metin2[0]) # her kelimeyi ayırdı ve 0. indeksi yazdırdı
print(metin3)
print(metin5)

passage = "Kazandığımızdan en emin olduğumuz an, kaybetmeye en yakın olduğumuz andır."

sorgu = passage.find('emin') # cümlede istediğimiz kelimenin yerini bulma
print(sorgu)

varmi = passage.startswith('K') # cümle K ile mi başlıyor. Evet ise True Hayır ise False
print(varmi)

sorgulama = passage.endswith('r') # cümle r ile mi bitiyor. Evet ise True Hayır ise False
print(sorgulama)

degis = passage.replace('an','yakın') # an ile yakın yeri değişir
degis1 = passage.replace('emin','kesin').replace('yakın','alakalı') # 1den fazla yan yana replace kullanılabilir
print(degis)
print(degis1)

length = len(passage)
bosluk = passage.center(120) # (yazdığımız değer - cümlenin uzunluğu = sonuc) yapılır. Çıkan sonuç 2 ye bölünür ve sağa ve sola eşit boşluk dağıtılır.
bosluk1 = passage.center(120,'*')
print(length)
print(bosluk)
print(bosluk1)

yazi = "  Beni öldürmeyen şey beni güçlendirir.  "
sonuc1 = yazi.lstrip() # sadece soldaki boşluğu siler
sonuc2 = yazi.rstrip() # sadece sağdaki boşluğu siler
print(sonuc1)
print(sonuc2)

yazi2 = "www.bertuginal.com"
sonuc3 = yazi2.strip('w.moc')
print(sonuc3)











