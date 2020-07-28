+-----------+--------+------+-----+---------+-------+
| Field     | Type   | Null | Key | Default | Extra |
+-----------+--------+------+-----+---------+-------+
| High      | double | YES  |     | NULL    |       |
| Low       | double | YES  |     | NULL    |       |
| Open      | double | YES  |     | NULL    |       |
| Close     | double | YES  |     | NULL    |       |
| Volume    | double | YES  |     | NULL    |       |
| Adj Close | double | YES  |     | NULL    |       |
| Company   | text   | YES  |     | NULL    |       |
| StockCode | text   | YES  |     | NULL    |       |
| Date      | text   | YES  |     | NULL    |       |
+-----------+--------+------+-----+---------+-------+

--연속으로 주가 하락한 종목 이름을 보여주는 쿼리
--아주 그지같은 성능때문에 성능개선이 필요함.
SELECT
    company
FROM(
SELECT
   (select close from stock where company = a.company and date = '2020-07-28' ) as one,
   (select close from stock where company = a.company and date = '2020-07-27' ) as two,
   (select close from stock where company = a.company and date = '2020-07-24' ) as three,
   (select close from stock where company = a.company and date = '2020-07-23' ) as four,
   (select close from stock where company = a.company and date = '2020-07-22' ) as five,
   a.company
FROM
    (SELECT DISTINCT company FROM stock) a 
) a
WHERE a.five  > a.four  
and   a.four  > a.three 
and   a.three > a.two   
and   a.two   > a.one   ;






select distinct company from stock where close > 1000000 and date = '2020-07-28';
