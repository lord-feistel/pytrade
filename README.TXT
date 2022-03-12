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
  
 

MOTIVATION

Pytrade is a script in python that was implemented to deliver a better plot tool 
for candles than Gnuplot. this program can be called a from C++ program's  pipe


INSTALLATION


1 - Clone the repo

git clone https://github.com/lord-feistel/pytrade.git

2 - install pip in case you don't have

sudo apt-get install python3-pip

3 - install some packages using pip

pip3 install pandas
pip3 install matplotlib
pip install --upgrade mplfinance
pip3 install yfinance

in case the last command failed, please check how to install
it with conda on the next section



4 - install conda ( needed for yfinance in case not possible with pip install)

In my case, I am using the script version
Anaconda3-2019.10-Linux-x86_64.sh, please check for the newest


5 - install yfinance using conda

wget  https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
chmod +x Anaconda3-2019.10-Linux-x86_64.sh

I chose the /opt/conda folder, please don't forget to change permissions

./Anaconda3-2019.10-Linux-x86_64.sh

don't forget to add to your environment (preferable to .bashrc)

export PATH=$PATH:/opt/conda/bin/

conda install yfinance


HOW TO USE

1 - PREPARATION

1.1 - Create a folder called data in order to download all information

mkdir data

1.2 - Create a file "companies.txt" with the ticks of companies that you intend to get data
e.g

$ cat companies.txt 
GOOGL
AMZN




2 - Comand to get data of a range of dates
python3 pytrade.py  get --start '2020-02-11' --end '2022-02-13'



3 - Comand to plot a graph:

python3 pytrade.py plot --company 'AMZN' --file './data/AMZN' --start '2020-02-11' --end '2022-02-13' --mav 9 --figure amazon	

On this an EMA 9 will be provided together, please check the software help fpr further options

the amazon.png can be found as a result.



4 - other funtionalities.

Also, it's possible to put on graph buy and sell points using the diles buy.data and sell.data
please check the software help for further questions.

Any question send a mailt to :


jr.overhead@gmail.com














