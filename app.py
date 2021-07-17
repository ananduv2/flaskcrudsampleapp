from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__)

#code to create student data
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

@app.route('/create')
def create():
   return render_template('enter.html')

#code to list student data
@app.route('/')
def contact():
   conn =sqlite3.connect('test.db')
   conn.row_factory=sqlite3.Row
   cur=conn.cursor()
   cur.execute("SELECT * FROM STUDENT")
   rows= cur.fetchall()
   return render_template('index.html',rows=rows)

#code to edit student data
@app.route('/edit/<id>')
def edit(id):
    sid = id
    conn =sqlite3.connect('test.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM STUDENT WHERE ID =(?)",[sid])
    rows = cur.fetchone()
    cid=rows[0]
    name=rows[1]
    city=rows[2]
    return render_template('edit.html',id=cid,name=name,city=city)

@app.route('/update/<id>',methods=['POST'])
def update(id):
   sid=id
   name=request.form['name']
   city=request.form['city']
   try:
       conn =sqlite3.connect('test.db')
       cur=conn.cursor()
       cur.execute("UPDATE STUDENT SET NAME=(?),CITY=(?) WHERE ID=(?)",(name,city,sid))
       conn.commit()
       msg="Updated successfully"
   except:
       conn.rollback()
       msg="Updation failed"
   finally:
       return render_template('msg.html',msg=msg)


#code to delete student data
@app.route('/delete/<id>')
def delete(id):
   conn =sqlite3.connect('test.db')
   cur=conn.cursor()
   cur.execute("DELETE FROM STUDENT WHERE ID=(?)",(id))
   conn.commit()
   msg="Deletion successfully"
   return render_template('msg.html',msg=msg)



if __name__ == '__main__':
    app.run(debug=True)