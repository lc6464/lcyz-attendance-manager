from handles.manager.student import app, check
from flask import request, session
import time
from session import Session

@app.route('/sudo', methods=['POST'])
def sudo():
	if check.login(session):
		if check.sudo(session):
			return {'code': 5, 'msg': '已经验证过！无需再次验证！'}
		elif 'Password' in request.form:
			r = Session.Get(session['uuid'])
			if request.form['Password'] == r[2]['password']:
				r[2]['sudo'] = time.time()
				Session.Set(session['uuid'], r[2])
				return {'code': 0, 'msg': '验证成功！'}
			else:
				return {'code': 1, 'msg': '密码错误！'}
		else:
			return {'code': 3, 'msg': '请输入密码！'}
	else:
		return {'code': 7, 'msg': '未登录！'}