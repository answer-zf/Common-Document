# MySQL语法



## 数据类型

```mysql

varchar 	可变字符长度（灵活性高）

char     	固定字符长度（效率高），字符不够，在后面补空格，直到字符长度与固定长度一样长。


			字符集：	 utf8
			排序规则：	utf8_general_ci
			
```



## MySQL 语法

```shell

## SQL语句是一套公共的标准，不同的数据库之间都可以执行，只不过有特性.

## select 语句可以选择列或者一个具体的值;

## 查询数据语句得到的是结果集;
## 增删改语句得到的是执行这个语句受影响的行数;

## delete 语句要配合where使用，否则删除一个字段（ 表单 ）；

## 查询总条数select count(1) as count from user;

## 子语句：

where 

	...where id = 6 and gender in (0,2);
	...where id > 6 or gender = 0;

limit     ##数据分页

	..limit <skip>, <length>;


		## 限制取几条

		select * from user limit 2;

		## 限制越过几条取几条；

		select * from user limit 2, 2;

		skip = (page-1) * length;(page:页面;length :每页数量);

## 示例：

$ select id,title, name from user;
$ select `id`,`title`, `name` from `user`;
$ select * from `user`;
$ select 1 from `user`;
$ insert into user values (null, 'CEO', 'sdf', 18, 0);
$ insert into user (name, title, age, gender) value ('CEO', 'sdf', 18, 0);
$ delete from user where id = '4' ;
$ select * from `user` where id > 3;
$ update users set name = '麻子', gender = 0
```



## 联合查询

```mysql

select 
	posts.id,
	posts.title,
	users.nickname as users_name,
	categories.`name` as category_name,
	posts.created,
	posts.`status`
from posts
inner join categories on posts.category_id = categories.id 
inner join users on posts.user_id = users.id 

## as 字段重新命名   
## on 声明 所联合的关系

```



## 分页查询

```mysql

 select 
   posts.id,
   posts.title,
   users.nickname as users_name,
   categories.`name` as category_name,
   posts.created,
  posts.`status`
 from posts
 inner join categories on posts.category_id = categories.id 
 inner join users on posts.user_id = users.id
 order by posts.created desc
 limit 0,10
 
 ## order by  以某字段排序  desc降序 asc升序
 
```

