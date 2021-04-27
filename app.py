from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

data = {'1': 'bed+OR+beds', '2': 'icu', '3': 'oxygen', '4': 'ventilator+OR+ventilators',
        '5': 'test+OR+tests+OR+testing', '6': 'remdesivir', '7': 'favipiravir',
        '8': 'tocilizumab', '9': 'plasma', '10': 'food'}


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
        x = q + data[d] + '+-"needed"+-"required"&f=live'
        return redirect(x)
    return render_template("index.html")

@app.route('/feedbackyes',methods=['POST', 'GET'])
def feedbackyes():
    print("yes clicked")
    return ("nothing")

@app.route('/feedbackno',methods=['POST', 'GET'])
def feedbackno():
    print("no clicked")
    return ("nothing")


@app.route('/counter')
def counter():
    conn = sqlite3.connect('static/counter.db')
    cur = conn.cursor()
    cur.execute("select * from counter")
    a = cur.fetchone()
    a = a[0]
    txt="Total no of visit: {}<br />".format(a)
    txt1="Total no of Yes:"
    return txt+txt1


if __name__ == '__main__':
    app.run()
