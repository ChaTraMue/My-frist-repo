import yfinance as yf

def analyse_stock(ticker, shares, buy_price):
    stock = yf.Ticker(ticker)
    info = stock.info

    name = info["longName"]
    price = info["currentPrice"]
    high = info["fiftyTwoWeekHigh"]
    low = info["fiftyTwoWeekLow"]
    value = round(price * shares, 2)
    cost = round(buy_price * shares, 2)
    profit = round(value - cost, 2)
    percent = round((profit / cost) * 100, 2)

    print("----------------------------")
    print("Company:", name)
    print("Current Price:", price)
    print("52 Week High:", high)
    print("52 Week Low:", low)
    print("Your Holdings:", shares, "shares")
    print("Current Value: $", value)
    print("Total Cost: $", cost)

    if profit > 0:
        print("Profit: +$", profit, "(+", percent, "%)")
    elif profit < 0:
        print("Loss: -$", abs(profit), "(", percent, "%)")
    else:
        print("Break even")

portfolio = [
    ("NVDA", 24, 131.31),
    ("AMD", 16, 122.61 ),
    ("ASML", 5.177, 744.62)
]

total_value = 0
total_cost = 0

for ticker, shares, buy_price in portfolio:
    analyse_stock(ticker, shares, buy_price)
    stock = yf.Ticker(ticker)
    price = stock.info["currentPrice"]
    total_value += price * shares
    total_cost += buy_price * shares

total_profit = round(total_value - total_cost, 2)
total_percent = round((total_profit / total_cost) * 100, 2)

print("----------------------------")
print("Total Portfolio Value: $", round(total_value, 2))
print("Total Cost: $", round(total_cost, 2))

if total_profit > 0:
    print("Total Profit: +$", total_profit, "(+", total_percent, "%)")
else:
    print("Total Loss: -$", abs(total_profit), "(", total_percent, "%)")