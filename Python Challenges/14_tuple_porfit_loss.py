#  Program to Calculate Portfolio Cost and Profit/Loss

# List of tuples containing share details: (share name, cost price, number of shares, selling price)
portfolio = [
    ("Apple", 150, 10, 170),
    ("Tesla", 800, 5, 850),
    ("Amazon", 3100, 2, 3000),
    ("Google", 2800, 4, 2900)
]

# Calculate total cost and total gain/loss
total_cost = sum(share[1] * share[2] for share in portfolio)
total_sale = sum(share[3] * share[2] for share in portfolio)
total_profit = total_sale - total_cost

# Displaying results
print("Total cost of portfolio:", total_cost)
print("Total selling price:", total_sale)
if total_profit > 0:
    print("Total amount gained:", total_profit)
elif total_profit < 0:
    print("Total amount lost:", abs(total_profit))
else:
    print("No gain, no loss.")
