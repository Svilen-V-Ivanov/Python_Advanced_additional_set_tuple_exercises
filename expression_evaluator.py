from collections import deque

expression = input().split()
numbers = deque()

command_dict = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}

for character in expression:
    if character in '+-/*':
        while len(numbers) > 1:
            first = numbers.popleft()
            second = numbers.popleft()
            result = command_dict[character](first, second)
            numbers.appendleft(result)

    else:
        numbers.append(int(character))

print(numbers.pop())
