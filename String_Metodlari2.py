a = "35164565"
b = a.isalpha() # stringin tamamı harf mi diye sorgular
c = a.isdigit() # stringin tamamı rakam mı diye sorgular
# print(b)
# print(c)

cikti = "bugün süperim".center(62,'-') # stringi tam merkeze koyar ve sağına soluna - işaretini dağıtır
cikti1 = "bugün süperim".ljust(62,'-') # stringi tam sola koyar ve sağına - işareti koyar
cikti2 = "bugün süperim".rjust(62,'-') # stringi tam sağa koyar ve soluna - işareti koyar
print(cikti)
print(cikti1)
print(cikti2)