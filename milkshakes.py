from collections import deque

chocolate = [int(x) for x in input().split(', ')]
milk = deque(int(x) for x in input().split(', '))
milkshakes = 0

while chocolate and milk and milkshakes < 5:
    choco_cup = chocolate.pop()
    milk_cup = milk.popleft()

    if choco_cup <= 0 and milk_cup <= 0:
        continue
    if choco_cup <= 0:
        milk.appendleft(milk_cup)
        continue
    if milk_cup <= 0:
        chocolate.append(choco_cup)
        continue

    if choco_cup == milk_cup:
        milkshakes += 1
    else:
        chocolate.append(choco_cup - 5)
        milk.append(milk_cup)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
else:
    print(f"Chocolate: empty")

if milk:
    print(f"Milk: {', '.join(str(x) for x in milk)}")
else:
    print(f"Milk: empty")
