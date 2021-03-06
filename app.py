from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

data = {'1': 'bed+OR+beds', '2': 'icu', '3': 'oxygen', '4': 'ventilator+OR+ventilators',
        '5': 'test+OR+tests+OR+testing', '6': 'remdesivir', '7': 'favipiravir',
        '8': 'tocilizumab', '9': 'plasma', '10': 'food', '11': 'Fabiflu', '12': 'ambulance'}


@app.route('/', methods=['POST', 'GET'])
def index():
    conn = sqlite3.connect('static/counter.db')
    cur = conn.cursor()
    cur.execute("select * from counter")
    a = cur.fetchone()
    a = a[0]
    b = a + 1
    update_query = """Update counter set count = ? where count = ?"""
    data1 = (b, a)
    cur.execute(update_query, data1)
    conn.commit()
    if request.method == 'POST':
        d = request.form['data']
        q = 'https://twitter.com/search?q=verified+indore+'
        x = q + data[d] + '+-"needed"+-"need" + -"needs"+-"required"+ -"require" + -"requires" + -"requirement" + -"requirements"&f=live'
        return redirect(x)
    return render_template("IndoreAgainstCovid.html")


@app.route('/feedbackyes', methods=['POST', 'GET'])
def feedbackyes():
    conn1 = sqlite3.connect('static/counter.db')
    cur1 = conn1.cursor()
    cur1.execute("select yes from feedback")
    y = cur1.fetchone()
    y = y[0]
    yu = y + 1
    update_query1 = """Update feedback set yes = ? where yes = ?"""
    data11 = (yu, y)
    cur1.execute(update_query1, data11)
    conn1.commit()
    return ("nothing")


@app.route('/feedbackno', methods=['POST', 'GET'])
def feedbackno():
    conn2 = sqlite3.connect('static/counter.db')
    cur2 = conn2.cursor()
    cur2.execute("select no from feedback")
    n = cur2.fetchone()
    n = n[0]
    nu = n + 1
    update_query2 = """Update feedback set no = ? where no = ?"""
    data12 = (nu, n)
    cur2.execute(update_query2, data12)
    conn2.commit()
    return ("nothing")


@app.route('/counter')
def counter():
    conn = sqlite3.connect('static/counter.db')
    cur = conn.cursor()
    cur.execute("select * from counter")
    a = cur.fetchone()
    a = a[0]
    txt = "Total no of visit: {}<br />".format(a)
    cur.execute("select yes from feedback")
    y = cur.fetchone()
    y = y[0]
    cur.execute("select no from feedback")
    n = cur.fetchone()
    n = n[0]
    txt1 = "Total no of Yes:{}<br />".format(y)
    txt2 = "Total no of NO:{}<br />".format(n)
    return txt + txt1 + txt2


if __name__ == '__main__':
    app.run()
