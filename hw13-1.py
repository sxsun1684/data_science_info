import pandas as pd
import matplotlib.pyplot as plt


file_path = 'INTC.csv'
df = pd.read_csv(file_path)


df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
df = df.dropna(subset=['Date', 'Close'])  # Drop rows with invalid data
df = df.sort_values('Date')

# Calculate 20-day SMA and EMA
df['SMA_20'] = df['Close'].rolling(window=20).mean()
df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()


plt.figure(figsize=(14, 7))
plt.plot(df['Date'].values, df['Close'].values, label='Closing Price', color='blue')
plt.plot(df['Date'].values, df['SMA_20'].values, label='20-Day SMA', color='red')
plt.plot(df['Date'].values, df['EMA_20'].values, label='20-Day EMA', color='green')
plt.title('INTC - 20-Day SMA and EMA')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

"""
Rising quarterly trend → INTC's average price is increasing, indicating positive performance.
Falling trend → Suggests weakening investor sentiment or company fundamentals.
Volatility → Daily price swings around the quarterly average show market uncertainty.
Trend reversals → Signal possible turning points in stock performance.
"""