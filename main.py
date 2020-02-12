from flask import Flask, request, Response, render_template, redirect, url_for
from dbConnect import execute_query
app = Flask(__name__)

@app.route('/')
def admin():
    return render_template('front.html', )

@app.route('/login', methods = ['POST', 'GET'])
def login():
    
    if request.method == 'POST':
        Email=request.form['Email']
        Password=request.form['Password']
        sql_query="SELECT * FROM users;"
        result=execute_query(sql_query)
        for i in result:
            if Email==i[3] and Password==i[4]:
                return redirect(url_for('booking'))

        return("invalid credentials")
        
        sql_query="INSERT INTO users(Email,Password) VALUES ('{}', '{}');".format(Email,Password)
        execute_query(sql_query, 'insert')

        return('added into database.')
    else:
        return render_template('login.html')

@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    
    if request.method=='POST':
        First_Name=request.form['First_Name']
        Last_Name=request.form['Last_Name']
        Email=request.form['Email']
        Password=request.form['Password']
        sql_query="SELECT * FROM users;"
        result= execute_query(sql_query)
        for i in result:
            if Email==i[3]:
                return('email already taken..try with new one.')
            else:
                sql_query="INSERT INTO users(First_Name,Last_Name,Email,Password) VALUES ('{}','{}','{}','{}');".format(First_Name,Last_Name,Email,Password)
        execute_query(sql_query,'insert')
    return render_template('signup.html')


@app.route('/booking', methods=['POST','GET'])
def booking():
    
    if request.method=='POST':
        
        First_Name=request.form['First_Name']
        Last_Name=request.form['Last_Name']
        Email=request.form['Email']
        Phone=request.form['Phone']
        Vehicle_No=request.form['Vehicle_No']
        Slot_ID=request.form['Slot_ID']
        Date=request.form['Date']
        Time=request.form['Time']
        sql_query="SELECT * FROM bookings;"
        bookin=execute_query(sql_query)
        for i in bookin:
            if Slot_ID==i[5]:
                return('slot Not available..pick Another Slot')
            else:
                sql_query="INSERT INTO bookings(First_Name,Last_Name,Email,Phone,Vehicle_No,Slot_ID,Date,Time) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}');".format(First_Name,Last_Name,Email,Phone,Vehicle_No,Slot_ID,Date,Time)
        execute_query(sql_query,'insert')
    return render_template('new_booking.html')
    
if __name__ == '__main__':
    app.run(debug = True)
    