CREATE TABLE stock_records (
       Open                     INT,
       High                     INT,
       Low                      INT,
       Close                    INT,
       Volume                   INT,
       Adj_Close                DECIMAL(20,2),
       Company                  VARCHAR(100),
       StockCode                VARCHAR(6) NOT NULL,
       Date                     Date NOT NULL,
    
      CONSTRAINT PLAYER_PK PRIMARY KEY (StockCode,Date)
    
);
