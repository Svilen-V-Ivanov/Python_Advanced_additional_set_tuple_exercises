from collections import deque

material_values = list(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())

crafts = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

crafted = {}
is_crafted = False

while material_values and magic_levels:
    material = material_values.pop()
    magic = magic_levels.popleft()

    if magic == 0 and material == 0:
        continue
    if magic == 0:
        material_values.append(material)
        continue
    if material == 0:
        magic_levels.appendleft(magic)
        continue

    combination = material * magic

    if combination in crafts.keys():
        toy_name = crafts[combination]
        if toy_name in crafted:
            crafted[toy_name] += 1
        else:
            crafted[toy_name] = 1
        continue

    if combination < 0:
        new_value = material + magic
        material_values.append(new_value)
    if combination > 0:
        material_values.append(material + 15)

if 'Doll' in crafted.keys() and 'Wooden train' in crafted.keys():
    is_crafted = True
if 'Teddy bear' in crafted.keys() and 'Bicycle' in crafted.keys():
    is_crafted = True

if is_crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if material_values:
    print(f"Materials left: {', '.join(str(x) for x in reversed(material_values))}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for key, value in sorted(crafted.items()):
    print(f"{key}: {value}")
