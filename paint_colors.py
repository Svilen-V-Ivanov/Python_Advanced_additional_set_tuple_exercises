from collections import deque

string = deque(input().split())

main_color = {
    'red',
    'yellow',
    'blue'
}
off_color = {
    'orange',
    'purple',
    'green'
}
colors = []
copy_colors = []

while string:
    first_part = string.popleft()
    second_part = string.pop() if string else ''
    word = first_part + second_part
    reversed_word = second_part + first_part

    if word in main_color or word in off_color:
        colors.append(word)
        continue
    if reversed_word in main_color or reversed_word in off_color:
        colors.append(reversed_word)
        continue

    first_part = first_part[:-1]
    second_part = second_part[:-1]

    if first_part:
        string.insert(len(string) // 2, first_part)
    if second_part:
        string.insert(len(string) // 2, second_part)

for _ in colors:
    copy_colors.append(_)

for color in colors:
    if color == 'orange':
        if 'red' not in colors or 'yellow' not in colors:
            copy_colors.remove(color)
    if color == 'purple':
        if 'red' not in colors or 'blue' not in colors:
            copy_colors.remove(color)
    if color == 'green':
        if 'blue' not in colors or 'yellow' not in colors:
            copy_colors.remove(color)

print(copy_colors)
