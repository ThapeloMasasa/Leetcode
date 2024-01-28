# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


def maxProfit(stocks):
    min_price = float('inf')
    max_profit = 0
    for i in range(len(stocks)):
        if stocks[i] < min_price:
            min_price = stocks[i]
        elif (stocks[i] - min_price) > max_profit:
            max_profit = stocks[i] - min_price
    return max_profit

#tests
stocks1 = [7,1,5,3,6,4]
ans = maxProfit(stocks1)
print(ans)
#test2
stocks2 = [7,6,4,3,1]
ans2 = maxProfit(stocks2)
print(ans2)
