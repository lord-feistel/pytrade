# Script made in order to provide to C++ libraries often used at financial area
# with scalability and with. Possible in the future it will be embedded
# in the C++ code using boost

'''

Copyright (c) 2022 
  
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
 
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>. 
  
  
Author : Antonio ( Lord Feistel )

repo : https://github.com/lord-feistel/pytrade

'''

import pandas as pd
import mplfinance as mpf
import sys
import yfinance as yf
import numpy as np
import math
import datetime
import glob
import argparse
#import talib as ta



banner = '''
                      __                               __
                      /  |                             /  |
  ______   __    __  _$$ |_     ______   ______    ____$$ |  ______
 /      \ /  |  /  |/ $$   |   /      \ /      \  /    $$ | /      \
/$$$$$$  |$$ |  $$ |$$$$$$/   /$$$$$$  |$$$$$$  |/$$$$$$$ |/$$$$$$  |
$$ |  $$ |$$ |  $$ |  $$ | __ $$ |  $$/ /    $$ |$$ |  $$ |$$    $$ |
$$ |__$$ |$$ \__$$ |  $$ |/  |$$ |     /$$$$$$$ |$$ \__$$ |$$$$$$$$/
$$    $$/ $$    $$ |  $$  $$/ $$ |     $$    $$ |$$    $$ |$$       |
$$$$$$$/   $$$$$$$ |   $$$$/  $$/       $$$$$$$/  $$$$$$$/  $$$$$$$/
$$ |      /  \__$$ |
$$ |      $$    $$/
$$/        $$$$$$/
'''


'''
Function made to be called from C++ in order to replace gnuplot
what showed a problem in graphs with windows

USAGE:

plot_candle(glabel, begin, final, extra_line)

glabel      -> name of graph usually a company
begin       -> start date on the format YYYY-MM-DD e.g. 2020-02-10
final       -> end  date on the format YYYY-MM-DD e.g. 2020-02-10
file        -> file in the format : C:\\DIR\\DIR\\FILE for windows OR   /DIR/DIR/DIR/FILE for linux
extra_aline -> format extra_line=[("2020-02-10" ,80.900002),("2020-04-15" ,80.900002)]
extra_vline -> format extra_line=["2020-02-10" ,"2020-04-15] -> use date
extra_hline -> format extra_line=["80" ,"90] -> use price
averages    -> take move averages in the format [20,30]
figure      -> True prinf False not

The file need to be in the format:

Date,Open,High,Low,Close,Adj Close,Volume
2020-02-11,49.389999,49.709999,48.860001,49.130001,47.461937,23168300

'''

def PlotGraph(glabel, begin , final, file, extra_aline,extra_vline,extra_hline,averages, figure):

    #read direct from Excell
    df = pd.read_csv(file, index_col=0, parse_dates=True)
    range = pd.date_range(start=begin, end=final)
    df = df[df.index.isin(range)]
    df.head()

    #take the signals to the graph
    buy, sell = AddSignals(df, "buy.dat", "sell.dat")

    #add markers which will be used after on the graph

    plots =[]

    if len(buy) > 0:
        up_plot = mpf.make_addplot(buy, type='scatter', marker='^', markersize=20, panel=0, color='green')
        plots.append(up_plot)

    if len(sell) > 0:
        down_plot = mpf.make_addplot(sell, type='scatter', marker='v', markersize=20, color='red',panel=0)
        plots.append(down_plot)


    #plots = [up_plot, down_plot] # markers vectors
    #plots = [up_plot, down_plot] # markers vectors

    #define colors of lines ,set_yscale
    s  = mpf.make_mpf_style(base_mpf_style='charles',mavcolors=['#1f77b4','#ff7f0e','#2ca02c'])


    if figure == None:
        nice = False
    else:
        nice = True

    #todo - fix problem with ax return
    try :
        fig, ax = mpf.plot(df, type='candle', #add candles

        style = s ,                          #style defined before
        title=glabel,                        #label of graph
        ylabel='Price',                      #label of Y
        alines=dict(alines=extra_aline, linewidths=(0.5,1)), #arbitrary line
        vlines=dict(vlines=extra_vline, linewidths=(0.5,1)), #arbitrary line
        hlines=dict(hlines=extra_hline, linewidths=(0.5,1)), #arbitrary line
        addplot=plots , # marks
        mav=(averages) , # move average
        volume=True, # turn on or not volume
        returnfig=nice) #save in a figure

    except IndexError :
        print("please enter a valid Date range !")
        sys.exit()
    except ValueError:
        print("please fix me ! : ValueError")
        sys.exit()
    except TypeError:
        print("please fix me ! : TypeError")
        sys.exit()


    if nice:
        fig.savefig(figure, dpi=1000)

'''
Simple function to convert a list of string
in a list of integer
'''

def LstringToLint(sl):
        il = []
        for i in sl:
            il.append(int(i))

        return il

'''
Simple function to convert a date with '-'
separator to a list of integers e.g:
2020-02-13 to [2020, 2, 13]

'''

