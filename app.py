from flask import Flask, render_template, flash, redirect, url_for, session, request, logging

'''
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, validators
from passlib.hash import sha256_crypt
from functools import wraps

#Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
'''

app = Flask(__name__)


#Register
@app.route('/register')
def register():
	return render_template("register.html")


#Login
@app.route('/login', methods=('GET', 'POST'))
def login():

	"""if request.method == 'POST':
		#Get form fields
		username = request.form['username']
		password_candidate = request.form['password']

		#Create Cursor
		cur = mysql.connection.cursor()

		#Get user by username
		result = cur.execute("SELECT * FROM users WHERE username == %s, [username]")

		if result > 0:
			#Get stored hash
			data = cur.fetchone()
			password = data['password']

			if sha256_crypt.verify(password_candidate, pasword):
				app.loger.info('PASSWORD MATCHED')
			else:
				app.logger.info("NO USER")"""



	return render_template("login.html")

if __name__ == '__main__':
	app.run(debug=True)