import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# 銘柄コードとデータ取得期間を指定
ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2023-01-01'

# Yahoo Financeから株価データを取得
df = yf.download(ticker, start=start_date, end=end_date)

# 移動平均線を計算 (短期: 25日、長期: 50日)
df['SMA25'] = df['Adj Close'].rolling(window=25).mean()
df['SMA50'] = df['Adj Close'].rolling(window=50).mean()

# グラフ描画
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Adj Close'], label=f'{ticker} Adjusted Close')
plt.plot(df.index, df['SMA25'], label='25-day Simple Moving Average', linestyle='--')
plt.plot(df.index, df['SMA50'], label='50-day Simple Moving Average', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title(f'{ticker} Stock Price and Moving Averages')
plt.legend()
plt.show()

#save
#plt.savefig(f'{ticker}_stock_price_and_moving_averages.png', dpi=300)
