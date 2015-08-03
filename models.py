from datetime import datetime
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

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated = db.Column(db.DateTime, default=datetime.utcnow, nullable=False,
                        onupdate=datetime.utcnow)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    profile_url = db.Column(db.String, nullable=False)
    access_token = db.Column(db.String)
    info = relationship("DonorInfo", backref="donor")

    def __init__(self, email, password, created, updated, name, profile_url, access_token):
        self.email = email
        self.password = password
        self.created = created
        self.updated = updated
        self.name = name
        self.profile_url = profile_url
        self.access_token = access_token

    def __repr__(self):
        return '<email {}'.format(self.email)
