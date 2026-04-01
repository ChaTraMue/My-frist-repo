import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

portfolio = [
    ("NVDA", 24, 131.31),
    ("AMD", 16, 122.61),
    ("ASML", 5.177, 744.67)
]

print("Pulling live market data...")

rows = []

for ticker, shares, buy_price in portfolio:
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

    rows.append({
        "Company": name,
        "Ticker": ticker,
        "Shares": shares,
        "Buy Price": buy_price,
        "Current Price": price,
        "52W High": high,
        "52W Low": low,
        "Value": value,
        "Cost": cost,
        "Profit": profit,
        "Return %": percent
    })

df = pd.DataFrame(rows)

print("\n====== PORTFOLIO SUMMARY ======")
print(df.to_string(index=False))
print("\nTotal Value:  $", round(df["Value"].sum(), 2))
print("Total Cost:   $", round(df["Cost"].sum(), 2))
print("Total Profit: $", round(df["Profit"].sum(), 2))
print("Best Performer:", df.loc[df["Return %"].idxmax(), "Company"])
print("Worst Performer:", df.loc[df["Return %"].idxmin(), "Company"])
print("Average Return:", round(df["Return %"].mean(), 2), "%")

df.to_excel("portfolio.xlsx", index=False)
print("\nSaved portfolio.xlsx")

plt.figure(figsize=(8, 6))
plt.pie(df["Value"], labels=df["Ticker"], autopct="%1.1f%%")
plt.title("Portfolio Allocation by Value")
plt.savefig("allocation.png")
plt.close()
print("Saved allocation.png")

# ==============================
# STEP 5 - RETURNS BAR CHART
# ==============================
plt.figure(figsize=(8, 6))
plt.bar(df["Ticker"], df["Return %"])
plt.title("Return % by Stock")
plt.xlabel("Stock")
plt.ylabel("Return %")
plt.savefig("returns.png")
plt.close()
print("Saved returns.png")

# ==============================
# STEP 6 - HISTORICAL CHARTS
# ==============================
print("Generating historical charts...")

for ticker, shares, buy_price in portfolio:
    stock = yf.Ticker(ticker)
    history = stock.history(period="1y")

    plt.figure(figsize=(12, 6))
    plt.plot(history.index, history["Close"])
    plt.title(ticker + " - 12 Month Price History")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.savefig(ticker + "_history.png")
    plt.close()
    print("Saved", ticker + "_history.png")

print("\nDone. All files saved to your folder.")