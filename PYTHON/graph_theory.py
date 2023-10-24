import math
def exact(n, k):
  return (n * n - (n % k) * math.ceil(n / k) ** 2 - (k - n % k) * math.floor(n / k) ** 2) / 2
for case in range(int(input())):
  N, M = map(int, input().split())
  k = math.ceil(N * N / (N * N - 2 * M))
  while M > exact(N, k):
    k += 1
  print(k) 
