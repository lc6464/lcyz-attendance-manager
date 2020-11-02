from handles.manager.account import app
from database import student
from flask import session, request
import re, check


@app.route('/student/get', methods=['GET'])
def get_students():
	if check.login(session):
		if 'SID' in request.args:
			r = student.search('学号', request.args['SID'])
			return {'code': 0, 'msg': '获取成功！', 'data': r} if len(r) != 0 else {'code': 2, 'msg': '无数据！'}
		else:
			r = student.search('ID', '%')
			return {'code': 0, 'msg': '获取成功！', 'data': r} if len(r) != 0 else {'code': 2, 'msg': '无数据！'}
	else:
		return {'code': 7, 'msg': '未登录！'}


@app.route('/student', methods=['POST'])
def student_manage():
	if check.login(session):
		if check.sudo(session):
			if 'type' in request.args:
				data = request.form
				t = request.args['type']
				if t == 'insert':
					if 'Name' in data and 'Sex' in data and 'SID' in data:
						r = student.select('学号', data['SID'])
						if len(r) != 0:
							r = r[0]
							return {'code': 5, 'msg': '学号为%s的%s同学 %s 已存在！'%(r[3], r[2], r[1])}
						else:
							if re.match(r'.{2,10}', data['Name']) != None and data['Sex'] in ['男', '女'] and len(data['SID']) == 10:
								r = student.insert(data['Name'], data['Sex'], data['SID'])[0]
								return {'code': 0, 'msg': '%s 同学添加成功！\\r\\nID：%s\\r\\n性别：%s\\r\\n学号：%s' % (r[1], r[0], r[2], r[3])}
							else:
								return {'code': 6, 'msg': '数据不合法！'}
					else:
						return {'code': 3, 'msg': '数据不合法！'}
				elif t == 'update':
					if 'ID' in data and 'Name' in data and 'Sex' in data and 'SID' in data:
						r = student.select('ID', data['ID'])
						if len(r) == 0:
							return {'code': 2, 'msg': 'ID为%s的同学不存在！' % data['ID']}
						else:
							if re.match(r'.{2,10}', data['Name']) != None and data['Sex'] in ['男', '女'] and len(data['SID']) == 10:
								student.update(data['ID'], '姓名', data['Name'])
								student.update(data['ID'], '性别', data['Sex'])
								r = student.update(data['ID'], '学号', data['SID'])[0]
								return {'code': 0, 'msg': '%s 同学修改成功！\\r\\nID：%s\\r\\n性别：%s\\r\\n学号：%s' % (r[1], r[0], r[2], r[3])}
							else:
								return {'code': 6, 'msg': '数据不合法！'}
					else:
						return {'code': 3, 'msg': '数据不合法！'}
				elif t == 'remove':
					if 'ID' in data:
						r = student.select('ID', data['ID'])
						if len(r) == 0:
							return {'code': 2, 'msg': 'ID为%s的同学不存在！' % data['ID']}
						else:
							r = student.delete(data['ID'])[0]
							return {'code': 0, 'msg': '已删除 %s 同学！\\r\\nID：%s\\r\\n性别：%s\\r\\n学号：%s' % (r[1], r[0], r[2], r[3])}
					else:
						return {'code': 3, 'msg': '数据不合法！'}
				else:
					return {'code': 9, 'msg': '选定的功能不合法！'}
			else:
				return {'code': 9, 'msg': '未选定功能！'}
		else:
			return {'code': 8, 'msg': '敏感操作验证！'}
	else:
		return {'code': 7, 'msg': '未登录！'}