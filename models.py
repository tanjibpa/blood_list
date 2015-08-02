from app import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class DonorInfo(db.Model):

    __tablename__ = "donorinfo"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    blood_group = db.Column(db.String, nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    area = db.Column(db.String, nullable=False)
    sex = db.Column(db.String, nullable=False)
    birthdate = db.Column(db.LargeBinary, nullable=False)
    last_donated = db.Column(db.LargeBinary, nullable=False)
    can_donate = db.Column(db.Boolean, nullable=False)
    donor_id = db.Column(db.Integer, ForeignKey('donors.id'))

    def __init__(self, first_name, last_name, blood_group, contact, area, sex, birthdate, last_donated, can_donate):

        self.first_name = first_name
        self.last_name = last_name
        self.blood_group = blood_group
        self.contact = contact
        self.area = area
        self.sex = sex
        self.birthdate = birthdate
        self.last_donated = last_donated
        self.can_donate = can_donate

    def __repr__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Donor(db.Model):

    __tablename__ = "donors"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    info = relationship("DonorInfo", backref="donor")

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<email {}'.format(self.email)
