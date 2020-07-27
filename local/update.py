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

#-----------------------------------------------------------------
# DESC
# 매일 돌면서 당일의 종목데이터를 DB에 저장 
#-----------------------------------------------------------------


# Crawling for C_DAYS
C_DAYS = 1000
end = datetime.datetime.now().date()
start = end

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


row = 0

for st in csvReader:

    print(st)    
    
    StockCode = st[0]
    CompanyName = st[1]
    print(st[0],StockCode,CompanyName)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    try:
        print("0번마")
        if selection == str(1):
            stock_data = web.DataReader("%s.KS" %st[0],'yahoo',start,end)
        if selection == str(2):
            print("너냐")
            stock_data = web.DataReader("%s.KQ" %st[0],'yahoo',start,end)
            print("너냐!")
        print("1번마")
        stock_data.loc[:,'Company'] = CompanyName
        stock_data.loc[:,'StockCode'] = StockCode
        stock_data.loc[:,'Date'] = stock_data.index.astype('str')
        json = open('DAILY_STOCK_DATA.json','a')
        #StockData.append(stock_data)
        #json.dumps(stock_data, ensure_ascii=False, sort_keys=False, separators=(',', ':')).encode('utf-8')
        # force_ascii=False for korean
        print("2번마")
        json.write(stock_data.to_json(orient='records',force_ascii=False))
        json.close()
        print("3번마")
        engine = create_engine('mysql+mysqlconnector://ADMIN:ADMIN@localhost:3306/stock', echo=False)
        print("4번마")
        stock_data.to_sql(name='stock', con=engine, if_exists = 'append', index=False)
        print(stock_data)

        
        print("------------------------------------")
        
       
    except:
        print("예외입니다잉")
        pass
    row = row+1
    print(row)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    if(row==10):
        break
    
    
stock_code.close()
conn.commit()
conn.close()
print("Complete the task !! ")