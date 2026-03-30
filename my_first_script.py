import yfinance as yf
import pandas as pd

portfolio = [
    ("NVDA", 24, 131.31),
    ("AMD", 16, 122.61),
    ("ASML", 5.177, 744.67)
]

rows = []

for ticker, shares, buy_price in portfolio:
    stock = yf.Ticker(ticker)
    info = stock.info

    name = info["longName"]
    price = info["currentPrice"]
    value = round(price * shares, 2)
    cost = round(buy_price * shares, 2)
    profit = round(value - cost, 2)
    percent = round((profit / cost) * 100, 2)

    rows.append({
        "Company": name,
        "Ticker": ticker,
        "Shares": shares,
        "Buy Price": buy_price,
        "Current Price": price,
        "Value": value,
        "Cost": cost,
        "Profit": profit,
        "Return %": percent
    })

df = pd.DataFrame(rows)
print(df.to_string(index=False))

print("\nTotal Value:  $", round(df["Value"].sum(), 2))
print("Total Cost:   $", round(df["Cost"].sum(), 2))
print("Total Profit: $", round(df["Profit"].sum(), 2))

print("\nBest Performer:")
print(df.loc[df["Return %"].idxmax(), "Company"])

print("\nWorst Performer:")
print(df.loc[df["Return %"].idxmin(), "Company"])

print("\nAverage Return:", round(df["Return %"].mean(), 2), "%")

df.to_excel("portfolio.xlsx", index=False)
print("\nPortfolio saved to portfolio.xlsx")