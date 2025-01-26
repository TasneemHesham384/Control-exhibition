from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  
app.config['MYSQL_PASSWORD'] = 'tasneem'  
app.config['MYSQL_DB'] = 'votingsystem'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM votes')
    projects = cur.fetchall()
    cur.close()
    return render_template('index.html', projects=projects)

@app.route('/vote', methods=['POST'])
def vote():
    project_id = request.form['project_id']
    cur = mysql.connection.cursor()

    cur.execute('UPDATE votes SET votecount = votecount + 1 WHERE id = %s', (project_id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)