def DateToIntList( s ):
    result = []
    ts = s.split('-')
    ti = LstringToLint(ts)
    return ti

'''
Function used to Download Data from Yahoo finance.
We did prefer it instead download with WGET beacuse this
library is often maintened and prevent future changes
that would be necessary in case we do our own  routine
USAGE:
start -> start date ( mandatory)
start -> end date ( not mandatory)

OUTPUT: save to data.dat
'''
def GetData(start, end):

    companies = ReadFile("companies.txt")

    syear, smonth, sday = DateToIntList( start )
    eyear, emonth, eday = DateToIntList( end )

    start = datetime.date(syear, smonth, sday)

    if end == None:
        end = datetime.date.today()
    else:
        datetime.date(eyear, emonth, eday)


    StrCompanies = ""

    # downlad can be done all at once
    #in order to avoid been blocked on the site
    #doing several calls
    # needed to be submited on the format "TICKER TICKER TICKER"

    print(companies)
    for c in companies:
            #StrCompanies = StrCompanies + ' '+ c
            if c != "":
                #data = yf.download(StrCompanies ,start, end, group_by="ticker")
                print(c)
                data = yf.download(c ,start, end, group_by="ticker")
                #data.reset_index(inplace=True)
                data.reset_index()
                fname = "./data/" + c
                data.to_csv(fname)

    return

'''
This function recive a DataFrame and two files containing dates to buy
and dates to cell in the format :

2020-03-09
2020-03-10
2020-03-11

this files by convention are : buy.dat and sell.data
USAGE:
data        -> Pandas DataFrame
FileBuy     -> dat file with Buy information
FileSell     -> dat file with Sell information

Todo - For now the name of files are hardcoded
'''

def AddSignals(data, FileBuy, FileSell):

    flgB = False
    flgS = False
    #list of buy entries
    buy=[]
    BuySet = ReadFile("buy.dat")

    #list of buy entries
    sell=[]
    SellSet = ReadFile("sell.dat")

    #it will check if it's on the buy file
    # or in the sell file
    for index, row in data.iterrows():

        #convert index to string
        tmp = str(index).split(' ')[0]

        # All fields needed to be filled
        # so if haven't some mark
        # need with a number

        if tmp in BuySet:
            #adding 3 to dont be attached to candle
            buy.append(row['Low'] - 1)
            sell.append(np.nan)
            flgB = True

        elif tmp in SellSet:
            sell.append(row['High'] + 1)
            buy.append(np.nan)
            flgS = True

        else:
            buy.append(np.nan)
            sell.append(np.nan)

        #avoiding
    if flgB == False:
        buy = []

    if flgS == False:
        sell = []

    return buy, sell

'''
Simple function to write file
USAGE:
Filename -> name of files
text     -> string be writen
RETURN:
    two lists to bse used on the plot
'''
def WriteFile(FileName, text):

    with open(FileName, 'w') as w:
            w.write(text)


'''
Simple function to read file
USAGE:
Filename -> name of files
RETURN:
a set with all read parsed by line feed
'''
def ReadFile(FileName):

    tmp = set()
    with open(FileName, 'r') as reader:

         line = " "
         while line !='':
            line = reader.readline().replace('\n','')
            tmp.add(line)
    return tmp



def main():


    #parsing

    #get parameters from comand line
    params = argparse.ArgumentParser(description=
    '''
    pytrade - Trade helper tool

    ''',

    usage='''python3 pytrade.py command parameters

             Examples:

             To plot:
             python3 pytrade.py plot --company \'high\' --file \'example_other.csv\' --start \'2020-02-11\' --end \'2020-03-13\' --mav 9 --figure zuza

             To get data:
             python3 pytrade.py  get --start \'2020-02-11\' --end \'2020-02-20\'
             ''')

    params.add_argument('command', metavar='command', type=str,
    help='command:\n\tplot\n\tget')

    params.add_argument('--company', metavar='company', type=str,
    help='the ticker of company')

    params.add_argument('--file', metavar='file', type=str,
    help='File to read data')

    params.add_argument('--start', metavar='start', type=str,
    help='start date in format yyyy-mm-dd')

    params.add_argument('--end', metavar='end', type=str,
    help='end date in format yyyy-mm-dd', default=None)

    params.add_argument('--mav', metavar='mav', type=str,
    help='move averages separeted by coma')

    params.add_argument('--figure', metavar='figure', type=str,
    help='plot difure F or V',  default=None, required=False)


    #Todo - expand also for hlines,vlines, and other parameters

    # Execute the parse_args() method
    args = params.parse_args()


    if args.command == 'plot':
        # extracting move averages
        Sma = args.mav.replace(']','').replace('[]','').split(',')
        Ima = LstringToLint(Sma)

        PlotGraph(args.company,  args.start , args.end, args.file, [], [], [], Ima ,args.figure )
    elif args.command == 'get':
        end = args.end
        start = args.start
        GetData(start,end)
    else:
        print('comand not found')


if __name__ == "__main__":
    main()
