import sqlite3 as sql

class ExecuteSql:
	def __init__(self, conn):
		self.conn = conn
		self.cur = conn.cursor()

	def execute(self, sql, parameters=(), cur=None):
		self.cur = cur if cur != None else self.cur
		return self.cur.execute(sql, parameters)

	def getResult(self, sql, parameters=(), cur=None):
		self.cur = cur if cur != None else self.cur
		return list(self.execute(sql, parameters))

	def getLength(self, sql, parameters=(), cur=None):
		self.cur = cur if cur != None else self.cur
		return len(self.getResult(sql, parameters))

	def commit(self, conn=None):
		self.conn = conn if conn != None else self.conn
		return self.conn.commit()


class Student(ExecuteSql):
	def insert(self, name, sex, sID):
		self.execute(
			'insert into 学生 (姓名, 性别, 学号) values (?, ?, ?)', (name, sex, sID))
		r = self.getResult('select * from 学生 where 学号 = ?', (sID,))
		self.commit()
		return r

	def select(self, index, value):
		indexes = ['ID', '姓名', '性别', '学号']
		return (self.getResult('select * from 学生 where ' + index + ' = ?', (value,)) if index in indexes else [])

	def search(self, index, value):
		indexes = ['ID', '姓名', '性别', '学号']
		return (self.getResult('select * from 学生 where ' + index + ' like ?', (value,)) if index in indexes else [])

	def delete(self, ID):
		r = self.getResult('select * from 学生 where ID = ?', (ID,))
		self.execute('delete from 学生 where ID = ?', (ID,))
		self.commit()
		return r

	def update(self, ID, key, value):
		keys = ['姓名', '性别', '学号']
		if key in keys:
			self.execute('update 学生 set ' + key +
						 ' = ? where ID = ?', (value, ID))
			self.commit()
			r = self.getResult('select * from 学生 where ID = ?', (ID,))
		else:
			r = []
		return r


class Information(ExecuteSql):
	def insert(self, key, value):
		self.execute(
			'insert into 信息 (名称, 值) values (?, ?)', (key, value))
		r = self.getResult('select * from 信息 where 名称 = ?', (key,))
		self.commit()
		return r

	def select(self, index, value):
		indexes = ['ID', '名称']
		return (self.getResult('select * from 信息 where ' + index + ' = ?', (value,)) if index in indexes else [])

	def search(self, index, value):
		indexes = ['ID', '名称']
		return (self.getResult('select * from 信息 where ' + index + ' like ?', (value,)) if index in indexes else [])

	def delete(self, ID):
		r = self.getResult('select * from 信息 where ID = ?', (ID,))
		self.execute('delete from 信息 where ID = ?', (ID,))
		self.commit()
		return r

	def update(self, ID, key, value):
		keys = ['名称', '值']
		if key in keys:
			self.execute('update 信息 set ' + key +
						 ' = ? where ID = ?', (value, ID))
			self.commit()
			r = self.getResult('select * from 信息 where ID = ?', (ID,))
		else:
			r = []
		return r


class Attendance(ExecuteSql):
	def insert(self, sID, time, status):
		self.execute(
			'insert into 考勤 (学号, 时间, 状态) values (?, ?, ?)', (sID, time, status))
		r = self.getResult('select * from 考勤 where 学号 = ?', (sID,))
		self.commit()
		return r

	def select(self, index, value):
		indexes = ['ID', '学号', '时间', '状态']
		return (self.getResult('select * from 考勤 where ' + index + ' = ?', (value,)) if index in indexes else [])

	def search(self, index, value):
		indexes = ['ID', '学号', '时间', '状态']
		return (self.getResult('select * from 考勤 where ' + index + ' like ?', (value,)) if index in indexes else [])

	def delete(self, ID):
		r = self.getResult('select * from 考勤 where ID = ?', (ID,))
		self.execute('delete from 考勤 where ID = ?', (ID,))
		self.commit()
		return r

	def update(self, ID, key, value):
		keys = ['学号', '时间', '状态']
		if key in keys:
			self.execute('update 考勤 set ' + key +
						 ' = ? where ID = ?', (value, ID))
			self.commit()
			r = self.getResult('select * from 考勤 where ID = ?', (ID,))
		else:
			r = []
		return r


class Account(ExecuteSql):
	def insert(self, user, password):
		self.execute(
			'insert into 账户 (名称, 密码) values (?, ?)', (user, password))
		r = self.getResult('select * from 账户 where 名称 = ?', (user,))
		self.commit()
		return r

	def select(self, index, value):
		indexes = ['ID', '名称']
		return (self.getResult('select * from 账户 where ' + index + ' = ?', (value,)) if index in indexes else [])

	def search(self, index, value):
		indexes = ['ID', '名称']
		return (self.getResult('select * from 账户 where ' + index + ' like ?', (value,)) if index in indexes else [])

	def delete(self, ID):
		r = self.getResult('select * from 账户 where ID = ?', (ID,))
		self.execute('delete from 账户 where ID = ?', (ID,))
		self.commit()
		return r

	def update(self, ID, key, value):
		keys = ['名称', '密码']
		if key in keys:
			self.execute('update 账户 set ' + key +
						 ' = ? where ID = ?', (value, ID))
			self.commit()
			r = self.getResult('select * from 账户 where ID = ?', (ID,))
		else:
			r = []
		return r