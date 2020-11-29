import re, time
from database import student, information, attendance, account
from session import Session

def password(password):
	return re.match(r'(?!^((\d+)|([A-Z]+)|([a-z]+)|([\\_#@\-=+/*$%^&()[\]{};:\'"?<>,.`~!|]+)|([\dA-Z]+)|([\da-z]+)|([\d\\_#@\-=+/*$%^&()[\]{};:\'"?<>,.`~!|]+)|([A-Za-z]+)|([A-Z\\_#@\-=+/*$%^&()[\]{};:\'"?<>,.`~!|]+)|([a-z\\_#@\-=+/*$%^&()[\]{};:\'"?<>,.`~!|]+))$)^[\da-zA-Z\\_#@\-=+/*$%^&()[\]{};:\'"?<>,.`~!|]{8,64}$', password) != None


def login(session):
	if 'uuid' in session:
		r = Session.Get(session['uuid'])
		if len(r) == 3:
			_session = r[2]
		else:
			_session = {}
		if 'password' in _session:
			acc = account.select('名称', r[1])
			if len(acc) == 1:
				if acc[0][2] == _session['password']:
					return True
		Session.Remove(session['uuid'])
		session.pop('uuid', None)
	return False

def sudo(session):
	r = Session.Get(session['uuid'])
	if len(r) == 3:
		_session = r[2]
	else:
		_session = {}
	if 'sudo' in _session:
		if time.time() - _session['sudo'] <= 1800:
			_session['sudo'] = time.time()
			Session.Set(session['uuid'], _session)
			return True
	_session.pop('sudo', None)
	Session.Set(session['uuid'], _session)
	return False
