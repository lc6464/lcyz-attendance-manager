from database.classes import ExecuteSql, sql
import sys
sys.path.append('..')
import config
er = ExecuteSql(sql.connect(config.database, check_same_thread=False))