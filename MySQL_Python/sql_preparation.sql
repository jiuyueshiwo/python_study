mysql -hlocalhost -uroot -pMySQL_666
show databases;
create database jing_dong charset=utf8;
use jing_dong;
create table goods(
	id int unsigned primary key auto_increment not null,
	name varchar(150) not null,
	cate_id int unsigned not null,
	brand_id int unsigned not null,
	price decimal(10, 3) not null default 0,
	is_show bit not null default 1,
	is_saleoff bit not null default 0
);


--商品分类表
create table if not exists goods_cates(
    id int unsigned primary key auto_increment not null,
    name varchar(40) not null
);
insert into goods_cates(name) values ("笔记本"), ("游戏本"), ("超级本"), ("平板电脑"), ("台式机"), ("服务器/工作站"), ("笔记本配件");

--商品品牌表
create table goods_brands (
    id int unsigned primary key auto_increment not null,
    name varchar(40) not null
);
insert into goods_brands(name) values ("华硕"), ("联想"), ("雷神"), ("索尼"), ("苹果"), ("戴尔"), ("宏碁"), ("惠普"), ("ibm");

--订单表
create table orders(
	id int unsigned primary key auto_increment not null,
	order_date_time datetime not null,
	customer_id int unsigned not null
);

--顾客表
create table customers(
	id int unsigned primary key auto_increment not null,
	name varchar(40) not null,
	address varchar(150) not null,
	tel varchar(11) not null,
	passwd varchar(20) not null
);

--订单详情表
create table order_detail(
	id int unsigned primary key auto_increment not null,
	order_id int unsigned not null,
	good_id int unsigned not null,
	quantity int unsigned not null
);













--插入数据
insert into goods values(0,'r510vc 15.6英寸笔记本',1,1,'3399',default,default); 
insert into goods values(0,'y400n 14.0英寸笔记本电脑',1,2,'4999',default,default);
insert into goods values(0,'g150th 15.6英寸游戏本',2,3,'8499',default,default); 
insert into goods values(0,'x550cc 15.6英寸笔记本',1,1,'2799',default,default); 
insert into goods values(0,'x240 超极本',3,2,'4880',default,default); 
insert into goods values(0,'u330p 13.3英寸超极本',3,2,'4299',default,default); 
insert into goods values(0,'svp13226scb 触控超极本',3,4,'7999',default,default); 
insert into goods values(0,'ipad mini 7.9英寸平板电脑',4,5,'1998',default,default);
insert into goods values(0,'ipad air 9.7英寸平板电脑',4,5,'3388',default,default); 
insert into goods values(0,'ipad mini 配备 retina 显示屏',4,5,'2788',default,default); 
insert into goods values(0,'ideacentre c340 20英寸一体电脑 ',5,2,'3499',default,default); 
insert into goods values(0,'vostro 3800-r1206 台式电脑',5,6,'2899',default,default); 
insert into goods values(0,'imac me086ch/a 21.5英寸一体电脑',5,5,'9188',default,default); 
insert into goods values(0,'at7-7414lp 台式电脑 linux ）',5,7,'3699',default,default); 
insert into goods values(0,'z220sff f4f06pa工作站',6,8,'4288',default,default); 
insert into goods values(0,'poweredge ii服务器',6,6,'5388',default,default); 
insert into goods values(0,'mac pro专业级台式电脑',6,5,'28888',default,default); 
insert into goods values(0,'hmz-t3w 头戴显示设备',7,4,'6999',default,default); 
insert into goods values(0,'商务双肩背包',7,4,'99',default,default); 
insert into goods values(0,'x3250 m4机架式服务器',6,9,'6888',default,default); 
insert into goods values(0,'商务双肩背包',7,4,'99',default,default);