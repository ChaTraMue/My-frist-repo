import yfinance as yf
import matplotlib.pyplot as plt

def plot_history(ticker, period="1y"):
    stock = yf.Ticker(ticker)
    history = stock.history(period=period)

    plt.figure(figsize=(12, 6))
    plt.plot(history.index, history["Close"])
    plt.title(ticker + " - 12 Month Price History")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.savefig(ticker + "_history.png")
    plt.close()
    print("Saved", ticker + "_history.png")

plot_history("NVDA")
plot_history("AMD")
plot_history("ASML")