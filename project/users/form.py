from flask_wtf import Form
from wtforms import TextField, RadioField, SelectField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email


class RegistrationForm(Form):
    name = TextField('Name', validators=[DataRequired()])
    blood_group = SelectField('Blood Group', choices=[('O+', 'O+'), ('O-', 'O-'),
                                                      ('A+', 'A+'), ('A-', 'A-'),
                                                      ('B+', 'B+'), ('B-', 'B-'),
                                                      ('AB+', 'AB+'), ('AB-', 'AB-')])

    contact = IntegerField('Contact', validators=[DataRequired()])
    email = TextField('Email', validators=[Email()])
    area = SelectField('Area', choices=[('Chittagong', 'Chittagong'),
                                        ('Dhaka', 'Dhaka'),
                                        ('Rajshahi', 'Rajshahi'),
                                        ('Khulna', 'Khulna'),
                                        ('Sylhet', 'Sylhet'),
                                        ('Barisal', 'Barisal'),
                                        ('Rangpur', 'Rangpur')])
    sex = RadioField('Sex', choices=[('Male', 'Male'),
                                     ('Female', 'Female'),
                                     ('Other', 'Other')])
    birthdate = DateField(
        'Birthdate', format='%Y-%m-%d', validators=[DataRequired()])
    last_donated = DateField('When did you last donated?', format='%Y-%m-%d')
