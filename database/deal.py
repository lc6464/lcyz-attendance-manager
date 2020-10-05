from database.classes import Student, Information, Attendance, Account
from database.pretreatment import er

student = Student(er.conn)
information = Information(er.conn)
attendance = Attendance(er.conn)
account = Account(er.conn)