yazi = "Aptallığın en büyük kanıtı aynı şeyleri tekrarlayıp farklı sonuçlar almayı beklemektir."
sayici = yazi.count('k') # kaç tane k olduğunu gösterir
sayici1 = yazi.count('k',0,25)
sayici2 = yazi.count('ar') # kaç tane ar olduğunu gösterir
degis = yazi.startswith('Apt')
degis1 = yazi.endswith('beklemektir.')
bul = yazi.find('büyük',0,20)
bul1 = yazi.index('büyük')


print(sayici)
print(sayici1)
print(sayici2)
print(degis)
print(degis1)
print(bul)
print(bul1)


