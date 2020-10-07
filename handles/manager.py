from handles.error import app, check
from flask import request, session
from database import student, information, attendance, account
import re, time

@app.route('/sudo', methods=['POST'])
def sudo():
	if check.login(session):
		if check.sudo(session):
			return {'code': 5, 'msg': '已经验证过！无需再次验证！'}
		elif 'Password' in request.form:
			if request.form['Password'] == session['password']:
				session['sudo'] = time.time()
				return {'code': 0, 'msg': '验证成功！'}
			else:
				return {'code': 1, 'msg': '密码错误！'}
		else:
			return {'code': 3, 'msg': '请输入密码！'}
	else:
		return {'code': 7, 'msg': '未登录！'}


@app.route('/student/insert', methods=['POST'])
def student_insert():
	if check.login(session):
		if check.sudo(session):
			data = request.form
			if 'Name' in data and 'Sex' in data and 'SID' in data:
				r = student.select('学号', data['SID'])
				if len(r) != 0:
					r = r[0]
					return {'code': 5, 'msg': '学号为“%s”的%s同学“%s”已存在！'%(r[3], r[2], r[1])}
				else:
					if re.match(r'.{2,10}', data['Name']) != None and data['Sex'] in ['男', '女'] and len(data['SID']) == 10:
						r = student.insert(data['Name'], data['Sex'], data['SID'])[0]
						return {'code': 0, 'msg': r'ID 为“%s”的“%s”同学添加成功！性别：%s，学号：%s。' % r}
					else:
						return {'code': 6, 'msg': '数据不合法！'}
			else:
				return {'code': 3, 'msg': '数据不合法！'}
		else:
			return {'code': 8, 'msg': '敏感操作验证！'}
	else:
		return {'code': 7, 'msg': '未登录！'}


@app.route('/student/get', methods=['GET'])
def student_get_all():
	if check.login(session):
		r = student.search('ID', '%')
		return {'code': 0, 'msg': '获取成功！', 'data': r} if len(r) != 0 else {'code': 2, 'msg': '无数据！'}
	else:
		return {'code': 7, 'msg': '未登录！'}


@app.route('/student/update', methods=['POST'])
def student_update():
	if check.login(session):
		if check.sudo(session):
			data = request.form
			if 'ID' in data and 'Name' in data and 'Sex' in data and 'SID' in data:
				r = student.select('ID', data['ID'])
				if len(r) == 0:
					return {'code': 2, 'msg': 'ID为“%s”的同学不存在！' % data['ID']}
				else:
					if re.match(r'.{2,10}', data['Name']) != None and data['Sex'] in ['男', '女'] and len(data['SID']) == 10:
						student.update(data['ID'], '姓名', data['Name'])
						student.update(data['ID'], '性别', data['Sex'])
						r = student.update(data['ID'], '学号', data['SID'])[0]
						return {'code': 0, 'msg': r'ID 为“%s”的“%s”同学修改成功！性别：%s，学号：%s。' % r}
					else:
						return {'code': 6, 'msg': '数据不合法！'}
			else:
				return {'code': 3, 'msg': '数据不合法！'}
		else:
			return {'code': 8, 'msg': '敏感操作验证！'}
	else:
		return {'code': 7, 'msg': '未登录！'}