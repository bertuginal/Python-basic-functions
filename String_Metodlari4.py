yazi = "Hafta içinde en yoğun geçen gün çarşamba olabilir."
degis = yazi.replace(' ','*')
# print(degis)

yazi1 = "Bütün insanlar suçlu değildir, ama bütün hayvanlar masumdur."
degis1 = yazi1.replace('bütün','tüm')
degis2 = yazi1.replace(' ','')

birles = yazi1.split()
a = ''.join(birles)

bol = yazi1.split(' ')

# print(degis1)
# print(degis2)
# print(a)
# print(bol)
# print(bol[0])
