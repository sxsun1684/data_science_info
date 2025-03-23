import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

end = pd.Timestamp.today()
start = end - pd.DateOffset(years=1)

stocks = yf.download(['INTC', 'WMT'], start=start, end=end)[['Close']]
stocks = stocks.dropna()

price_intc = stocks['Close']['INTC']
price_wmt = stocks['Close']['WMT']

def rolling_corr(x, y, window=30, lag=0):
    return x.shift(lag).rolling(window).corr(y)

corr_0 = rolling_corr(price_intc, price_wmt, lag=0)
corr_intc_lag1 = rolling_corr(price_intc, price_wmt, lag=1)
corr_wmt_lag1 = rolling_corr(price_wmt, price_intc, lag=1)

correlations = pd.DataFrame({
    'INTC vs WMT (Lag 0)': corr_0,
    'INTC(t-1) vs WMT(t)': corr_intc_lag1,
    'WMT(t-1) vs INTC(t)': corr_wmt_lag1
})


plt.figure(figsize=(14, 7))
for label in correlations.columns:
    plt.plot(correlations.index.to_numpy(), correlations[label].to_numpy(), label=label)

plt.title('30-Day Moving Cross-Correlation: INTC & WMT')
plt.xlabel('Date')
plt.ylabel('Correlation Coefficient')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

"""No strong cross-correlation exists between INTC and WMT, as they operate in unrelated sectors. 
Lagged relationships are weak, indicating limited predictive power. 
However, the low correlation supports their use in a diversified portfolio to reduce risk.
"""