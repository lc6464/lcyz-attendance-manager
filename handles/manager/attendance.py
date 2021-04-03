from handles.manager.account import app
from database import attendance, student
from flask import session, request
from time import strftime
import re, check

@app.route('/attendance/get', methods=['GET'])
def attendance_get():
	if check.login(session):
		if 'SID' in request.args:
			r = attendance.search('学号', request.args['SID'])
			return {'code': 0, 'msg': '获取成功！', 'data': r} if len(r) != 0 else {'code': 2, 'msg': '无数据！'}
		else:
			r = attendance.search('ID', '%')
			return {'code': 0, 'msg': '获取成功！', 'data': r} if len(r) != 0 else {'code': 2, 'msg': '无数据！'}
	else:
		return {'code': 7, 'msg': '未登录！'}


@app.route('/attendance/insert', methods=['POST'])
def attendance_insert():
	if check.login(session):
		if check.sudo(session):
			data = request.form
			if 'SID' in data and 'Status' in data:
				if data['Status'] in ['i', 'o']:
					if student.select('学号', data['SID']) != []:
						attendance.insert(data['SID'], strftime('%Y-%m-%dT%H:%M:%S+08:00'), data['Status'])
						return {'code': 0, 'msg': '%s 记录成功！' % data['SID']}
					else:
						return {'code': 2, 'msg': '学号为“%s”的学生不存在！'%data['SID']}
				else:
					return {'code': 6, 'msg': '数据不合法！'}
			else:
				return {'code': 3, 'msg': '数据不合法！'}
		else:
			return {'code': 8, 'msg': '敏感操作验证！'}
	else:
		return {'code': 7, 'msg': '未登录！'}