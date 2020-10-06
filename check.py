import re, time
from database import student, information, attendance, account

def password(password):
	return re.match(r'(?!^((\d+)|([A-Z]+)|([a-z]+)|([\\_#@\-=+/*$%^&()[\]{};:\'"?<>,.`~!|]+)|([\dA-Z]+)|([\da-z]+)|([\d\\_#@\-=+/*$%^&()[\]{};:\'"?<>,.`~!|]+)|([A-Za-z]+)|([A-Z\\_#@\-=+/*$%^&()[\]{};:\'"?<>,.`~!|]+)|([a-z\\_#@\-=+/*$%^&()[\]{};:\'"?<>,.`~!|]+))$)^[\da-zA-Z\\_#@\-=+/*$%^&()[\]{};:\'"?<>,.`~!|]{8,64}$', password) != None


def login(session):
	if 'user' in session and 'password' in session:
		acc = account.select('名称', session['user'])
		if len(acc) == 1:
			if acc[0][2] == session['password']:
				return True
	session.pop('user', None)
	session.pop('password', None)
	return False

def sudo(session):
	if 'sudo' in session:
		if time.time() - session['sudo'] <= 1800:
			session['sudo'] = time.time()
			return True
	session.pop('sudo', None)
	return False
