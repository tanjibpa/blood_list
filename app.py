from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# config
import os
app.config.from_object(os.environ['APP_SETTINGS'])

# sqlalchemy object
db = SQLAlchemy(app)

from models import *


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        blood_group_qrd = request.form.get('blood-group')
        area_qrd = request.form.get('area')
        que = db.session.query(DonorInfo).filter_by(
            blood_group=blood_group_qrd, area=area_qrd).all()
        donors = [dict(first_name=row.first_name, last_name=row.last_name,
                       blood_group=row.blood_group, contact=row.contact,
                       area=row.area, sex=row.sex, birthdate=row.birthdate,
                       last_donated=row.last_donated, can_donate=row.can_donate)
                  for row in que]
        print donors
        return render_template('result.html',
                               donors=donors,
                               blood_group=blood_group_qrd,
                               area=area_qrd)
    return render_template('landing.html')


@app.route('/fb', methods=['GET', 'POST'])
def fb():
    return render_template('fb.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
