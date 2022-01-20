n, m = map(int, input().split())
result = 0
for _ in range(n):
    data = list(map(int,input().split()))
    minValue = min(data)
    result = max(minValue,result)

print(result)