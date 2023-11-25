N, B = map(int, input().split())
result = ''

while N > 0:
    remainder = N % B
    result = str(remainder) + result if remainder < 10 else chr(ord('A') + remainder - 10) + result
    N //= B

print(result if result else '0')

