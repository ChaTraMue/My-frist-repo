import yfinance as yf

def analyse_stock(ticker, shares):
    stock = yf.Ticker(ticker)
    info = stock.info

    name = info["longName"]
    price = info["currentPrice"]
    high = info["fiftyTwoWeekHigh"]
    low = info["fiftyTwoWeekLow"]
    value = round(price * shares, 2)

    print("----------------------------")
    print("Company:", name)
    print("Current Price:", price)
    print("52 Week High:", high)
    print("52 Week Low:", low)
    print("Your Holdings:", shares, "shares")
    print("Current Value: $", value)

portfolio = [
	("NVDA", 100),
	("AAPL", 50),
	("YAL.AX", 100),
]

total = 0
for ticker, shares in portfolio: 
	analyse_stock(ticker, shares)
	stock = yf.Ticker(ticker)
	price = stock.info["currentPrice"]
	total += price * shares

print("----------------------------")
print("Total Portfolio Value: $", round(total, 2))
