from handles.static import app, check
from flask import render_template, redirect, session
from database import student, information, attendance, account

@app.route('/')
def index():
	if check.login(session):
		return render_template('index.html', user=session['user'])
	else:
		return redirect('/login')


@app.route('/student')
def student_manager():
	if check.login(session):
		return render_template('manager/student.html')
	else:
		return redirect('/login?r=/student')


@app.route('/account')
def account_manager():
	if check.login(session):
		return render_template('manager/account.html')
	else:
		return redirect('/login?r=/account')


@app.route('/attendance/register')
def register():
	if check.login(session):
		return render_template('manager/register.html')
	else:
		return redirect('/login?r=/attendance/register')


@app.route('/attendance/record')
def record():
	if check.login(session):
		return render_template('manager/record.html')
	else:
		return redirect('/login?r=/attendance/record')