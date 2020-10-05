from flask import Flask
import config

app = Flask(__name__)
app.secret_key = config.secret_key
app.config['PERMANENT_SESSION_LIFETIME'] = config.session_lifttime
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = config.cache_max_age
app.debug = config.debug