from sys import path
path.append('..')
from app import app
from flask import send_file
import check

@app.errorhandler(404)
def not_found(e):
	return send_file('web/errorPages/404.html'), 404


@app.errorhandler(405)
def method_not_allowed(e):
	return send_file('web/errorPages/405.html'), 405


@app.errorhandler(500)
def internal_server_error(e):
	return send_file('web/errorPages/500.html'), 500