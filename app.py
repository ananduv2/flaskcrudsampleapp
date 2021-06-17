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
def contact():
   conn =sqlite3.connect('test.db')
   conn.row_factory = sqlite3.Row
   cur=conn.cursor()
   cur.execute("SELECT * FROM STUDENT")
   rows = cur.fetchall()
   return render_template("list.html",rows = rows)



@app.route('/edit/<id>')
def edit(id):
    conn =sqlite3.connect('test.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM STUDENT WHERE ID=(?)",(id))
    rows = cur.fetchone()
    return render_template("edit.html",id=rows[0],name=rows[1],city=rows[2])


@app.route('/update/<id>',methods=['POST','GET'])
def update(id):
    sid=id
    name=request.form['name']
    city=request.form['city']
    try:
        conn =sqlite3.connect('test.db')
        cur=conn.cursor()
        cur.execute("UPDATE STUDENT SET NAME=(?),CITY=(?) WHERE ID=(?) ",(name,city,sid))
        conn.commit()
        msg="Updated successfully"
    except:
        conn.rollback()
        msg ="Updation failed"
    finally:
        return render_template('msg.html',msg=msg)


@app.route('/delete/<id>')
def delete(id):
   sid=id
   try:
        conn =sqlite3.connect('test.db')
        cur=conn.cursor()
        cur.execute("DELETE FROM STUDENT WHERE ID=(?) ",(sid))
        conn.commit()
        msg="Deleted successfully"
   except:
        conn.rollback()
        msg ="Deletion failed"
   finally:
        return render_template('msg.html',msg=msg)

   


@app.route('/create')
def create():
   return render_template('enter.html')







if __name__ == '__main__':
    app.run(debug=True)