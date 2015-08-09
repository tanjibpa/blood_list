from app import db
from models import DonorInfo

# create the databasean and database tables
db.create_all()

# insert
db.session.add(
    DonorInfo("Ikramul",
              "Alam",
              "O+", "01678691763", "Chittagong", "Male", "1990-12-09", "2015-07-10", True, 1))
db.session.add(
    DonorInfo("Safayet",
              "Alam",
              "B+", "01620467439", "Chittagong", "Male", "1992-08-27", "2015-05-12", True, 1))
db.session.add(
    DonorInfo("Humaira",
              "Islam",
              "A+", "01678691753", "Chittagong", "Female", "1991-02-11", "2015-02-20", True, 1))
db.session.add(
    DonorInfo("John",
              "Doe",
              "A-", "01234567891", "Dhaka", "Male", "1991-02-11", "2015-02-20", True, 1))
db.session.add(
    DonorInfo("Jao",
              "Ji",
              "B-", "01234567891", "Rajshahi", "Female", "1991-02-11", "2015-02-20", True, 1))
db.session.add(
    DonorInfo("Dick",
              "Head",
              "O-", "01234567891", "Sylhet", "Male", "1991-02-11", "2015-02-20", True, 1))
db.session.add(
    DonorInfo("Butt",
              "Head",
              "AB+", "01234567891", "Rangpur", "Female", "1991-02-11", "2015-02-20", True, 1))
db.session.add(
    DonorInfo("Shit",
              "Head",
              "AB-", "01234567891", "Khulna", "Female", "1991-02-11", "2015-02-20", True, 1))
db.session.add(
    DonorInfo("Piss",
              "Head",
              "O+", "01234567891", "Barisal", "Female", "1991-02-11", "2015-02-20", True, 1))
db.session.add(
    DonorInfo("Fart",
              "Head",
              "O-", "01234567891", "Dhaka", "Male", "1991-02-11", "2015-02-20", True, 1))
db.session.add(
    DonorInfo("Mad",
              "Man",
              "A+", "01234567891", "Rajshahi", "Male", "1991-02-11", "2015-02-20", True, 1))
db.session.add(
    DonorInfo("Mad",
              "Woman",
              "A+", "01234567891", "Khulna", "Female", "1991-02-11", "2015-02-20", True, 1))
db.session.add(
    DonorInfo("Dimm",
              "Egg",
              "B-", "01234567891", "Sylhet", "Female", "1991-02-11", "2015-02-20", True, 1))


# commit the changes
db.session.commit()
