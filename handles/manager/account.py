from sys import path
path.append('..')
from handles.error import app
from database import account
from flask import session, request
import check

@app.route('/account/get', methods=['GET'])
def get_account():
	if check.login(session):
		if 'Account' in request.args:
			r = account.search('名称', request.args['Account'])
			return {'code': 0, 'msg': '账号存在！'} if len(r) != 0 else {'code': 2, 'msg': '账号不存在！'}
		else:
			return {'code': 3, 'msg': '未传入账号！'}
	else:
		return {'code': 7, 'msg': '未登录！'}


@app.route('/logout', methods=['GET'])
def logout():
	if check.login(session):
		session.pop('user', None)
		session.pop('password', None)
		session.pop('sudo', None)
		return {'code': 0, 'msg': '退出登录成功！'}
	else:
		return {'code': 5, 'msg': '未登录！无需退出登录！'}


@app.route('/account', methods=['POST'])
def account_manage():
	if check.login(session):
		if 'type' in request.args:
			data = request.form
			t = request.args['type']
			if t == 'changePassword':
				if 'Password' in data and 'NewPassword' in data:
					r = account.select('名称', session['user'])
					if len(r) != 0:
						r = r[0]
						if data['Password'] == r[2]:
							account.update(r[0], '密码', data['NewPassword'])
							return {'code': 0, 'msg': '修改密码成功！'}
						else:
							return {'code': 1, 'msg': '旧密码错误！'}
					else:
						return {'code': 2, 'msg': '账户不存在！'}
				else:
					return {'code': 3, 'msg': '数据不合法！'}
			elif t == 'newAccount':
				if 'Password' in data and 'NewAccount' in data and 'NewPassword' in data:
					r = account.select('名称', session['user'])
					if len(r) != 0:
						r = r[0]
						if data['Password'] == r[2]:
							account.insert(data['NewAccount'], data['NewPassword'])
							return {'code': 0, 'msg': '创建账户 %s 成功！' % data['NewAccount']}
						else:
							return {'code': 1, 'msg': '当前账户密码错误！'}
					else:
						return {'code': 2, 'msg': '当前账户不存在！'}
				else:
					return {'code': 3, 'msg': '数据不合法！'}
			elif t == 'removeAccount':
				if 'Password' in data:
					r = account.select('名称', session['user'])
					if len(r) != 0:
						r = r[0]
						if data['Password'] == r[2]:
							account.delete(r[0])
							session.pop('user', None)
							session.pop('password', None)
							session.pop('sudo', None)
							return {'code': 0, 'msg': '删除账户 %s 成功！' % r[1]}
						else:
							return {'code': 1, 'msg': '当前账户密码错误！'}
					else:
						return {'code': 2, 'msg': '当前账户不存在！'}
				else:
					return {'code': 3, 'msg': '数据不合法！'}
			else:
				return {'code': 9, 'msg': '选定的功能不合法！'}
		else:
			return {'code': 9, 'msg': '未选定功能！'}
	else:
		return {'code': 7, 'msg': '未登录！'}