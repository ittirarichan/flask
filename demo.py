from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
import sqlite3

con=sqlite3.connect('database.db')
try:
    con.execute('create table user (name text,age int)')
except:
    pass

@app.route('/')
def view_data():
    con = sqlite3.connect("database/form.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()
    return render_template('demo.html',rows=rows)

@app.route('/',methods=['POST','GET'])
def fun1():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        con=sqlite3.connect('database/form.db')
        con.execute("insert into user(name,age)values(?,?)",(name,age))
        con.commit()
        print(name,age)
        return redirect(url_for('fun1'))
    else:
        return render_template('demo.html')


app.run()


