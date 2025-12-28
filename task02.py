text = input('Input: ')

items = text.split(', ')

formatted_items = []

for item in items:
    item = item.lower()
    item = item.replace(' ', '_')
    formatted_items.append(item)
result = '_'.join(formatted_items)

print(result)
