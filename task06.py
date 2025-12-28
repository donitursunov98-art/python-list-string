matn = input('Matn: ')

palindromlar = []

for soz in matn.split():
    if soz.lower() == soz[::-1].lower():
        palindromlar.append(soz)

print(palindromlar)
