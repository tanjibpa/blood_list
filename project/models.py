from datetime import datetime
from project import db

# from sqlalchemy import Date
# from sqlalchemy.orm import relationship
# from sqlalchemy.dialects.postgresql import Date


class DonorInfo(db.Model):

    __tablename__ = "donorinfo"

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    blood_group = db.Column(db.String, nullable=False)
    contact = db.Column(db.String, nullable=False)
    area = db.Column(db.String, nullable=False)
    sex = db.Column(db.String, nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    last_donated = db.Column(db.Date, nullable=True)
    can_donate = db.Column(db.Boolean, nullable=False, default=True)
    # donor_id = db.Column(db.Integer, ForeignKey('donors.id'))

    # def __init__(self, first_name, last_name, blood_group, contact, area, sex, birthdate, last_donated, can_donate):

    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.blood_group = blood_group
    #     self.contact = contact
    #     self.area = area
    #     self.sex = sex
    #     self.birthdate = birthdate
    #     self.last_donated = last_donated
    #     self.can_donate = can_donate

    # def __repr__(self):
    #     return '{} {}'.format(self.first_name, self.last_name)


class Donor(db.Model):

    __tablename__ = "donors"

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    uid = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated = db.Column(db.DateTime, default=datetime.utcnow, nullable=False,
                        onupdate=datetime.utcnow)
    name = db.Column(db.String, nullable=False)
    access_token = db.Column(db.String, nullable=False)
    # info = relationship("DonorInfo", backref="donor")
