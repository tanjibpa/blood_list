from flask import Flask, render_template, request, redirect, session, url_for, g
from facebook import get_user_from_cookie, GraphAPI
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# config
import os
app.config.from_object(os.environ['APP_SETTINGS'])

# sqlalchemy object
db = SQLAlchemy(app)

from models import *

# Facebook app details
FB_APP_ID = '528895670599140'
FB_APP_NAME = 'bloodlist'
FB_APP_SECRET = '5a80e6cf3e44bd9c424492d028efe956'


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
        return render_template('result.html',
                               donors=donors,
                               blood_group=blood_group_qrd,
                               area=area_qrd)
    return render_template('landing.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if g.user:
        return render_template('hello.html', app_id=FB_APP_ID,
                               app_name=FB_APP_NAME, user=g.user)
    # Otherwise, a user is not logged in.
    return render_template('register.html', app_id=FB_APP_ID, name=FB_APP_NAME)


@app.route('/logout')
def logout():
    """Log out the user from the application.

    Log out the user from the application by removing them from the
    session.  Note: this does not log the user out of Facebook - this is done
    by the JavaScript SDK.
    """
    session.pop('user', None)
    return redirect(url_for('index'))


@app.before_request
def get_current_user():
    if session.get('user'):
        g.user = session.get('user')
        return

    result = get_user_from_cookie(cookies=request.cookies,
                                  app_id=FB_APP_ID,
                                  app_secret=FB_APP_SECRET)

    if result:
        user = Donor.query.filter(Donor.id == result['uid']).first()

        if not user:

            graph = GraphAPI(result['access_token'])
            profile = graph.get_object('me')

            user = Donor(id=profile['id'],
                         name=profile['name'],
                         profile_url=profile['link'],
                         access_token=profile['access_token'])

            db.session.add(user)

        elif user.access_token != result['access_token']:
            user.access_token = result['access_token']

        session['user'] = dict(name=user.name, profile_url=user.profile_url,
                               id=user.id, access_token=user.access_token)

    db.session.commit()
    g.user = session.get('user', None)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
