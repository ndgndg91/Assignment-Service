DROP TABLE ACCOUNT PURGE;
DROP TABLE BRANCH PURGE;
DROP TABLE CUSTOMER PURGE;
DROP TABLE LOAN PURGE;
DROP TABLE BORROWER PURGE;
DROP TABLE DEPOSITOR PURGE;
DROP VIEW ALL_CUSTOMER;
CREATE TABLE ACCOUNT(
    ACCOUNT_NUMBER VARCHAR2(20) PRIMARY KEY,
    BRANCH_NAME VARCHAR2(20),
    BALANCE NUMBER
);

insert into account values('A-101','Downtown',500);
insert into account values('A-102','Perryridge',400);
insert into account values('A-201','Brighton',900);
insert into account values('A-215','Mianus',700);
insert into account values('A-217','Brighton',750);
insert into account values('A-222','Redwood',700);
insert into account values('A-305','Round Hill',350);

select * from account;



CREATE TABLE BRANCH(
    BRANCH_NAME VARCHAR2(20) PRIMARY KEY,
    BRANCH_CITY VARCHAR2(20),
    ASSETS NUMBER
);

insert into branch values('Brighton','Brooklyn',7100000);
insert into branch values('Downtown','Brooklyn',9000000);
insert into branch values('Mianus','Horseneck',400000);
insert into branch values('North Town','Rye',3700000);
insert into branch values('Perryridge','Horseneck',1700000);
insert into branch values('Pownal','Benninghton',300000);
insert into branch values('Redwood','Palo Alto',2100000);
insert into branch values('Round Hill','Horseneck',8000000);

select * from branch;





CREATE TABLE CUSTOMER(
    CUSTOMER_NAME VARCHAR2(20) PRIMARY KEY,
    CUSTOMER_STREET VARCHAR2(20),
    CUSTOMER_CITY VARCHAR2(20)
);

insert into customer values('Adams','Spring','Pittsfield');
insert into customer values('Brooks','Senator','Brooklyn');
insert into customer values('Curry','North','Rye');
insert into customer values('Glenn','Sand Hill','Woodside');
insert into customer values('Green','Walnut','Stamford');
insert into customer values('Hayes','Main','Harrison');
insert into customer values('Johnson','Alma','Palo Alto');
insert into customer values('Jones','Main','Harrison');
insert into customer values('Lindsay','Park','Pittsfield');
insert into customer values('Smith','North','Rye');
insert into customer values('Turner','Putnam','Stamford');
insert into customer values('Williams','Nassau','Princeton');

select * from customer;




CREATE TABLE LOAN(
    LOAN_NUMBER VARCHAR2(20) PRIMARY KEY,
    BRANCH_NAME VARCHAR2(20),
    AMOUNT NUMBER
);

insert into loan values('L-11','Round Hill',900);
insert into loan values('L-14','Downtown',1500);
insert into loan values('L-15','Perryridge',1500);
insert into loan values('L-16','Perryridge',1300);
insert into loan values('L-17','Downtown',1000);
insert into loan values('L-23','Redwood',2000);
insert into loan values('L-93','Mianus',500);

select * from loan;



CREATE TABLE BORROWER(
    CUSTOMER_NAME VARCHAR2(20),
    LOAN_NUMBER VARCHAR2(20)
);

insert into borrower values('Adams', 'L-16');
insert into borrower values('Curry', 'L-93');
insert into borrower values('Hayes', 'L-15');
insert into borrower values('Johnson', 'L-14');
insert into borrower values('Jones', 'L-17');
insert into borrower values('Smith', 'L-11');
insert into borrower values('Smith', 'L-23');
insert into borrower values('Williams', 'L-17');

select * from borrower;


CREATE TABLE DEPOSITOR(
    CUSTOMER_NAME VARCHAR2(20),
    ACCOUNT_NUMBER VARCHAR2(20)
);

insert into depositor values('Hayes', 'A-102');
insert into depositor values('Johnson', 'A-101');
insert into depositor values('Johnson', 'A-201');
insert into depositor values('Jones', 'A-217');
insert into depositor values('Lindsay', 'A-222');
insert into depositor values('Smith', 'A-215');
insert into depositor values('Turner', 'A-305');

select * from depositor;

--3. 중복되지 않은 모든 지점들의 이름을 구하라.(distinct)
select DISTINCT branch_name
from branch;

--4.Perryridge 지점에서 $1200 이상의 대출 총액을 지닌 모든 대출에 대해 대출 번호를 전부 구하라.
--(select)
select loan_number
from branch b, loan l
where b.branch_name = l.branch_name and l.amount >= 1200 and b.branch_name ='Perryridge';

--5.은행에 대출을 가지고 있는 모든 고객들에 대해 그들의 이름과 대출번호와 대출 액수를 구하라.
--(select)
select customer_name, l.loan_number, amount
from borrower b, loan l
where b.loan_number = l.loan_number;

