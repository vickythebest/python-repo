# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0
def coincount(coin,amount):
    result=[1+amount]*(1+amount)
    print("result: ",result)
    result[0]=0
    for n in range(1,(amount+1)):
        for c in coin:
            if n-c>=0:
                result[n]=min(result[n],1+result[n-c])
                print(n, c, " - ",1+result[n-c],"  min result: ",result)
    if result[amount]!=amount:
        return result[amount]
    else:
        return -1
    # return result [amount] if result[amount] != amount else -1

nums=[1,2,5]
print(coincount([1,2,5],11))