/* �ý��� �������� ���� */
DROP USER hanart CASCADE;

CREATE USER hanart 
IDENTIFIED BY hanart
Default Tablespace users
Temporary Tablespace temp
profile default;

GRANT Connect, RESOURCE TO hanart;
-- GRANT create view, create synonym to madang;

ALTER USER hanart ACCOUNT unlock;

drop table customer CASCADE CONSTRAINTS;
drop table Mart CASCADE CONSTRAINTS;
drop table emp CASCADE CONSTRAINTS;
drop table Car CASCADE CONSTRAINTS;
drop table product CASCADE CONSTRAINTS;
drop table sales_emp CASCADE CONSTRAINTS;
drop table m_customer CASCADE CONSTRAINTS;
drop table orders CASCADE CONSTRAINTS;
purge recyclebin;
select * from tab;

CREATE TABLE customer
(
	c_no                 NUMBER NOT NULL ,
	c_name               VARCHAR2(20) NULL ,
	c_birth              DATE NULL ,
	c_address            VARCHAR2(20) NULL ,
	ship_address         VARCHAR2(20) NULL ,
	c_phone              VARCHAR2(20) NULL 
);

ALTER TABLE customer
	ADD  PRIMARY KEY (c_no);

CREATE TABLE Mart
(
	m_no                 NUMBER NOT NULL ,
	m_name               VARCHAR2(20) NULL ,
	m_address            VARCHAR2(20) NULL ,
	m_phone              VARCHAR2(20) NULL 
);

ALTER TABLE Mart
	ADD  PRIMARY KEY (m_no);

CREATE TABLE emp
(
	e_no                NUMBER NOT NULL ,
	m_no                 NUMBER NULL ,
	e_name                VARCHAR2(20) NULL ,
	e_address            VARCHAR2(20) NULL ,
	e_birth              DATE NULL ,
	e_phone              VARCHAR2(20) NULL ,
	e_type               VARCHAR2(20) NULL ,
	e_sal_year           NUMBER NULL ,
	mgr                  NUMBER NULL 
);

ALTER TABLE emp
	ADD  PRIMARY KEY (e_no);

CREATE TABLE Car
(
	c_no                 NUMBER NOT NULL ,
	c_manufac              VARCHAR2(20) NULL ,
	c_model                VARCHAR2(20) NULL ,
	c_max_weight           NUMBER NULL ,
	c_prod_year            DATE NULL ,
	m_no                 NUMBER NOT NULL 
);

ALTER TABLE Car
	ADD  PRIMARY KEY (c_no);

CREATE TABLE product
(
	p_no                 NUMBER NOT NULL ,
	p_name               VARCHAR2(20) NULL ,
	o_price              NUMBER NULL ,
	c_price              NUMBER NULL ,
	cnt                  NUMBER NULL 
);

ALTER TABLE product
	ADD  PRIMARY KEY (p_no);

CREATE TABLE sales_emp
(
	e_no                NUMBER NOT NULL ,
	max_sales            CHAR(18) NULL ,
	goal_sales           CHAR(18) NULL 
);

ALTER TABLE sales_emp
	ADD  PRIMARY KEY (e_no);

CREATE TABLE m_customer
(
	c_no                 NUMBER NOT NULL ,
	e_no                NUMBER NULL 
);

ALTER TABLE m_customer
	ADD  PRIMARY KEY (c_no);

CREATE TABLE orders
(
	o_no                NUMBER NOT NULL ,
	e_no                NUMBER NOT NULL ,
	c_no                NUMBER NULL ,
	o_date              date NULL ,
	ship_address        VARCHAR2(20) NULL ,
	o_cnt               NUMBER NULL ,
	o_total             NUMBER NULL ,
	p_no                 NUMBER NULL 
);

ALTER TABLE orders
	ADD  PRIMARY KEY (o_no);

ALTER TABLE emp
	ADD (FOREIGN KEY (m_no) REFERENCES Mart (m_no) ON DELETE SET NULL);

ALTER TABLE Car
	ADD (FOREIGN KEY (m_no) REFERENCES Mart (m_no) ON DELETE SET NULL);

ALTER TABLE sales_emp
	ADD (FOREIGN KEY (e_no) REFERENCES emp (e_no) ON DELETE CASCADE);

ALTER TABLE m_customer
	ADD (FOREIGN KEY (c_no) REFERENCES customer (c_no) ON DELETE CASCADE);

