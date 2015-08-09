# from project import app
from project.models import *
from flask import render_template, request, redirect, session, url_for, g, Blueprint
from facebook import get_user_from_cookie, GraphAPI
from form import RegistrationForm

# blueprint config
users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates')


# Facebook app details
FB_APP_ID = '528895670599140'
FB_APP_NAME = 'bloodlist'
FB_APP_SECRET = '5a80e6cf3e44bd9c424492d028efe956'


@users_blueprint.route('/register', methods=['POST', 'GET'])
def register():
    if g.user:
        donor_data = DonorInfo.query.filter_by(uid=g.user['id']).first()
        print donor_data
        if g.user['id']:
            return render_template('show_info.html', donor_data=donor_data)
        elif request.method == 'POST':
            form_sub = RegistrationForm()
            if form_sub.validate_on_submit():
                donor_info = DonorInfo(uid=g.user['id'],
                                       name=form_sub.name.data,
                                       blood_group=form_sub.blood_group.data,
                                       contact=form_sub.contact.data,
                                       area=form_sub.area.data,
                                       sex=form_sub.sex.data,
                                       birthdate=form_sub.birthdate.data,
                                       last_donated=form_sub.last_donated.data)
                db.session.add(donor_info)
                db.session.commit()
                return render_template('search.landing.html')
        form = RegistrationForm(request.form)
        return render_template('hello.html', app_id=FB_APP_ID,
                               app_name=FB_APP_NAME, user=g.user, form=form)
    # Otherwise, a user is not logged in.
    return render_template('register.html', app_id=FB_APP_ID, name=FB_APP_NAME)


@users_blueprint.route('/logout')
def logout():
    """Log out the user from the application.

    Log out the user from the application by removing them from the
    session.  Note: this does not log the user out of Facebook - this is done
    by the JavaScript SDK.
    """
    session.pop('user', None)
    return redirect(url_for('search.index'))


@users_blueprint.route('/edit', methods=['GET', 'POST'])
def edit():
    form = RegistrationForm(request.form)
    donor = DonorInfo.query.filter_by(uid=g.user['id']).first()
    return render_template('edit.html', user=donor, form=form)


@users_blueprint.before_request
def get_current_user():
    if session.get('user'):
        g.user = session.get('user')
        return

    result = get_user_from_cookie(cookies=request.cookies,
                                  app_id=FB_APP_ID,
                                  app_secret=FB_APP_SECRET)

    if result:
        user = Donor.query.filter(Donor.uid == result['uid']).first()

        if not user:

            graph = GraphAPI(result['access_token'])
            profile = graph.get_object('me')

            user = Donor(uid=str(profile['id']),
                         name=profile['name'],
                         access_token=result['access_token'])

            db.session.add(user)

        elif user.access_token != result['access_token']:
            user.access_token = result['access_token']

        session['user'] = dict(name=user.name,
                               id=user.uid,
                               access_token=user.access_token)

    db.session.commit()
    g.user = session.get('user', None)
