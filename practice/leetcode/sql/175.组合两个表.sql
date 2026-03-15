Create table If Not Exists Person (personId int, firstName varchar(255), lastName varchar(255));
Create table If Not Exists Address (addressId int, personId int, city varchar(255), state varchar(255));
Truncate table Person;
insert into Person (personId, lastName, firstName) values ('1', 'Wang', 'Allen');;
insert into Person (personId, lastName, firstName) values ('2', 'Alice', 'Bob');;
Truncate table Address;
insert into Address (addressId, personId, city, state) values ('1', '2', 'New York City', 'New York');
insert into Address (addressId, personId, city, state) values ('2', '3', 'Leetcode', 'California');


select * from person;
select * from address;

-- 编写解决方案，报告 Person 表中每个人的姓、名、城市和州。如果 personId 的地址不在 Address 表中，则报告为 null 。

-- 以 任意顺序 返回结果表。

-- 题目分析：
-- 报告Person表中每个人的姓，名 -- 说明要提取person中的所有数据
-- personid不再address中，则报告为null，典型的left join，匹配不到就显示null

select 
    p.firstName, p.lastName, a.city, a.state
from person p
left join address a
on p.personid = a.personid;