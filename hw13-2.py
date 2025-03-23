import pandas as pd
import matplotlib.pyplot as plt


file_path = 'INTC.csv'
df = pd.read_csv(file_path)


df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
df = df.dropna(subset=['Date', 'Close']).sort_values('Date')
df.set_index('Date', inplace=True)

# Resample to quarterly average
quarterly_trend = df['Close'].resample('QE-DEC').mean()


plt.figure(figsize=(14, 7))
plt.plot(df.index.to_numpy(), df['Close'].to_numpy(), label='Daily Closing Price', color='blue')
plt.plot(quarterly_trend.index.to_numpy(), quarterly_trend.to_numpy(), label='Quarterly Average Trend', color='red', linestyle='--', marker='o')
plt.title('INTC Daily Closing Price with Quarterly Trend')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

"""
Intel’s quarterly average price has been gradually increasing over the last few quarters, suggesting sustained investor 
confidence. Despite some short-term volatility, the overall trend indicates recovery or growth—possibly due to positive 
earnings or strong demand in its core semiconductor market.
"""