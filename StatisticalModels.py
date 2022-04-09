import statistics
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 


def calcSimpleMovingAverage(data): 
    total_sum = 0 
    count = 0
    for prices in data: 
        close_ = float(prices[4])
        total_sum += close_
        count += 1
    
    common_average = round((total_sum / count), 5)
    return common_average


def calcPercentageIncrease(open_, close_): 
    # Calculate the % difference between the current price and the close price of the previous candle
    # If the price increased, use the formula [(New Price - Old Price)/Old Price] and then multiply that number by 100.
    percentage_Increase = (open_ - close_) / (close_ * 100)
    return percentage_Increase
 

def calcPercentageDecrease(open_, close_): 
    # If the price decreased, use the formula [(Old Price - New Price)/Old Price] and multiply that number by 100. 
    percentage_Decrease = (close_ - open_) / (close_* 100)
    return percentage_Decrease


def calcStandardDeviation(data): 
    close_= []
    for prices in data: 
        close_.append(float(prices[4]))

    return statistics.stdev(close_)




# Whenever the asset crosses the upper boundary, it is time to sell, and similarly, when the asset crosses the lower boundary, it is time to buy.
# https://blog.finxter.com/bollinger-bands-algorithm-python-binance-api-for-crypto-trading/
# https://codingandfun.com/bollinger-bands-pyt/

def calcBollingerBands(data, crypto_symbol, real_tender):
    # converts the API response dictionary into a Pandas DataFrame using the Pandas from_dict() method

    pricesOfCrypto = pd.DataFrame.from_dict(data)
    #pricesOfCrypto = pricesOfCrypto.set_index(0) # is the timestamp column

    #print(pricesOfCrypto)

    pricesOfCrypto.insert(7, 8, pricesOfCrypto[4].rolling(2, min_periods=1).mean()) # where 8 is 'mean' 
    pricesOfCrypto.insert(8, 9, pricesOfCrypto[4].rolling(2, min_periods=1).std()) # where 9 is 'std (standard deviation)'

    upperbound = pricesOfCrypto[8] + (pricesOfCrypto[9] * 2)
    lowerbound = pricesOfCrypto[8] - (pricesOfCrypto[9] * 2)

    pricesOfCrypto.insert(9, 10, upperbound) # where 10 is the upperbound 
    pricesOfCrypto.insert(10, 11, lowerbound) # and 11 is the lower bound

    #print(pricesOfCrypto.iloc[0:, 0:1])
    #print(pricesOfCrypto.iloc[0:, 4:5])
    #print(len(pricesOfCrypto) - 2)
    #print(pricesOfCrypto)

    #Dateframe requires iloc to be used so we can specify index within the data 

    #print(pricesOfCrypto.iloc[len(pricesOfCrypto) - 2:len(pricesOfCrypto) - 1, 10:11]) 
    #print(pricesOfCrypto.iloc[len(pricesOfCrypto) - 2:len(pricesOfCrypto) - 1, 9:10]) 

    # i is short for indexed 
    iupperbound = pricesOfCrypto.iloc[len(pricesOfCrypto) - 2:len(pricesOfCrypto) - 1, 9:10] # upperbound value in relation to previous closing price [58:59, 9:10]
    ilowerbound = pricesOfCrypto.iloc[len(pricesOfCrypto) - 2:len(pricesOfCrypto) - 1, 10:11] # lowerbound value in relation to previous closing price [58:59, 10:11]
    ipreviousclose = pricesOfCrypto.iloc[len(pricesOfCrypto) - 2:len(pricesOfCrypto) - 1, 4:5] # [0: previous close, 4:5 (close column)]

    #print(ilowerbound)
    #print(iupperbound)
    #print(ipreviousclose)
    #print(ipreviousclose[4][58])
    #print(ipreviousclose[4][58])
    #print(ipreviousclose[4][58])

    # disecting values stored within the frame from 3 dimensions to 1. Where the three dimensions are the rows, columns and the value itself. 
    arrayify = []

    # Length may change due to unknown increase in the number of rows within the frame after each regernetaion of counters, hence we have not used i.e. [10][58] row. 
    # Future proofing in the instance the issue cannot be resolved. Does not affect the outcome when triggering conditions to place buy/sell events. 
    # Specifying index will range from 0 - 2 when wanting to perform logical comparison between previous closing price and upper/lower bounds. 
    arrayify.append(iupperbound[10][len(pricesOfCrypto) - 2]) # index 0 of array is 'upperbound' 
    arrayify.append(ilowerbound[11][len(pricesOfCrypto) - 2]) # index 1 of array is 'ilowerbound' 
    arrayify.append(ipreviousclose[4][len(pricesOfCrypto) - 2]) # index 2 is 'previous closing price of array) 

    #print(arrayify)

    if float(arrayify[2]) < float(arrayify[0]) and float(arrayify[2]) > calcSimpleMovingAverage(data): # previous close less than upperbound and greater than mean 
        return 0
    elif float(arrayify[2]) > float(arrayify[1]) and float(arrayify[2]) < calcSimpleMovingAverage(data): # previous close greater than lowerbound and less than mean 
        return 1
    elif float(arrayify[2]) > float(arrayify[0]): # close greater than upperbound
        return 2
    elif float(arrayify[2]) < float(arrayify[1]): # close less than lowerbound
        return 3


