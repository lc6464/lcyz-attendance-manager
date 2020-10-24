from handles.static import app, check
from flask import render_template, redirect, session
from database import student, information, attendance, account

@app.route('/', methods=['GET'])
def index():
	if check.login(session):
		return render_template('index.html', user=session['user'])
	else:
		return redirect('/login')


@app.route('/student', methods=['GET'])
def student_manager():
	if check.login(session):
		return render_template('manager/student.html')
	else:
		return redirect('/login?r=/student')


@app.route('/account', methods=['GET'])
def account_manager():
	if check.login(session):
		return render_template('manager/account.html')
	else:
		return redirect('/login?r=/account')


@app.route('/attendance/register', methods=['GET'])
def register():
	if check.login(session):
		return render_template('manager/register.html')
	else:
		return redirect('/login?r=/attendance/register')


@app.route('/attendance/record', methods=['GET'])
def record():
	if check.login(session):
		return render_template('manager/record.html')
	else:
		return redirect('/login?r=/attendance/record')