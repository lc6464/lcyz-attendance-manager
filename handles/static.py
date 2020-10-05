from handles.manager import app, check
from flask import abort, send_file

@app.route('/favicon.ico')
def favicon():
	return send_file('web/resources/icon.ico')


@app.route('/favicon.svg')
def faviconSvg():
	return send_file('web/resources/icon.svg')


@app.route('/error/static/<path:file>')
def error_static_file(file):
	try:
		return send_file('web/errorPages/static/' + file)
	except IOError:
		return abort(404)