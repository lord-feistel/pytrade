
Tool created to automatize download and graph plot on trading market

Dependencies:

pandas, mplfinance, sys, yfinance, numpy, math, datetime, glob, argparse


Date,Open,High,Low,Close,Adj Close,Volume

2020-02-11,49.389999,49.709999,48.860001,49.130001,47.461937,23168300



USAGE EXAMPLE:

1 - Comand to plot a graph

python3 pytrade.py plot --company 'high' --file 'example_other.csv' --start '2020-02-11' --end '2020-03-13' --mav 9 --figure zuza

2 - Comand to get data of a range of dates

python3 pytrade.py  get --start '2020-02-11' --end '2020-02-20'

TODO LIST

- maybe more functions using talib
- improve argparser