--6.Perryridge 지점의 모든 대출에 대하여 고객의 이름과 대출 번호, 대출 액수를 구하라.
select customer_name, l.loan_number, l.amount
from loan l, borrower b
where l.loan_number = b.loan_number and l.branch_name = 'Perryridge';

--7. 이름에 'Main'이라는 부분 문자열이 포함된 거리에 살고 있는 모든 고객들의 이름을 구하여라. (like) 
select customer_name
from customer
where customer_street like '%Main%';

--8. Perryridge 지점의 대출을 가진 모든 고객들을 알파벳 순서로 나열하라. (order by)
select customer_name
from branch b, loan l, borrower bo
where l.branch_name = b.branch_name and
bo.loan_number = l.loan_number and b.branch_name = 'Perryridge'
order by 1;

--9. 은행에서 대출, 계좌 혹은 둘 다를 가진 모든 고객을 나열하라. (union) 
select distinct customer_name
from borrower
union
select distinct customer_name
from depositor;

--10. 대출 총액이 가장 큰 고객의 이름과 대출 총액을 구하여라. (max)
select customer_name, amount
from loan l, borrower bo
where l.loan_number = bo.loan_number
and amount = (select max(amount)
from loan l, borrower bo
where l.loan_number = bo.loan_number);

--11. Harrison과 Woodside 에 살지 않으면서 계좌에 잔고가 500이상 있는 고객의 이름과 고객이 사 는 도시를 구하라. (select) 
select c.customer_name,c.customer_city
from customer c, depositor de, account ac
where c.customer_name = de.customer_name and ac.account_number = de.account_number 
and customer_street != 'Woodside' and customer_city != 'Harrison'
and balance >= 500;

--12. Perryridge 지점에서 계좌의 평균 잔고를 구하여라. (avg) 
select avg(balance)
from account
where branch_name = 'Perryridge';

--13. 각 지점의 평균 계좌 잔고를 구하라. (avg, group by) 
select b.branch_name, avg(balance)
from account ac, branch b
where b.branch_name = ac.branch_name
group by b.branch_name;

--14. 각 지점의 예금자들의 수를 구하라. (count, group by) 
select b.branch_name, count(de.customer_name)
from depositor de, account ac, branch b
where ac.account_number = de.account_number and b.branch_name = ac.branch_name
group by b.branch_name;

--15. 평균 잔고가 $800 이상인 지점 이름과 평균 잔고를 나열하라. (avg, group by, having)
select b.branch_name,avg(balance)
from branch b, account ac, depositor de
where b.branch_name = ac.branch_name and de.account_number = ac.account_number
group by b.branch_name
having avg(balance) >= 800;

--16. 모든 계좌의 평균 잔고를 구하라. (avg) 
select avg(balance)
from account;

--17. Palo Alto 에 살고 최소한 두 개의 계좌를 가진 각각의 고객들의 이름과 평균 잔고를 구하라. (group by, having) 
select c.customer_name, avg(balance)
from customer c, account ac, depositor de
where de.account_number = ac.account_number and de.customer_name = c.customer_name
group by c.customer_name
having count(ac.account_number) >= 2;

--18. 같은 도시에 사는 고객의 이름의 쌍을 구하여라. (select) 
select c1.customer_name, c2.customer_name
from (select customer_name, customer_city from customer) c1, 
(select customer_name, customer_city from customer) c2
where c1.customer_city = c2.customer_city
and c1.customer_name != c2.customer_name;

--19. 각 도시 별로 가장 높은 대출 총액을 가지고 있는 고객의 이름과 대출 총액을 구하여라. 단, 대출 을 가진 고객이 살지 않는 도시는 표시하지 않는다. (max, group by) 
select customer_name, max(총액)
from (
select c.customer_city, c.customer_name, max(amount) as "총액"
from loan l, branch b, borrower bo, customer c
where l.branch_name = b.branch_name and bo.loan_number = l.loan_number
and c.customer_name = bo.customer_name
and c.customer_city = b.branch_city
group by c.customer_city , c.customer_name) 
group by customer_name;

--20. 지점 이름과 그 지점에 계좌나 대출 둘 중 하나를 가진 고객 이름으로 구성된 View 를 작성하라. 단 View의 이름은 all_customer이다. (create view) 
create or replace view all_customer
as
select *
from(
select b.branch_name, b.branch_city, assets, ac.account_number,balance,customer_name
from branch b, account ac, depositor de
where b.branch_name = ac.branch_name and de.account_number = ac.account_number
union
select b.branch_name, b.branch_city, assets, l.loan_number, amount, customer_name
from branch b, loan l, borrower bo
where b.branch_name = l.branch_name and l.loan_number = bo.loan_number)
order by 4;

select *
from all_customer;

--21. 20에서 생성된 View 를 이용하여 Perryridge 지점의 모든 고객 이름을 나열하라. 
select distinct customer_name
from all_customer
where branch_name = 'Perryridge';
--22. 각 지점에서 총 잔고의 최대값을 나열하라. (as) 
select branch_name, max(balance) AS "최대값"
from account
group by branch_name;