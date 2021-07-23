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

			...

USAGE EXAMPLE:

1 - Comand to plot a graph:
python3 pytrade.py plot --company 'high' --file 'example_other.csv' --start '2020-02-11' --end '2020-03-13' --mav 9 --figure zuza

2 - Comand to get data of a range of dates
python3 pytrade.py  get --start '2020-02-11' --end '2020-02-20'

TODO LIST

- maybe more functions using talib
- imprive argparser

