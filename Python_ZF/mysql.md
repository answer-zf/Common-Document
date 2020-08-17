```mysql
create table teacher(
id int primary key,
tname varchar(20),
level varchar(20)
)charset=utf8;
insert into teacher values (1,'zf','S'),(2,'cf','D');

create table course(
id int primary key,
cname varchar(20),
score int
)charset=utf8;
insert into course values (1,'HTML',5),(2,'Spider',5),(3,'MySQL',3);

create table middel(
id int primary key auto_increment,
t_id int,
c_id int,
foreign key (t_id)
references teacher(id),
foreign key (c_id)
references course(id)
)charset=utf8;
insert into middel values(1,1,1),(2,1,3),(3,2,1),(4,2,2),(5,2,3);

select teacher.tname,course.cname from course
inner join middel on course.id=middel.c_id
inner join teacher on teacher.id=middel.t_id
where teacher.tname='zf';

select teacher.tname,course.cname from teacher
inner join middel on teacher.id=middel.t_id
inner join course on course.id=middel.c_id
where teacher.tname='zf';
























```

