from handles.templates import app, check
from flask import request, session, redirect, render_template
from database import student, information, attendance, account
from session import Session

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		if check.login(session):
			return {'code': 5, 'msg': '已经登录过！无需再次登录！'}
		else:
			if not ('User' in request.form and 'Password' in request.form):
				return {'code': 3, 'msg': '请输入账号密码！'}
			user = request.form['User']
			password = request.form['Password']
			if user != None and password != None and user != '' and password != '':
				result = account.select('名称', user)
				if len(result) == 1:
					if result[0][2] == password:
						session.permanent = True
						r = Session.Add(user)[0]
						session['uuid'] = r
						Session.Set(r, {'password': password})
						return {'code': 0, 'msg': '登录成功！'}
					else:
						return {'code': 1, 'msg': '用户名或密码错误！'}
				else:
					return {'code': 2, 'msg': '用户不存在！'}
			else:
				return {'code': 3, 'msg': '请输入账号密码！'}
	else:
		r = request.args['r'] if 'r' in request.args else '/'
		if check.login(session):
			return redirect(r)
		return render_template('login.html', redirect=r)


@app.route('/config', methods=['GET', 'POST'])
def first_config():
	if request.method == 'POST':
		if len(account.search('ID', '%')) == 0:
			if not ('User' in request.form and 'Password' in request.form):
				return {'code': 3, 'msg': '请输入账号密码！'}
			user = request.form['User']
			password = request.form['Password']
			if user != None and password != None and user != '' and password != '':
				if check.password(password):
					session.permanent = True
					r = Session.Add(user)[0]
					session['uuid'] = r
					Session.Set(r, {'password': password})
					return {'code': 0, 'msg': '“%s” 创建成功！请牢记账号密码！' % account.insert(request.form['User'], request.form['Password'])[0][1]}
				else:
					return {'code': 4, 'msg': '密码过于简单！'}
			else:
				return {'code': 3, 'msg': '请输入账号密码！'}
		else:
			return {'code': 5, 'msg': '已经创建过账户，请直接登录！'}
	else:
		r = request.args['r'] if 'r' in request.args else '/'
		if len(account.search('ID', '%')) == 0:
			return render_template('first_config.html', redirect=r)
		else:
			return redirect('/login')