def store_upper_and_lower_bounds(data):
    # converts the API response dictionary into a Pandas DataFrame using the Pandas from_dict() method

    pricesOfCrypto = pd.DataFrame.from_dict(data)
    #pricesOfCrypto = pricesOfCrypto.set_index(0) # is the timestamp column

    #print(pricesOfCrypto)

    pricesOfCrypto.insert(7, 8, pricesOfCrypto[4].rolling(2, min_periods=1).mean()) # where 8 is 'mean' 
    pricesOfCrypto.insert(8, 9, pricesOfCrypto[4].rolling(2, min_periods=1).std()) #where 9 is 'std (standard deviation)'

    upperbound = pricesOfCrypto[8] + (pricesOfCrypto[9] * 2)
    lowerbound = pricesOfCrypto[8] - (pricesOfCrypto[9] * 2)

    pricesOfCrypto.insert(9, 10, upperbound) # where 10 is the upperbound 
    pricesOfCrypto.insert(10, 11, lowerbound) # and 11 is the lower bound

    iupperbound = pricesOfCrypto.iloc[len(pricesOfCrypto) - 2:len(pricesOfCrypto) - 1, 9:10] # upperbound value in relation to previous closing price [58:59, 9:10]
    ilowerbound = pricesOfCrypto.iloc[len(pricesOfCrypto) - 2:len(pricesOfCrypto) - 1, 10:11] # lowerbound value in relation to previous closing price [58:59, 10:11]
    ipreviousclose = pricesOfCrypto.iloc[len(pricesOfCrypto) - 2:len(pricesOfCrypto) - 1, 4:5] # [0: previous close, 4:5 (close column)]

        # disecting values stored within the frame from 3 dimensions to 1. Where the three dimensions are the rows, columns and the value itself. 
    arrayify = []

    upperbound_formatted = "{:.5f}".format(iupperbound[10][len(pricesOfCrypto) - 2])
    lowerbound_formatted = "{:.5f}".format(ilowerbound[11][len(pricesOfCrypto) - 2])
    
    # Length may change due to unknown increase in the number of rows within the frame after each regernetaion of counters, hence we have not used i.e. [10][58] row. 
    # Future proofing in the instance the issue cannot be resolved. Does not affect the outcome when triggering conditions to place buy/sell events. 
    # Specifying index will range from 0 - 2 when wanting to perform logical comparison between previous closing price and upper/lower bounds. 
    arrayify.append(str(upperbound_formatted)) # index 0 of array is 'upperbound' 
    arrayify.append(str(lowerbound_formatted)) # index 1 of array is 'lowerbound' 
    arrayify.append(str(ipreviousclose[4][len(pricesOfCrypto) - 2])) # index 2 is 'previous closing price of array) 
    
    #time.sleep(0.5) # Put in place to prevent 'float' object from being non-subscriptable

    return arrayify


# Technical Indicators used as Features to predict reliance of indicators used in trading strategy. 
def calc_indicators(data): 
    #[open, high, low, close]
    #dataset[[1, 2, 3, 4]]  
    dataset = pd.DataFrame.from_dict(data)
    #dataset = dataset.dropna() # removes rows containing null values 

    dataset = dataset.dropna()

    open_ = pd.to_numeric(dataset[1])
    high_ = pd.to_numeric(dataset[2])
    low_ = pd.to_numeric(dataset[3])
    close_ = pd.to_numeric(dataset[4])
    
    # The first thing to notice is that by default rolling looks for n-1 prior rows of data to aggregate,
    # where n is the window size. If that condition is not met, it will return NaN for the window. This is
    # what's happening at the first row. In the fourth and fifth row, it's because one of the values in the sum is NaN.

    # If you would like to avoid returning NaN, you could pass min_periods=1 to the method which reduces the minimum 
    # required number of valid observations in the window to 1 instead of 2
 
    dataset['H-L'] = high_ - low_
    dataset['O-C'] = open_ - close_
    dataset['ma'] = close_.rolling(2, min_periods=1).mean()
    dataset['std'] = close_.rolling(window=2).std().fillna(method='bfill').fillna(method='ffill')
    dataset['Price_Rise'] = np.where(close_.shift(-1) > close_, 1, 0)

    upperbound = dataset['ma'] + (dataset['std'] * 2)
    lowerbound = dataset['ma'] - (dataset['std'] * 2)

    dataset['Upperbound'] = upperbound
    dataset['Lowerbound'] = lowerbound

    #print(dataset)

    return dataset


