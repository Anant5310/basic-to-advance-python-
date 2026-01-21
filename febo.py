n = int(input("Enter limit: "))
a, b = 2, 3

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b