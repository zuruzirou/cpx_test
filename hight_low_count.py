import yfinance as yf
from datetime import datetime, timedelta

technology_stocks = ['AAPL','ACN','ADBE','ADI','ADP','ADSK','AKAM','AMAT','AMD','ANET','APH','AVGO','BR','CDNS','CERN','CHKP','CSCO','CTSH','CTXS','DELL','DXC','EA','EBAY','FB','FFIV','FISV','FLT','FTNT','GLW','GOOG','GOOGL','GRMN','HPE','HPQ','IBM','INTC','INTU','IPGP','ITW','JKHY','JNPR','KEYS','KLAC','LRCX','MA','MCHP','MSFT','MU','MXIM','NFLX','NTAP','NVDA','ORCL','PAYC','PAYX','PYPL','QCOM','QRVO','SNPS','SWKS','TEL','TMO']
healthcare_stocks = ['ABT','ABBV','ABMD','ALGN','ALXN','ALNY','AMGN','ANTM','BAX','BDX','BIIB','BSX','BMY','CAH','CNC','CERN','CI','COO','CVS','DHR','DXCM','DVA','EW','GILD','HCA','HSIC','HOLX','IDXX','ILMN','INCY','ISRG','JNJ']
financial_stocks = ['BRK.B','JPM','BAC','C','WFC','GS','MS','USB','AXP','COF','DFS','SYF','SIVB','PNC','FITB','MTB','KEY','HBAN','CFG','ZION','RF','FRC','CMA','STT','BKU','PBCT','SBNY','FHN','BPOP','PACW','CBSH']

def get_new_high_and_low_stocks(stocks, start_date, end_date):
    new_high_stocks = []
    new_low_stocks = []
    
    for stock in stocks:
        stock_data = yf.download(stock, start=start_date, end=end_date)
        
        if len(stock_data) > 0:
            stock_high = stock_data['High'].max()
            stock_low = stock_data['Low'].min()
            stock_last = stock_data.iloc[-1]['Close']
            
            if stock_last >= stock_high:
                new_high_stocks.append(stock)
            elif stock_last <= stock_low:
                new_low_stocks.append(stock)
    
    return new_high_stocks, new_low_stocks

def detect_buy_alert(technology_stocks, healthcare_stocks, financial_stocks):
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')
    
    technology_new_high, technology_new_low = get_new_high_and_low_stocks(technology_stocks, start_date, end_date)
    healthcare_new_high, healthcare_new_low = get_new_high_and_low_stocks(healthcare_stocks, start_date, end_date)
    financial_new_high, financial_new_low = get_new_high_and_low_stocks(financial_stocks, start_date, end_date)
    
    technology_new_high_count = len(technology_new_high)
    technology_new_low_count = len(technology_new_low)
    healthcare_new_high_count = len(healthcare_new_high)
    healthcare_new_low_count = len(healthcare_new_low)
    financial_new_high_count = len(financial_new_high)
    financial_new_low_count = len(financial_new_low)

    technology_ratio = technology_new_high_count / technology_new_low_count if technology_new_low_count > 0 else technology_new_high_count
    healthcare_ratio = healthcare_new_high_count / healthcare_new_low_count if healthcare_new_low_count > 0 else healthcare_new_high_count
    financial_ratio = financial_new_high_count / financial_new_low_count if financial_new_low_count > 0 else financial_new_high_count

    if technology_new_high_count >= 10 and technology_ratio >= 2:
        print('Technology sector - Buy Alert')
    if healthcare_new_high_count >= 10 and healthcare_ratio >= 2:
        print('Healthcare sector - Buy Alert')
    if financial_new_high_count >= 10 and financial_ratio >= 2:
        print('Financial sector - Buy Alert')
    detect_buy_alert(technology_stocks, healthcare_stocks, financial_stocks)
