# x = int(input())
print("Input array")
# n = list(map(int, input().strip().split()))

n = int(input())
x = [int(x) for x in input().split(" ", n-1)]

print(x)
