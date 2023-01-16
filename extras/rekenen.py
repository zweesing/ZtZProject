import math

y = x = 16

connecties = 30
ans = (
    connecties
    * (4 ** (x * y - 2 * x - 2 * y + 4))
    * (3 ** (2 * x + 2 * y - 8))
    * (2**4)
)

# ans = math.factorial(26) / math.factorial(26 - 7)
print(ans)
