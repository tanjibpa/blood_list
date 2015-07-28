from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)

app.secret_key = "something weird"
app.database = "sample.db"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        blood_group_qrd = request.form.get('blood-group')
        area_qrd = request.form.get('area')
        g.db = connect_db()
        cur = g.db.execute(
            "SELECT * FROM donors WHERE blood_group=? AND area=?", (blood_group_qrd, area_qrd))
        donors = [dict(first_name=row[1], last_name=row[2], blood_group=row[3],
                       area=row[4], sex=row[5], birthdate=row[6], last_donated=row[7])
                  for row in cur.fetchall()]
        print donors
        g.db.close()
        return render_template('result.html', donors=donors, blood_group=blood_group_qrd, area=area_qrd)
    return render_template('landing.html')


def connect_db():
    return sqlite3.connect(app.database)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
