import yfinance as yf
import mplfinance as mpf


def DownloadDay(ticker):

	tickers = yf.Tickers(ticker)

	intraday = yf.download(  # or pdr.get_data_yahoo(...
        	# tickers list or string as well
        	tickers = "SPY",
        	period = "1d",
        	interval = "5m",
        	group_by = 'ticker',
        	auto_adjust = True,
        	prepost = True,
        	threads = True,
        	proxy = None
    	)
    
    
	intraday.reset_index()
	fname = "SPY.data" 
	intraday.to_csv(fname)

	

Download('SPY')



