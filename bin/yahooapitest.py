#!/usr/bin/env python
#  Copyright (c) 2014, Rob Innes Hislop
#  email:robinneshislop__AT__gmail.com

"""
This module queries the Yahoo Finance API
with every allowable data key, one at a time
and prints the raw output
"""
import urllib2
from pyhoofinance import * # Useful constants
from pyhoofinance.quotedata import get_quotes

def get_quote(symbol, dataKey):
    """
    Queries Yahoo for quotes. List of symbols must be no
    greater than 200 per Yahoo limits
     
    Returns list of dictionaries
    """

    # Retrieve block of quotes in the form of a CSV file
    url = 'http://finance.yahoo.com/d/quotes.csv?s='+symbol+'&f='+dataKey
        
    # For each line of the CSV, extract quote data and store
    try:
        rawData = urllib2.urlopen(url)
    except:
        print('urlopen failed')
        return []

    if (rawData.msg != 'OK'):
        print ('URL request failed: {}'.format(rawData.msg))
        return []
    rawData = rawData.read().splitlines()

    return rawData

if __name__=='__main__':
    numQuotes = 1000
    symbolList = ['YHOO' for i in range(numQuotes)]
    quotes = get_quotes(symbolList)
    print len(quotes)
    while len(quotes) == len(symbolList):
        numQuotes += 1
        symbolList.append('YHOO')
        quotes = get_quotes(symbolList)
        print 'lengths %s %s' % (len(symbolList), len(quotes))
    print numQuotes
    # print quotes[:-2]
    
    """
    for data in YAHOO_FINANCE_KEYS_DICT:
        key = YAHOO_FINANCE_KEYS_DICT[data]
        print('{0:>42} = {1:3} --> {2}'.format(data, key, get_quote('TWTR',key)))
    """