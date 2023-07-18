from flask import *
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="Titanic"
app.config['MYSQL_CURSORCLASS']="DictCursor"
mysql=MySQL(app)
@app.route('/')
def home():
    return render_template('library.html')
@app.route('/au')
def au():
    return render_template('ADDUSER.html')
#edit user
@app.route('/eu/<string:id>',methods=['GET','POST'])
def edituser(id):
    con = mysql.connection.cursor()
    con.execute("select * from user where user_id=%s;",id)
    r=con.fetchone()
    con.close()
    return render_template('edituser.html',id=r)
#edit trans
@app.route('/et/<string:id>',methods=['GET','POST'])
def edittrans(id):
    con = mysql.connection.cursor()
    con.execute("select * from transaction where tid=%s",[id])
    r=con.fetchone()
    con.close()
    return render_template('edittrans.html',id=r)
@app.route('/at')
def at():
    return render_template('addtrans.html')
@app.route('/ab')
def ab():
    return render_template('addbook.html')
@app.route('/eb')
def eb():
    return render_template('editbook.html')
#edit trans
@app.route('/eb/<string:id>',methods=['GET','POST'])
def editbook(id):
    con = mysql.connection.cursor()
    con.execute("select * from books where book_no=%s",[id])
    r=con.fetchone()
    con.close()
    return render_template('editbook.html',id=r)
@app.route('/eib')
def eib():
    return render_template('editissue.html')
#edit trans
@app.route('/eib/<string:id>',methods=['GET','POST'])
def editissue(id):
    con = mysql.connection.cursor()
    con.execute("select * from issue_books where issue_id=%s",[id])
    r=con.fetchone()
    con.close()
    return render_template('editissue.html',id=r)
@app.route('/aib')
def aib():
    return render_template('addissue.html')
@app.route('/login')
def logout():
    return render_template('library.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/login')
def login():
    return render_template('library.html')
@app.route('/dash')
def dash():
    con = mysql.connection.cursor()
    con.execute("select * from user;")
    r = len(con.fetchall())
    con.execute("select * from books;")
    d = len(con.fetchall())
    con.close()
    return render_template('dash.html',data=r,data1=d)
@app.route('/user')
def user():
    con=mysql.connection.cursor()
    con.execute("select * from user;")
    r=con.fetchall()
    con.close()
    return render_template('sign.html',data=r)
@app.route('/book')
def book():
    con=mysql.connection.cursor()
    con.execute("select * from books;")
    r=con.fetchall()
    con.close()
    return render_template('books.html',data=r)
@app.route('/transaction')
def trans():
    con=mysql.connection.cursor()
    con.execute("select * from transaction")
    r=con.fetchall()
    con.close()
    return render_template('transaction.html',data=r)
@app.route('/issuebook')
def issue():
    con=mysql.connection.cursor()
    con.execute("select * from issue_books")
    r=con.fetchall()
    con.close()
    return render_template('issues.html',data=r)
#DELETE
@app.route('/deleteuser/<string:id>',methods=['GET','POST'])
def deleteuser(id):
    con = mysql.connection.cursor()
    con.execute("delete from user where user_id=%s",[id])
    mysql.connection.commit()
    con.close()
    return redirect(url_for('user'))
@app.route('/deletebook/<string:id>',methods=['GET','POST'])
def deletebook(id):
    con = mysql.connection.cursor()
    con.execute("delete from Books where book_no=%s",[id])
    mysql.connection.commit()
    con.close()
    return redirect(url_for('book'))
@app.route('/deleteissue/<string:id>',methods=['GET','POST'])
def deleteissue(id):
    con = mysql.connection.cursor()
    con.execute("delete from issue_books where issue_id=%s;",[id])
    mysql.connection.commit()
    con.close()
    return redirect(url_for('issue'))
@app.route('/deletetrans/<string:id>',methods=['GET','POST'])
def deletetrans(id):
    con = mysql.connection.cursor()
    con.execute("delete from transaction where tid=%s;",[id])
    mysql.connection.commit()
    con.close()
    return redirect(url_for('trans'))
