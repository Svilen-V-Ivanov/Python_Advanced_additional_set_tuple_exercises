from collections import deque


def honey_making(bee, operation, nectar):
    produce = 0
    if operation == '+':
        produce = bee + nectar
    elif operation == '-':
        produce = abs(bee - nectar)
    elif operation == '*':
        produce = bee * nectar
    else:
        produce = bee / nectar

    return produce


bees = deque(int(x) for x in input().split())
nectars = deque(int(x) for x in input().split())
process = input().split(' ')
honey = 0

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()
    if nectar < bee:
        bees.appendleft(bee)
        continue
    elif nectar == 0:
        continue
    else:
        if process:
            operation = process.pop(0)
            current_honey = honey_making(bee, operation, nectar)
            honey += current_honey

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectars:
    print(f"Nectar left: {', '.join(str(x) for x in nectars)}")
