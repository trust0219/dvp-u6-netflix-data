{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction\n",
    "\n",
    "In this project, you will act as a data visualization developer at Yahoo Finance! You will be helping the \"Netflix Stock Profile\" team visualize the Netflix stock data. In finance, a _stock profile_ is a series of studies, visualizations, and analyses that dive into different aspects a publicly traded company's data. \n",
    "\n",
    "For the purposes of the project, you will only visualize data for the year of 2017. Specifically, you will be in charge of creating the following visualizations:\n",
    "+ The distribution of the stock prices for the past year\n",
    "+ Netflix's earnings and revenue in the last four quarters\n",
    "+ The actual vs. estimated earnings per share for the four quarters in 2017\n",
    "+ A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017 \n",
    "\n",
    "Note: We are using the Dow Jones Industrial Average to compare the Netflix stock to the larter stock market. Learn more about why the Dow Jones Industrial Average is a general reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).\n",
    "\n",
    "During this project, you will analyze, prepare, and plot data. Your visualizations will help the financial analysts asses the risk of the Netflix stock.\n",
    "\n",
    "After you complete your visualizations, you'll be creating a presentation to share the images with the rest of the Netflix Stock Profile team. Your slides should include:\n",
    "\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n",
    "\n",
    "Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1\n",
    "\n",
    "Let's get our notebook ready for visualizing! Import the modules that you'll be using in this project:\n",
    "- `from matplotlib import pyplot as plt`\n",
    "- `import pandas as pd`\n",
    "- `import seaborn as sns`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "import pandas as pd\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's load the datasets and inspect them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX.csv** into a DataFrame called `netflix_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Hint: Use the `pd.read_csv()`function).\n",
    "\n",
    "Note: In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted for both dividends and splits. This means this is the true closing stock price for a given business day."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Date        Open        High         Low       Close   Adj Close  \\\n",
      "0   2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
      "1   2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
      "2   2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
      "3   2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
      "4   2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
      "5   2017-06-01  163.520004  166.869995  147.300003  149.410004  149.410004   \n",
      "6   2017-07-01  149.800003  191.500000  144.250000  181.660004  181.660004   \n",
      "7   2017-08-01  182.490005  184.619995  164.229996  174.710007  174.710007   \n",
      "8   2017-09-01  175.550003  189.949997  172.440002  181.350006  181.350006   \n",
      "9   2017-10-01  182.110001  204.380005  176.580002  196.429993  196.429993   \n",
      "10  2017-11-01  197.240005  202.479996  184.320007  195.509995  195.509995   \n",
      "11  2017-12-01  186.990005  194.490005  178.380005  191.960007  191.960007   \n",
      "\n",
      "       Volume  \n",
      "0   181772200  \n",
      "1    91432000  \n",
      "2   110692700  \n",
      "3   149769200  \n",
      "4   116795800  \n",
      "5   135675800  \n",
      "6   185144700  \n",
      "7   136523100  \n",
      "8   111427900  \n",
      "9   208657800  \n",
      "10  161719700  \n",
      "11  115103700  \n"
     ]
    }
   ],
   "source": [
    "netflix_stocks = pd.read_csv(\"NFLX.csv\")\n",
    "print(netflix_stocks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **DJI.csv** into a DataFrame called `dowjones_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Note: You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Date          Open          High           Low         Close  \\\n",
      "0   2017-01-01  19872.859375  20125.580078  19677.939453  19864.089844   \n",
      "1   2017-02-01  19923.810547  20851.330078  19831.089844  20812.240234   \n",
      "2   2017-03-01  20957.289063  21169.109375  20412.800781  20663.220703   \n",
      "3   2017-04-01  20665.169922  21070.900391  20379.550781  20940.509766   \n",
      "4   2017-05-01  20962.730469  21112.320313  20553.449219  21008.650391   \n",
      "5   2017-06-01  21030.550781  21535.029297  20994.220703  21349.630859   \n",
      "6   2017-07-01  21392.300781  21929.800781  21279.300781  21891.119141   \n",
      "7   2017-08-01  21961.419922  22179.109375  21600.339844  21948.099609   \n",
      "8   2017-09-01  21981.769531  22419.509766  21709.630859  22405.089844   \n",
      "9   2017-10-01  22423.470703  23485.250000  22416.000000  23377.240234   \n",
      "10  2017-11-01  23442.900391  24327.820313  23242.750000  24272.349609   \n",
      "11  2017-12-01  24305.400391  24876.070313  23921.900391  24719.220703   \n",
      "\n",
      "       Adj Close      Volume  \n",
      "0   19864.089844  6482450000  \n",
      "1   20812.240234  6185580000  \n",
      "2   20663.220703  6941970000  \n",
      "3   20940.509766  5392630000  \n",
      "4   21008.650391  6613570000  \n",
      "5   21349.630859  7214590000  \n",
      "6   21891.119141  5569720000  \n",
      "7   21948.099609  6150060000  \n",
      "8   22405.089844  6342130000  \n",
      "9   23377.240234  7302910000  \n",
      "10  24272.349609  7335640000  \n",
      "11  24719.220703  6589890000  \n"
     ]
    }
   ],
   "source": [
    "dowjones_stocks = pd.read_csv(\"DJI.csv\")\n",
    "print(dowjones_stocks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX_daily_by_quarter.csv** into a DataFrame called `netflix_stocks_quarterly`. Then, quickly inspect the DataFrame using `print()`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "           Date        Open        High         Low       Close   Adj Close  \\\n",
      "0    2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
      "1    2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
      "2    2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
      "3    2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
      "4    2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
      "5    2017-01-10  131.270004  132.220001  129.289993  129.889999  129.889999   \n",
      "6    2017-01-11  130.910004  131.500000  129.250000  130.500000  130.500000   \n",
      "7    2017-01-12  130.630005  130.850006  128.500000  129.179993  129.179993   \n",
      "8    2017-01-13  131.149994  133.929993  130.580002  133.699997  133.699997   \n",
      "9    2017-01-17  135.039993  135.399994  132.089996  132.889999  132.889999   \n",
      "10   2017-01-18  133.210007  133.649994  131.059998  133.259995  133.259995   \n",
      "11   2017-01-19  142.009995  143.460007  138.250000  138.410004  138.410004   \n",
      "12   2017-01-20  139.360001  140.789993  137.660004  138.600006  138.600006   \n",
      "13   2017-01-23  138.649994  139.490005  137.309998  137.389999  137.389999   \n",
      "14   2017-01-24  138.110001  140.929993  137.029999  140.110001  140.110001   \n",
      "15   2017-01-25  140.800003  141.389999  139.050003  139.520004  139.520004   \n",
      "16   2017-01-26  140.449997  141.210007  138.509995  138.960007  138.960007   \n",
      "17   2017-01-27  139.460007  142.490005  139.000000  142.449997  142.449997   \n",
      "18   2017-01-30  141.770004  141.970001  138.800003  141.220001  141.220001   \n",
      "19   2017-01-31  140.550003  141.830002  139.699997  140.710007  140.710007   \n",
      "20   2017-02-01  141.199997  142.410004  139.300003  140.779999  140.779999   \n",
      "21   2017-02-02  140.610001  141.039993  139.050003  139.199997  139.199997   \n",
      "22   2017-02-03  139.509995  140.639999  139.100006  140.250000  140.250000   \n",
      "23   2017-02-06  140.000000  141.000000  139.160004  140.970001  140.970001   \n",
      "24   2017-02-07  141.490005  144.279999  141.050003  144.000000  144.000000   \n",
      "25   2017-02-08  143.570007  145.070007  142.559998  144.740005  144.740005   \n",
      "26   2017-02-09  144.979996  145.089996  143.580002  144.139999  144.139999   \n",
      "27   2017-02-10  144.679993  145.300003  143.970001  144.820007  144.820007   \n",
      "28   2017-02-13  145.190002  145.949997  143.050003  143.199997  143.199997   \n",
      "29   2017-02-14  143.199997  144.110001  140.050003  140.820007  140.820007   \n",
      "..          ...         ...         ...         ...         ...         ...   \n",
      "221  2017-11-16  194.330002  197.699997  193.750000  195.509995  195.509995   \n",
      "222  2017-11-17  195.740005  195.949997  192.649994  193.199997  193.199997   \n",
      "223  2017-11-20  193.300003  194.320007  191.899994  194.100006  194.100006   \n",
      "224  2017-11-21  195.039993  197.520004  194.970001  196.229996  196.229996   \n",
      "225  2017-11-22  196.580002  196.750000  193.630005  196.320007  196.320007   \n",
      "226  2017-11-24  196.649994  196.899994  195.330002  195.750000  195.750000   \n",
      "227  2017-11-27  195.559998  195.850006  194.000000  195.050003  195.050003   \n",
      "228  2017-11-28  195.339996  199.679993  194.009995  199.179993  199.179993   \n",
      "229  2017-11-29  198.910004  199.029999  184.320007  188.149994  188.149994   \n",
      "230  2017-11-30  190.309998  190.860001  186.679993  187.580002  187.580002   \n",
      "231  2017-12-01  186.990005  189.800003  185.000000  186.820007  186.820007   \n",
      "232  2017-12-04  189.360001  189.720001  178.380005  184.039993  184.039993   \n",
      "233  2017-12-05  183.500000  188.139999  181.190002  184.210007  184.210007   \n",
      "234  2017-12-06  183.380005  186.479996  182.880005  185.300003  185.300003   \n",
      "235  2017-12-07  185.710007  187.339996  183.220001  185.199997  185.199997   \n",
      "236  2017-12-08  186.500000  189.419998  186.300003  188.539993  188.539993   \n",
      "237  2017-12-11  187.850006  189.419998  185.910004  186.220001  186.220001   \n",
      "238  2017-12-12  186.009995  187.850006  184.820007  185.729996  185.729996   \n",
      "239  2017-12-13  186.100006  188.690002  185.410004  187.860001  187.860001   \n",
      "240  2017-12-14  187.979996  192.639999  187.199997  189.559998  189.559998   \n",
      "241  2017-12-15  189.610001  191.429993  188.009995  190.119995  190.119995   \n",
      "242  2017-12-18  191.199997  191.649994  188.899994  190.419998  190.419998   \n",
      "243  2017-12-19  190.179993  190.300003  185.750000  187.020004  187.020004   \n",
      "244  2017-12-20  187.940002  189.110001  185.259995  188.820007  188.820007   \n",
      "245  2017-12-21  189.440002  190.949997  187.580002  188.619995  188.619995   \n",
      "246  2017-12-22  188.330002  190.949997  186.800003  189.940002  189.940002   \n",
      "247  2017-12-26  189.779999  189.940002  186.399994  187.759995  187.759995   \n",
      "248  2017-12-27  187.800003  188.100006  185.220001  186.240005  186.240005   \n",
      "249  2017-12-28  187.179993  194.490005  186.850006  192.710007  192.710007   \n",
      "250  2017-12-29  192.509995  193.949997  191.220001  191.960007  191.960007   \n",
      "\n",
      "       Volume Quarter  \n",
      "0     9437900      Q1  \n",
      "1     7843600      Q1  \n",
      "2    10185500      Q1  \n",
      "3    10657900      Q1  \n",
      "4     5766900      Q1  \n",
      "5     5985800      Q1  \n",
      "6     5615100      Q1  \n",
      "7     5388900      Q1  \n",
      "8    10515000      Q1  \n",
      "9    12183200      Q1  \n",
      "10   16168600      Q1  \n",
      "11   23203400      Q1  \n",
      "12    9497400      Q1  \n",
      "13    7433900      Q1  \n",
      "14    7754700      Q1  \n",
      "15    7238100      Q1  \n",
      "16    6038300      Q1  \n",
      "17    8323900      Q1  \n",
      "18    8122500      Q1  \n",
      "19    4411600      Q1  \n",
      "20    6033400      Q1  \n",
      "21    3462400      Q1  \n",
      "22    3512600      Q1  \n",
      "23    3552100      Q1  \n",
      "24    8573500      Q1  \n",
      "25    6887100      Q1  \n",
      "26    4555100      Q1  \n",
      "27    6171900      Q1  \n",
      "28    4790400      Q1  \n",
      "29    8355000      Q1  \n",
      "..        ...     ...  \n",
      "221   5678400      Q4  \n",
      "222   3906300      Q4  \n",
      "223   3827500      Q4  \n",
      "224   4787300      Q4  \n",
      "225   5895400      Q4  \n",
      "226   2160500      Q4  \n",
      "227   3210100      Q4  \n",
      "228   6981100      Q4  \n",
      "229  14202700      Q4  \n",
      "230   6630100      Q4  \n",
      "231   6219500      Q4  \n",
      "232   9069800      Q4  \n",
      "233   5783700      Q4  \n",
      "234   5490100      Q4  \n",
      "235   4659500      Q4  \n",
      "236   4987300      Q4  \n",
      "237   5298600      Q4  \n",
      "238   4265900      Q4  \n",
      "239   4710000      Q4  \n",
      "240   7792800      Q4  \n",
      "241   7285600      Q4  \n",
      "242   5011000      Q4  \n",
      "243   7033000      Q4  \n",
      "244   6545400      Q4  \n",
      "245   4729800      Q4  \n",
      "246   3878900      Q4  \n",
      "247   3045700      Q4  \n",
      "248   4002100      Q4  \n",
      "249  10107400      Q4  \n",
      "250   5187600      Q4  \n",
      "\n",
      "[251 rows x 8 columns]\n"
     ]
    }
   ],
   "source": [
    "netflix_stocks_quarterly = pd.read_csv(\"NFLX_daily_by_quarter.csv\")\n",
    "print(netflix_stocks_quarterly)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's learn more about our data. The datasets are large and it may be easier to view the entire dataset locally on your computer. Open the CSV files directly from the folder you downloaded for this project.\n",
    " - `NFLX` is the stock ticker symbol for Netflix and `^DJI` is the stock ticker symbol for the Dow Jones industrial Average, which is why the CSV files are named accordingly\n",
    " - In the Yahoo Data, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    " - You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n",
    " \n",
    "Answer the following questions by inspecting the data in the **NFLX.csv**,**DJI.csv**, and **NFLX_daily_by_quarter.csv** in your computer."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What year is represented in the data? Look out for the latest and earliest date."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Year 2017\n",
    "# Earliest Date: 2017-01-01\n",
    "# Latest Date: 2017-12-29"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "+ Is the data represented by days, weeks, or months? \n",
    "+ In which ways are the files different? \n",
    "+ What's different about the columns for `netflix_stocks` versus `netflix_stocks_quarterly`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# netflix_stocks_quarterly has one extra column that indicates the quarter."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4\n",
    "\n",
    "Great! Now that we have spent sometime looking at the data, let's look at the column names of the DataFrame `netflix_stocks` using `.head()`. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Adj Close</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>143.460007</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>181772200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>141.199997</td>\n",
       "      <td>145.949997</td>\n",
       "      <td>139.050003</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>91432000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>142.839996</td>\n",
       "      <td>148.289993</td>\n",
       "      <td>138.259995</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>110692700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>146.699997</td>\n",
       "      <td>153.520004</td>\n",
       "      <td>138.660004</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>149769200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>151.910004</td>\n",
       "      <td>164.750000</td>\n",
       "      <td>151.610001</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>116795800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close   Adj Close  \\\n",
       "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
       "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
       "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
       "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
       "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
       "\n",
       "      Volume  \n",
       "0  181772200  \n",
       "1   91432000  \n",
       "2  110692700  \n",
       "3  149769200  \n",
       "4  116795800  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "netflix_stocks.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What do you notice? The first two column names are one word each, and the only one that is not is `Adj Close`! \n",
    "\n",
    "The term `Adj Close` is a confusing term if you don't read the Yahoo Documentation. In Yahoo, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    "\n",
    "This means this is the column with the true closing price, so these data are very important.\n",
    "\n",
    "Use Pandas to change the name of of the column to `Adj Close` to `Price` so that it is easier to work with the data. Remember to use `inplace=True`.\n",
    "\n",
    "Do this for the Dow Jones and Netflix Quarterly pandas dataframes as well.\n",
    "Hint: Use [`.rename()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "netflix_stocks.rename(columns={\"Adj Close\":\"Price\"},inplace=True)\n",
    "dowjones_stocks.rename(columns={\"Adj Close\":\"Price\"},inplace=True)\n",
    "netflix_stocks_quarterly.rename(columns={\"Adj Close\":\"Price\"},inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Run `netflix_stocks.head()` again to check your column name has changed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Price</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>143.460007</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>181772200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>141.199997</td>\n",
       "      <td>145.949997</td>\n",
       "      <td>139.050003</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>91432000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>142.839996</td>\n",
       "      <td>148.289993</td>\n",
       "      <td>138.259995</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>110692700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>146.699997</td>\n",
       "      <td>153.520004</td>\n",
       "      <td>138.660004</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>149769200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>151.910004</td>\n",
       "      <td>164.750000</td>\n",
       "      <td>151.610001</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>116795800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close       Price  \\\n",
       "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
       "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
       "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
       "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
       "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
       "\n",
       "      Volume  \n",
       "0  181772200  \n",
       "1   91432000  \n",
       "2  110692700  \n",
       "3  149769200  \n",
       "4  116795800  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "netflix_stocks.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Call `.head()` on the DataFrame `dowjones_stocks` and `netflix_stocks_quarterly`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Price</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Quarter</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-03</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>128.190002</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>9437900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-01-04</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>130.169998</td>\n",
       "      <td>126.550003</td>\n",
       "      <td>129.410004</td>\n",
       "      <td>129.410004</td>\n",
       "      <td>7843600</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-01-05</td>\n",
       "      <td>129.220001</td>\n",
       "      <td>132.750000</td>\n",
       "      <td>128.899994</td>\n",
       "      <td>131.809998</td>\n",
       "      <td>131.809998</td>\n",
       "      <td>10185500</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-01-06</td>\n",
       "      <td>132.080002</td>\n",
       "      <td>133.880005</td>\n",
       "      <td>129.809998</td>\n",
       "      <td>131.070007</td>\n",
       "      <td>131.070007</td>\n",
       "      <td>10657900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-01-09</td>\n",
       "      <td>131.479996</td>\n",
       "      <td>131.990005</td>\n",
       "      <td>129.889999</td>\n",
       "      <td>130.949997</td>\n",
       "      <td>130.949997</td>\n",
       "      <td>5766900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close       Price  \\\n",
       "0  2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
       "1  2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
       "2  2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
       "3  2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
       "4  2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
       "\n",
       "     Volume Quarter  \n",
       "0   9437900      Q1  \n",
       "1   7843600      Q1  \n",
       "2  10185500      Q1  \n",
       "3  10657900      Q1  \n",
       "4   5766900      Q1  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dowjones_stocks.head()\n",
    "netflix_stocks_quarterly.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5\n",
    "\n",
    "In this step, we will be visualizing the Netflix quarterly data! \n",
    "\n",
    "We want to get an understanding of the distribution of the Netflix quarterly stock prices for 2017. Specifically, we want to see in which quarter stock prices flucutated the most. We can accomplish this using a violin plot with four violins, one for each business quarter!\n",
    "\n",
    "\n",
    "1. Start by creating a variable `ax` and setting it equal to `sns.violinplot()`. This will instantiate a figure and give us access to the axes through the variable name `ax`.\n",
    "2. Use `sns.violinplot()` and pass in the following arguments:\n",
    "+ The `Quarter` column as the `x` values\n",
    "+ The `Price` column as your `y` values\n",
    "+ The `netflix_stocks_quarterly` dataframe as your `data`\n",
    "3. Improve the readability of the chart by adding a title of the plot. Add `\"Distribution of 2017 Netflix Stock Prices by Quarter\"` by using `ax.set_title()`\n",
    "4. Change your `ylabel` to \"Closing Stock Price\"\n",
    "5. Change your `xlabel` to \"Business Quarters in 2017\"\n",
    "6. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x10458a748>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = sns.violinplot(x=\"Quarter\",y=\"Price\",data=netflix_stocks_quarterly)\n",
    "ax.set_title(\"Distribution of 2017 Netflix Stock Prices by Quarter\")\n",
    "ax.set(xlabel=\"Business Quarters in 2017\",ylabel=\"Closing Stock Price\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "- What are your first impressions looking at the visualized data?\n",
    "\n",
    "- In what range(s) did most of the prices fall throughout the year?\n",
    "\n",
    "- What were the highest and lowest prices? "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### In 2017, stock price of Netflix has increased significantly in a year.\n",
    "#### In Q3, the approximate range of price was from \\\\$140 to \\$200, which is the largest change in price among the four quarters.\n",
    "#### Overall in 2017, the Netflix stock has reached to about \\\\$200 as highest, and $125 as lowest.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 6\n",
    "\n",
    "Next, we will chart the performance of the earnings per share (EPS) by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. We will accomplish this using a scatter chart. \n",
    "\n",
    "1. Plot the actual EPS by using `x_positions` and `earnings_actual` with the `plt.scatter()` function. Assign `red` as the color.\n",
    "2. Plot the actual EPS by using `x_positions` and `earnings_estimate` with the `plt.scatter()` function. Assign `blue` as the color\n",
    "\n",
    "3. Often, estimates and actual EPS are the same. To account for this, be sure to set your transparency  `alpha=0.5` to allow for visibility pf overlapping datapoint.\n",
    "4. Add a legend by using `plt.legend()` and passing in a list with two strings `[\"Actual\", \"Estimate\"]`\n",
    "\n",
    "5. Change the `x_ticks` label to reflect each quarter by using `plt.xticks(x_positions, chart_labels)`\n",
    "6. Assing \"`\"Earnings Per Share in Cents\"` as the title of your plot.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x116006208>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "x_positions = [1, 2, 3, 4]\n",
    "chart_labels = [\"1Q2017\",\"2Q2017\",\"3Q2017\",\"4Q2017\"]\n",
    "earnings_actual =[.4, .15,.29,.41]\n",
    "earnings_estimate = [.37,.15,.32,.41 ]\n",
    "plt.scatter(x_positions, earnings_actual,c=\"red\",alpha=0.5)\n",
    "plt.scatter(x_positions, earnings_estimate,c=\"blue\",alpha=0.5)\n",
    "plt.legend([\"Actual\",\"Estimate\"],loc=4)\n",
    "plt.xticks(x_positions, chart_labels)\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## Graph Literacy\n",
    "\n",
    "+ What do the purple dots tell us about the actual and estimate earnings per share in this graph? Hint: In color theory red and blue mix to make purple.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 7"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, we will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side. We have visualized a similar chart in the second Matplotlib lesson [Exercise 4](https://www.codecademy.com/courses/learn-matplotlib/lessons/matplotlib-ii/exercises/side-by-side-bars).\n",
    "\n",
    "As you may recall, plotting side-by-side bars in Matplotlib requires computing the width of each bar before hand. We have pasted the starter code for that exercise below. \n",
    "\n",
    "1. Fill in the `n`, `t`, `d`, `w` values for the revenue bars\n",
    "2. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `revenue_by_quarter` data\n",
    "3. Fill in the `n`, `t`, `d`, `w` values for the earnings bars\n",
    "4. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `earnings_by_quarter` data\n",
    "5. Create a legend for your bar chart with the `labels` provided\n",
    "6. Add a descriptive title for your chart with `plt.title()`\n",
    "7. Add labels to each quarter by assigning the position of the ticks through the code provided. Hint:  `plt.xticks(middle_x, quarter_labels)`\n",
    "8. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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7hHxInAfcHDR/BUR8Wqa/CWwZ3WqZ2ZmXVG2z11SPfB6RLwoaUvgAODCojKDI2JpmjwMmFuV2k3sX5XVvLW+VWWLtN3yt83xxx/PhAkTNnjTS5Ys4ayzzlrvy0lmZt2lkqtlBgPXSqojO9K/JSLukDQJaIyIacBZkg4DWoGVwPjuqnB3K7zlb2e1trbSq1fpJt1hhx0c7Ga20VRytcwsYPcS888rGD8XOLe6VetZJk2axO23386aNWv48Ic/zJVXXokkxo4dy+jRo3nooYc44YQTmD17Nttuuy2NjY0899xzXHTRRRxzzDEsXLiQQw89lDlz5nDNNdcwbdo0Vq9ezYIFCzjyyCO56KKLgOwOkBdeeCEDBgxgt912o0+fPlx66aX85je/4fzzz6euro7+/fuvu8OkmVkpvrdMkba7QrYNU6ZMAeDMM89k+vTpzJkzhzVr1nDHHXese8xrr71GY2MjZ599NgBLly7loYce4o477mi3S2fmzJlMmTKF2bNnM2XKFBYtWsSSJUv47ne/y8MPP8xf/vIXnnrqqXXlJ02axF133cXjjz/OtGnTurEFzCwPevS9ZWqhvW6Z++67j4suuojVq1ezcuVKRo4cyac//WmAdXeCbHPEEUewxRZbMGLECJ5//vmS29l///3p3z87pzBixAieffZZli9fzsc+9jEGDhwIZHebfPrppwHYb7/9GD9+PMcddxxHHXVU1fbXzPLJR+4VWLt2LV/60peYOnUqs2fP5tRTT13vlrxbb731euULb+nb3r17im/729ra2mEdrrjiCi644AIWLVrEnnvuyYoVK7qyK2a2mXC4V6AtyAcNGkRLS0u3nRjda6+9uP/++3nhhRdobW1d7xeaFixYwD777MOkSZOor69n0aJF3VIHM8uHnt0tU8Gli9XW1ufe5uCDD+b73/8+p556Krvuuivbb789e+21V7dse8iQIXzzm99k7733ZuDAgey8887rum7OOecc5s2bR0Sw//77s9tuu3VLHcwsH3zL3x6mpaWFfv360draypFHHsnnP/95jjzyyIoe6/aznsa3/K2+Sm/527OP3DdDEydO5I9//CNr167lwAMP5Igjjqh1lQyHlG16HO49zMUXX1zrKphZDvS4E6q16iba1LndzKxQjwr3vn37smLFCgdVJ0UEK1asoG/fvrWuipn1ED2qW2bo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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x1160afe10>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# The metrics below are in billions of dollars\n",
    "revenue_by_quarter = [2.79, 2.98,3.29,3.7]\n",
    "earnings_by_quarter = [.0656,.12959,.18552,.29012]\n",
    "quarter_labels = [\"2Q2017\",\"3Q2017\",\"4Q2017\", \"1Q2018\"]\n",
    "# Revenue\n",
    "n = 1  # This is our first dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = 4 # Number of sets of bars\n",
    "w = 1 # Width of each bar\n",
    "bars1_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "# Earnings\n",
    "n = 2  # This is our second dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = 4 # Number of sets of bars\n",
    "w = 1 # Width of each bar\n",
    "bars2_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "\n",
    "middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]\n",
    "labels = [\"Revenue\", \"Earnings\"]\n",
    "plt.bar(bars1_x, revenue_by_quarter)\n",
    "plt.bar(bars2_x, earnings_by_quarter)\n",
    "plt.legend(labels)\n",
    "plt.title(\"2017 Quarterly Analysis of Netflix\")\n",
    "plt.xticks(middle_x, quarter_labels)\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "What are your first impressions looking at the visualized data?\n",
    "\n",
    "- Does Revenue follow a trend?\n",
    "- Do Earnings follow a trend?\n",
    "- Roughly, what percentage of the revenue constitutes earnings?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Both revenue and earnings follow increasing trend just like trend of stocks.\n",
    "#Both revenue and earnings are expected to grow in future.\n",
    "#Earnings are about 7 to 8 % of revenue constitutes earnings.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 8\n",
    "\n",
    "In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure. \n",
    "\n",
    "Since `Price` which is the most relevant data is in the Y axis, let's map our subplots to align vertically side by side.\n",
    "- We have set up the code for you on line 1 in the cell below. Complete the figure by passing the following arguments to `plt.subplots()` for the first plot, and tweaking the third argument for the second plot\n",
    "    - `1`-- the number of rows for the subplots\n",
    "    - `2` -- the number of columns for the subplots\n",
    "    - `1` -- the subplot you are modifying\n",
    "\n",
    "- Chart the Netflix Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`netflix_stocks['Date'], netflix_stocks['Price']`)\n",
    "- Assign \"Netflix\" as a title to this subplot. Hint: `ax1.set_title()`\n",
    "- For each subplot, `set_xlabel` to `\"Date\"` and `set_ylabel` to `\"Stock Price\"`\n",
    "- Chart the Dow Jones Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`dowjones_stocks['Date'], dowjones_stocks['Price']`)\n",
    "- Assign \"Dow Jones\" as a title to this subplot. Hint: `plt.set_title()`\n",
    "- There is some crowding in the Y axis labels, add some space by calling `plt.subplots_adjust(wspace=.5)`\n",
    "- Be sure to `.show()` your plots.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x116466e10>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
   "source": [
    "# Left plot Netflix\n",
    "# ax1 = plt.subplot(total number rows, total number columns, index of subplot to modify)\n",
    "ax1=plt.subplot(1,2,1)\n",
    "plt.bar(netflix_stocks[\"Date\"],netflix_stocks[\"Price\"])\n",
    "ax1.set_title(\"Netflix\")\n",
    "ax1.set_xlabel(\"Date\")\n",
    "ax1.set_ylabel(\"Stock Price\")\n",
    "\n",
    "\n",
    "\n",
    "# Right plot Dow Jones\n",
    "# ax2 = plt.subplot(total number rows, total number columns, index of subplot to modify)\n",
    "ax2=plt.subplot(1,2,2)\n",
    "plt.bar(dowjones_stocks[\"Date\"],dowjones_stocks[\"Price\"])\n",
    "ax2.set_title(\"Dow Jones\")\n",
    "ax2.set_xlabel(\"Date\")\n",
    "plt.subplots_adjust(wspace=0.5)\n",
    "plt.show()\n",
    "\n",
    "\n",
    "\n",
    "print(len(netflix_stocks[\"Date\"]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- How did Netflix perform relative to Dow Jones Industrial Average in 2017?\n",
    "- Which was more volatile?\n",
    "- How do the prices of the stocks compare?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 9\n",
    "\n",
    "It's time to make your presentation! Save each of your visualizations as a png file with `plt.savefig(\"filename.png\")`.\n",
    "\n",
    "As you prepare your slides, think about the answers to the graph literacy questions. Embed your observations in the narrative of your slideshow!\n",
    "\n",
    "Remember that your slideshow must include:\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