ALTER TABLE m_customer
	ADD (FOREIGN KEY (e_no) REFERENCES sales_emp (e_no) ON DELETE SET NULL);

ALTER TABLE orders
	ADD (FOREIGN KEY (e_no) REFERENCES emp (e_no) ON DELETE SET NULL);

ALTER TABLE orders
	ADD (FOREIGN KEY (c_no) REFERENCES customer (c_no) ON DELETE SET NULL);

ALTER TABLE orders
	ADD (FOREIGN KEY (p_no) REFERENCES product (p_no) ON DELETE SET NULL);

SELECT * FROM TAB;

INSERT INTO MART VALUES(101,'�����Ѱ��Ʈ','����� ������','02-1234-1234');
INSERT INTO MART VALUES(102,'�۵��Ѱ��Ʈ','��õ �۵�','02-1234-1234');
INSERT INTO MART VALUES(103,'�д��Ѱ��Ʈ','��⵵ �д��','02-1234-1234');
INSERT INTO MART VALUES(104,'�ϳ��Ѱ��Ʈ','��⵵ �ϳ���','02-1234-1234');
INSERT INTO MART VALUES(105,'��õ�Ѱ��Ʈ','��⵵ ��õ��','02-1234-1234');


INSERT INTO PRODUCT VALUES(1,'��',100,1000,500);
INSERT INTO PRODUCT VALUES(2,'����',5000,30000,100);
INSERT INTO PRODUCT VALUES(3,'�ȷ�Ʈ',3000,18000,150);
INSERT INTO PRODUCT VALUES(4,'����',50,300,1000);
INSERT INTO PRODUCT VALUES(5,'���찳',100,600,1000);


INSERT INTO CAR VALUES(1555,'����','AA123',1500,TO_DATE('2015-11-07','YYYY-MM-DD'),103);
INSERT INTO CAR VALUES(1556,'����','AA123',1500,TO_DATE('2016-10-07','YYYY-MM-DD'),104);
INSERT INTO CAR VALUES(1557,'���','CC234',1000,TO_DATE('2012-09-07','YYYY-MM-DD'),105);
INSERT INTO CAR VALUES(1558,'����','VV123',2500,TO_DATE('2017-05-07','YYYY-MM-DD'),102);
INSERT INTO CAR VALUES(1559,'����','VV123',2500,TO_DATE('2017-04-07','YYYY-MM-DD'),101);


DESC EMP
INSERT INTO EMP VALUES(1,101,'ȫ�浿','�����',TO_DATE('1980-10-10','YYYY-MM-DD'),'010-1234-5678','�������',3000,4);
INSERT INTO EMP VALUES(2,101,'�迵��','�����',TO_DATE('1980-10-10','YYYY-MM-DD'),'010-1234-5678','����',3300,4);
INSERT INTO EMP VALUES(3,101,'��ö��','�����',TO_DATE('1980-10-10','YYYY-MM-DD'),'010-1234-5678','����',3300,4);
INSERT INTO EMP VALUES(4,101,'�̼���','�����',TO_DATE('1980-10-10','YYYY-MM-DD'),'010-1234-5678','������',4000,null);
INSERT INTO EMP VALUES(5,101,'�嵿��','�����',TO_DATE('1980-10-10','YYYY-MM-DD'),'010-1234-5678','����',3500,4);

INSERT INTO EMP VALUES(6,102,'���ֿ�','��õ �۵�',TO_DATE('1981-05-05','YYYY-MM-DD'),'010-1234-5678','�������',3000,9);
INSERT INTO EMP VALUES(7,102,'��׷�','��õ �۵�',TO_DATE('1981-05-05','YYYY-MM-DD'),'010-1234-5678','����',3300,9);
INSERT INTO EMP VALUES(8,102,'�赿��','��õ �۵�',TO_DATE('1981-05-05','YYYY-MM-DD'),'010-1234-5678','����',3300,9);
INSERT INTO EMP VALUES(9,102,'�̼���','��õ �۵�',TO_DATE('1981-05-05','YYYY-MM-DD'),'010-1234-5678','������',4000,null);
INSERT INTO EMP VALUES(10,102,'��ҿ�','��õ �۵�',TO_DATE('1981-05-05','YYYY-MM-DD'),'010-1234-5678','����',3500,9);

