n = int(input("Введіть додатне ціле число n: "))

total = 0

for i in range(1, n + 1):
    print(i)
    total += i

print("Сума:", total)

while n >= 1:
    print(n)
    n -= 1
