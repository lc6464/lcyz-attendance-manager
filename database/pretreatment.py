from database.openDatabase import er
er.execute('create table if not exists 信息 (ID INTEGER PRIMARY KEY AUTOINCREMENT, 名称 varchar(16) unique not null, 值 varchar(64) not null)')
er.execute('create table if not exists 学生 (ID INTEGER PRIMARY KEY AUTOINCREMENT, 姓名 varchar(10) not null, 性别 char(1) not null, 学号 char(10) unique not null)')
er.execute('create table if not exists 考勤 (ID INTEGER PRIMARY KEY AUTOINCREMENT, 学号 char(10) unique not null, 时间 char(20) not null, 状态 char(1) not null)')
er.execute('create table if not exists 账户 (ID INTEGER PRIMARY KEY AUTOINCREMENT, 名称 varchar(32) unique not null, 密码 varchar(64) not null)')
er.commit()