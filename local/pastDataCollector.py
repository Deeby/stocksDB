import json
import datetime
import pandas_datareader.data as web
import sys
import csv
import socket
import pymysql
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

# Crawling for C_DAYS
C_DAYS = 1200
end = datetime.datetime.now().date()
start = end - datetime.timedelta(days=C_DAYS)

passcode = True
while passcode:
    #print("1. KOSPI DATA ")
    #print("2. KOSDAQ DATA ")
    #selection=int(input("Which one do you want to download? : "))
    selection = str(2)
 
    if selection == str(1):
        stock_code = open('KOSPI.csv','r')
        passcode = False
    elif selection == str(2):
        stock_code = open('KOSDAQ.csv','r')
        passcode = False
    else:
        print("Wrong Number !! Try again !!!" )
csvReader = csv.reader(stock_code)


#jsonFile = '/Users/sh/Documents/_iPython/Stock_Data/test_run.json'
  
#Database 연결
conn = pymysql.connect(host='localhost', port=3306, user='ADMIN', passwd='ADMIN', db='stock',charset='utf8',autocommit=False)
cur = conn.cursor()



for st in csvReader:
        
    StockCode = st[1]
    CompanyName = st[2]
    print(StockCode, "-" , CompanyName)
    print(st[0],StockCode,CompanyNamem)
    try:
        if selection == str(1):
            stock_data = web.DataReader("%s.KS" %st[1],'yahoo',start,end)
        if selection == str(2):
            stock_data = web.DataReader("%s.KQ" %st[1],'yahoo',start,end)

        stock_data.loc[:,'Company'] = CompanyName
        stock_data.loc[:,'StockCode'] = StockCode
        stock_data.loc[:,'Date'] = stock_data.index.astype('str')
        json = open('/Users/sh/Documents/_iPython/Stock_Data/DAILY_STOCK_DATA.json','a')
        #StockData.append(stock_data)
        #json.dumps(stock_data, ensure_ascii=False, sort_keys=False, separators=(',', ':')).encode('utf-8')
        # force_ascii=False for korean
        json.write(stock_data.to_json(orient='records',force_ascii=False))
        json.close()
        engine = create_engine('mysql+mysqlconnector://root:pw@localhost:3306/YourDB_NAME', echo=False)
        stock_data.to_sql(name='stock_records', con=engine, if_exists = 'append', index=False)
        print(stock_data)


    except:
        pass

    
    
stock_code.close()
conn.commit()
conn.close()
print("Complete the task !! ")