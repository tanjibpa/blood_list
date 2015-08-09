from flask import render_template, request, Blueprint
# from project import app, db

from project.models import *
# config blueprint
search_blueprint = Blueprint('search', __name__, template_folder='templates')


@search_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        blood_group_qrd = request.form.get('blood-group')
        area_qrd = request.form.get('area')
        que = db.session.query(DonorInfo).filter_by(
            blood_group=blood_group_qrd, area=area_qrd).all()
        donors = [dict(name=row.name,
                       blood_group=row.blood_group, contact=row.contact,
                       area=row.area, sex=row.sex, birthdate=row.birthdate,
                       last_donated=row.last_donated)
                  for row in que]
        return render_template('result.html',
                               donors=donors,
                               blood_group=blood_group_qrd,
                               area=area_qrd)
    return render_template('landing.html')
