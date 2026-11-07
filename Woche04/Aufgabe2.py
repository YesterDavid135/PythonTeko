
print("A: For-Loop")
for i in reversed(range(11)):
    print(i)

print("B: While-Loop")
i = 10
while i >= 0:
    print(i)
    i -= 1

print("C: While-Loop Fussgesteuert")
i = 10
while True:
    print(i)
    i -= 1
    if i < 0:
        break