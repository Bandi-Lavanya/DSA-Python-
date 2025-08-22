class StockSpannerBrute:
    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        span = 1
        i = len(self.prices) - 2
        while i >= 0 and self.prices[i] <= price:
            span += 1
            i -= 1
        return span


# Example
sp = StockSpannerBrute()
print([sp.next(x) for x in [7,2,1,3,3,1,8]])
[1, 1, 1, 3, 4, 1, 7]

def stockSpan(prices):
    n = len(prices)
    span = [0] * n
    stack = []  # will store indices

    for i in range(n):
        # Pop smaller or equal elements (they can't be PGE)
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        if not stack:  
            span[i] = i + 1   # no greater element → span = i+1
        else:  
            span[i] = i - stack[-1]  # distance from previous greater

        stack.append(i)

    return span


# Example
prices = [100, 80, 60, 70, 60, 75, 85]
print(stockSpan(prices))  # Output: [1, 1, 1, 2, 1, 4, 6]
