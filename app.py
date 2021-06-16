from flask import Flask,render_template,request
import sqlite3





app = Flask(__name__)


@app.route('/enter',methods=['POST'])
def enter():
   if request.method == 'POST':
       try:
           name=request.form['name']
           city=request.form['city']
           conn =sqlite3.connect('test.db')
           cur=conn.cursor()
           cur.execute("INSERT INTO STUDENT (NAME,CITY) VALUES(?,?)",(name,city))
           conn.commit()
           msg ="Data saved successfully"
       except:
           conn.rollback()
           msg ="Data not saved "

       finally:
           return render_template('msg.html',msg=msg)

@app.route('/')
def create():
   return render_template('enter.html')



















if __name__ == '__main__':
    app.run(debug=True)