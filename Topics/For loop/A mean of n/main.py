n = int(input())

total = 0

# https://flake8.codes/WPS519/
# for _ in range(0, n):
#    total += int(input())

total = sum(int(input()) for _ in range(n))

print(float(total / n))
