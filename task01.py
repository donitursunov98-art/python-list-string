fish = input('Input: ')

parts = fish.split()

familiya = parts[0]
ism_sharif = ' '.join(parts[1:])

print(f'{ism_sharif}, {familiya}')
