text = input('input: ')

pairs = text.split(', ')

for pair in pairs:
    separated_pair = pair.split(':')
    result = f'{separated_pair[0]}: {separated_pair[1]}'
    print(result)