def graph_representations_of_indicators(data): 

    dataset = calc_indicators(data)
    
    open_ = pd.to_numeric(dataset[1])
    high_ = pd.to_numeric(dataset[2])
    low_ = pd.to_numeric(dataset[3])
    close_ = pd.to_numeric(dataset[4])

    
    # High vs Low in relation to Close
    close_, low_, high_.plot(figsize=(10,6))

    plt.grid(True)
    plt.title("High vs Low in relation to Closing price")
    plt.axis('tight')
    plt.xlabel('no. of data point (60 closing prices per hour)')
    plt.ylabel('Price')
    plt.savefig('graphical_representations/High_VS_Low_in_relation_to_Close.png')
    plt.close() # Reduce the number of plts opened. Reduce memory usage (kbytes)


    # Open vs Close
    open_, close_.plot(figsize=(10,6))
    plt.grid(True)
    plt.title("Open price vs Closing price")
    plt.axis('tight')
    plt.xlabel('no. of data point (60 closing prices per hour)')
    plt.ylabel('Price')
    plt.savefig('graphical_representations/Open_vs_Close.png')
    plt.close() # Reduce the number of plts opened. Reduce memory usage (kbytes)

    # High - Low in relation to Close
    dataset[['H-L']].plot(figsize=(10,6))
    plt.grid(True)
    plt.title("High Price vs Low Price")
    plt.axis('tight')
    plt.xlabel('no. of data point (60 closing prices per hour)')
    plt.ylabel('Price')
    plt.savefig('graphical_representations/High-Low_in_relation_to_Close.png')
    plt.close() # Reduce the number of plts opened. Reduce memory usage (kbytes)

    # Open - Close in relation to Close
    dataset[['O-C']].plot(figsize=(10,6))
    plt.grid(True)
    plt.title("Open Price vs Close Price")
    plt.axis('tight')
    plt.xlabel('no. of data point (60 closing prices per hour)')
    plt.ylabel('Price')
    plt.savefig('graphical_representations/Open-Close_in_relation_to_Close.png')
    plt.close() # Reduce the number of plts opened. Reduce memory usage (kbytes)

    # OHLC all in one graph 
    open_, high_, low_, close_.plot(figsize=(10,6))
    plt.grid(True)
    plt.title("OHLC")
    plt.axis('tight')
    plt.xlabel('no. of data point (60 closing prices per hour)')
    plt.ylabel('Price')
    plt.savefig('graphical_representations/OHLC.png')
    plt.close() # Reduce the number of plts opened. Reduce memory usage (kbytes)

    # Moving Average 
    dataset[['ma']].plot(figsize=(10,6))
    plt.grid(True)
    plt.title("Moving Average")
    plt.axis('tight')
    plt.xlabel('no. of data point (60 closing prices per hour)')
    plt.ylabel('Price')
    plt.savefig('graphical_representations/ma.png')
    plt.close() # Reduce the number of plts opened. Reduce memory usage (kbytes)

    # Standard Deviation
    dataset[['std']].plot(figsize=(10,6))
    plt.grid(True)
    plt.title("Standard deviation")
    plt.axis('tight')
    plt.xlabel('no. of data point (60 closing prices per hour)')
    plt.ylabel('Price')
    plt.savefig('graphical_representations/std.png')
    plt.close() # Reduce the number of plts opened. Reduce memory usage (kbytes)

    # Price Rise 
    dataset[['Price_Rise']].plot(figsize=(10,6))
    plt.grid(True)
    plt.title("Price Rise")
    plt.axis('tight')
    plt.xlabel('no. of data point (60 closing prices per hour)')
    plt.ylabel('Price')
    plt.savefig('graphical_representations/Price_Rise.png')
    plt.close() # Reduce the number of plts opened. Reduce memory usage (kbytes)

    # Upper bound VS Lower Bound along with the mean price
    dataset[['ma', 'Upperbound', 'Lowerbound']].plot()
    plt.grid(True)
    plt.title("Bollinger Bands")
    plt.axis('tight')
    plt.xlabel('no. of data point (60 closing prices per hour)')
    plt.ylabel('Price')
    plt.savefig('graphical_representations/Bollinger_Bands.png')
    plt.close() # Reduce the number of plts opened. Reduce memory usage (kbytes)

    # All indicators in one graph 
    open_, high_, low_, close_.plot(figsize=(10,6))
    dataset[['ma', 'std', 'H-L', 'O-C', 'Price_Rise', 'Upperbound', 'Lowerbound']].plot()
    plt.grid(True)
    plt.title("All indicators in one")
    plt.axis('tight')
    plt.xlabel('no. of data point (60 closing prices per hour)')
    plt.ylabel('Price')
    plt.savefig('graphical_representations/All_indicators.png')
    plt.close() # Reduce the number of plts opened. Reduce memory usage (kbytes)



