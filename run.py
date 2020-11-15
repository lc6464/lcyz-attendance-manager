import config, click, sys

@click.command()
@click.option("--host", '-h', default=config.host, help="The domain the server listen.\r\nDefault: %s"%config.host, type=click.STRING)
@click.option("--port", '-p', default=config.port, help="The port the server listen.\r\nDefault: %s"%config.port, type=click.INT)
@click.option("--debug", '-d', default=config.debug, help="Enable server debugging mode.\r\nDefault: %s"%config.debug, type=click.BOOL)
@click.option("--secret_key", '-k', default=config.secret_key, help="Session secret key.\r\nDefault: %s"%config.secret_key, type=click.STRING)
@click.option("--cache_max_age", '-c', default=config.cache_max_age, help="Static file cache max age (seconds).\r\nDefault: %s"%config.cache_max_age, type=click.INT)
@click.option("--session_lifttime", '-l', default=config.session_lifttime, help="Session cookie lift time (days).\r\nDefault: %s"%config.session_lifttime, type=click.INT)
def run(host='', port=0, debug=False, secret_key='dev', cache_max_age=0, session_lifttime=0):
	if not ('--help' in sys.argv):
		from handles import app
		from datetime import timedelta
		app.secret_key = secret_key
		app.config['SEND_FILE_MAX_AGE_DEFAULT'] = cache_max_age
		app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=session_lifttime)
		if debug:
			if not click.confirm('Warning: Are you sure to enable server debugging mode? This will be very dangerous!', False, False):
				debug = False
		app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
	run()