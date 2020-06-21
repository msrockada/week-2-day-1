height = int(input())
for b in range(height):
    b = int(input())

limit = 0
r = int(input())
for b in range(height):
    if b >=r:
        limit = limit +1

print(limit)