#LOGIN PROCESS
@app.route('/ulogin',methods=['GET','POST'])
def ulogin():
    if request.method=="POST":
        uname=request.form['uname']
        pas=request.form['upass']
        con = mysql.connection.cursor()
        con.execute("select * from user where user_name=%s and password=%s;",[uname,pas])
        r = len(con.fetchall())
        con.close()
        if r==1:
            return redirect(url_for('dash'))
        else:
            flash("Invalid user_name or password")
            return redirect(url_for('home'))
#Add user
@app.route('/adduser',methods=['GET','POST'])
def adduser():
    if request.method=="POST":
        id = request.form['fname']
        name = request.form['lname']
        email=request.form['email']
        pas=request.form['mob']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO user(user_id,user_name,Email,Password) value (%s,%s,%s,%s);",(id,name,email,pas))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('user'))
#Add book
@app.route('/addbook',methods=['GET','POST'])
def addbook():
    if request.method=="POST":
        id = request.form['fname']
        name = request.form['lname']
        author=request.form['email']
        qnt=request.form['mob']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO books(book_no,book_name,author,quantity) value (%s,%s,%s,%s);",(id,name,author,qnt))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('book'))
#Add issue
@app.route('/addissue',methods=['GET','POST'])
def addissue():
    if request.method=="POST":
        id = request.form['id']
        uname = request.form['uname']
        bname=request.form['bname']
        issd=request.form['idate']
        expd=request.form['edate']
        retd=request.form['rdate']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO issue_books(issue_id,username,bookname,issuedate,expdate,retundate) value (%s,%s,%s,%s,%s,%s);",(id,uname,bname,issd,expd,retd))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('issue'))
#Add trans
@app.route('/addtrans',methods=['GET','POST'])
def addtrans():
    if request.method=="POST":
        id = request.form['fname']
        uname = request.form['lname']
        name=request.form['email']
        due=request.form['mob']
        sta=request.form['Email']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO transaction(tid,user_name,bookname,due,status) value (%s,%s,%s,%s,%s);",(id,uname,name,due,sta))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('trans'))
#update user
@app.route('/updateuser',methods=['GET','POST'])
def updateuser():
    if request.method=="POST":
        id = request.form['fname']
        name = request.form['lname']
        email=request.form['email']
        pas=request.form['mob']
        con = mysql.connection.cursor()
        con.execute("update user set user_id=%s,user_name=%s,Email=%s,Password=%s where user_id=%s;",(id,name,email,pas,id))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('user'))
#update book
@app.route('/updatebook',methods=['GET','POST'])
def updatebook():
    if request.method=="POST":
        id = request.form['fname']
        name = request.form['lname']
        author=request.form['email']
        quantity=request.form['mob']
        con = mysql.connection.cursor()
        con.execute("update books set book_no=%s,book_name=%s,author=%s,quantity=%s where book_no=%s;",(id,name,author,quantity,id))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('book'))
#update issue
@app.route('/updateissue',methods=['GET','POST'])
def updateissue():
    if request.method=="POST":
        id = request.form['fname']
        name = request.form['lname']
        bname=request.form['email']
        issd=request.form['mob']
        expd=request.form['ed']
        retd=request.form['rd']
        con = mysql.connection.cursor()
        con.execute("update issue_books set issue_id=%s,username=%s,bookname=%s,issuedate=%s,expdate=%s,retundate=%s where issue_id=%s;",(id,name,bname,issd,expd,retd,id))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('issue'))
#update issue
@app.route('/updatetrans',methods=['GET','POST'])
def updatetrans():
    if request.method=="POST":
        id = request.form['id']
        uname = request.form['uname']
        name = request.form['bname']
        due = request.form['due']
        sta = request.form['status']
        con = mysql.connection.cursor()
        con.execute("update transaction set tid=%s,user_name=%s,bookname=%s,due=%s,status=%s where tid=%s;",(id,uname,name,due,sta,id))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('trans'))

if __name__=='__main__':
    app.run(debug=True)