INSERT INTO EMP VALUES(11,103,'����','������ �д�',TO_DATE('1980-07-07','YYYY-MM-DD'),'010-1234-5678','�������',3000,14);
INSERT INTO EMP VALUES(12,103,'õ����','������ �д�',TO_DATE('1980-07-07','YYYY-MM-DD'),'010-1234-5678','����',3300,14);
INSERT INTO EMP VALUES(13,103,'�����','������ �д�',TO_DATE('1980-07-07','YYYY-MM-DD'),'010-1234-5678','����',3300,14);
INSERT INTO EMP VALUES(14,103,'�豸','������ �д�',TO_DATE('1980-07-07','YYYY-MM-DD'),'010-1234-5678','������',4000,null);
INSERT INTO EMP VALUES(15,103,'����','������ �д�',TO_DATE('1980-07-07','YYYY-MM-DD'),'010-1234-5678','����',3500,14);




select * from tab;
desc sales_emp
insert into sales_emp values(2,15,3000000);
insert into sales_emp values(3,15,3000000);
insert into sales_emp values(7,12,2500000);
insert into sales_emp values(8,12,2500000);
insert into sales_emp values(12,10,2400000);
insert into sales_emp values(13,10,2400000);


desc customer
insert into customer values(1,'����',to_date('1832-01-02','YYYY-MM-DD'),'����','����','010-1234-1234');
insert into customer values(2,'��ī��',to_date('1840-03-04','YYYY-MM-DD'),'����','����','010-1234-1234');
insert into customer values(3,'����',to_date('1841-05-21','YYYY-MM-DD'),'����','����','010-1234-1234');
insert into customer values(4,'���',to_date('1832-09-12','YYYY-MM-DD'),'����','����','010-1234-1234');
insert into customer values(5,'�����Ƹ�',to_date('1839-12-01','YYYY-MM-DD'),'����','����','010-1234-1234');
insert into customer values(6,'����',to_date('1834-01-25','YYYY-MM-DD'),'����','����','010-1234-1234');




desc m_customer;
insert into m_customer values(1,2);
insert into m_customer values(2,3);
insert into m_customer values(3,7);
insert into m_customer values(4,7);
insert into m_customer values(5,8);




desc orders
insert into orders values(1,2,1,to_date('2017-11-28','YYYY-MM-DD'),'����',300,300000,1);
insert into orders values(2,2,1,to_date('2017-11-28','YYYY-MM-DD'),'����',60,1800000,2);
insert into orders values(3,3,2,to_date('2017-11-28','YYYY-MM-DD'),'����',100,1800000,3);
insert into orders values(4,7,3,to_date('2017-11-28','YYYY-MM-DD'),'����',100,100000,1);
insert into orders values(5,8,5,to_date('2017-11-28','YYYY-MM-DD'),'����',30,900000,2);



commit;
select * from tab;
SELECT * FROM MART;
SELECT * FROM PRODUCT;
SELECT * FROM CAR;
SELECT * FROM EMP;
select * from sales_emp;
select * from customer;
select * from m_customer;
select * from orders;

select o.o_no "�ֹ���ȣ",o.o_date "�ֹ���¥",o.ship_address "����ּ�",
o.o_cnt "�ֹ���ǰ����",o.o_total "�ֹ��Ѿ�",o.c_no "�ֹ�����ȣ",o.e_no "���������ȣ"
,p.p_no "��ǰ��ȣ",p.p_name "��ǰ��",p.o_price "����",p.c_price "�Һ��ڰ�",p.cnt "���"
from orders o, product p
where o.p_no = p.P_NO and o.c_no = (select c_no from customer where c_name='����');


select e.e_name "�����̸�",sum(nvl(o_total,0)) "������հ�",
se.GOAL_SALES "��ǥ�����"
from orders o, sales_emp se, emp e
where o.e_no(+)=e.E_NO and e.e_no = se.e_no and
e.e_type ='����' and
O_DATE between '17/11/01' and '17/11/30'
group by e.e_name,se.GOAL_SALES
order by sum(nvl(o_total,0)) desc;

select e.e_name, sum(nvl(o_total,0)), se.GOAL_SALES
from sales_emp se, emp e,orders o
where e.e_no = se.e_no and o.e_no(+)=e.e_no
group by e.e_name, se.GOAL_SALES
order by sum(nvl(o_total,0)) desc;