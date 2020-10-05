from handles.error import app, check
from flask import request, session
from database import student, information, attendance, account
import re

@app.route('/student/insert', methods=['POST'])
def student_insert():
	if check.login(session):
		data = request.form
		if 'Name' in data and 'Sex' in data and 'SID' in data:
			if len(student.select('学号', data['SID'])) != 0:
				return {'code': 5, 'msg': '此学生已存在！'}
			else:
				if re.match(r'.{2,10}', data['Name']) != None and data['Sex'] in ['男', '女'] and len(data['SID']) == 10:
					r = student.insert(data['Name'], data['Sex'], data['SID'])[0]
					return {'code': 0, 'msg': r'ID 为 %s 的 %s 同学添加成功！\r\n性别：%s\t学号：%s' % r}
				else:
					return {'code': 6, 'msg': '数据不合法！'}
		else:
			return {'code': 3, 'msg': '数据不合法！'}
	else:
		return {'code': 7, 'msg': '未登录！'}