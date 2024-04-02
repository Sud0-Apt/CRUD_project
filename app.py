from flask import Flask, render_template,request,redirect,url_for,session
import psycopg2
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

conn = psycopg2.connect(
    dbname = 'logbook',
    user = 'your_username1',
    password = 'your_password',
    host = 'localhost'
)

cur = conn.cursor()

# ROUTING SECTION FOR HTML PAGES
@app.route('/')
def index():
    return render_template('base.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/read')
def read():
    return render_template('read.html')

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/delete')
def delete():
    return render_template('delete.html')

#ROUTING SECTION FOR CREATE
@app.route('/insertData', methods = ['POST'])
def insert_data():
    try:
        mobile = request.form['mobile']
        name = request.form['name']
        mail = request.form['mail']
        city = request.form['city']
        remarks = request.form['remarks']

        cur.execute("""INSERT INTO addbook (mobile,name,mail,city,remarks) VALUES (%s,%s,%s,%s,%s)
                    """,(mobile,name,mail,city,remarks))
        
        conn.commit()
        
        session['message'] = 'Data insertion successful'

        return redirect(url_for('index'))  # Redirect to the '/' route
    except KeyError as e:
        return f'Missing form field: {e}', 400
    except Exception as e:
        return 'Error inserting data: ' + str(e), 500


#ROUTING SECTION FOR READ
@app.route('/fetchData')
def fetch_data():
    try:
        # Query the database to fetch data
        cur.execute('SELECT * FROM addbook')
        rows = cur.fetchall()

        # Pass the fetched data to the template
        return render_template('read.html', rows=rows)
    except Exception as e:
        return 'Error: ' + str(e), 500



#ROUTING SECTION FOR UPDATE
@app.route('/updateData', methods=['POST'])
def update_data():
    try:
        mobile = request.form['mobile']
        name = request.form['name']
        mail = request.form['mail']
        city = request.form['city']
        remarks = request.form['remarks']

        cur.execute("""update addbook set name = %s,mail = %s,city = %s,remarks = %s where mobile = %s
        """, (name, mail, city, remarks,mobile))

        conn.commit()

        session['message'] = 'Data updated!!'

        return redirect(url_for('index'))  # Redirect to the '/' route
    except KeyError as e:
        return f'Missing form field: {e}', 400
    except Exception as e:
        return 'Error inserting data: ' + str(e), 500


#ROUTING SECTION FOR DELETE
@app.route('/deleteData', methods = ['POST'])
def delete_data():
    try:
        mobile = request.form['mobile']
        # Check if the mobile number exists in the database
        cur.execute("SELECT COUNT(*) FROM addbook WHERE mobile = %s", (mobile,))
        if cur.fetchone()[0] == 0:  # If no rows are returned, the data doesn't exist
            session['message'] = 'This data do not exist ):'
        else:
            cur.execute("DELETE FROM addbook WHERE mobile = %s", (mobile,))
            conn.commit()
            session['message'] = 'Data deletion successful'
        return redirect(url_for('index'))  # Redirect to the '/' route
    except KeyError as e:
        return f'Missing form field: {e}', 400
    except Exception as e:
        return 'Error deleting data: ' + str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
