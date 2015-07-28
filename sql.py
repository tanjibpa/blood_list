import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute(
        """CREATE TABLE donors(
        	id INTEGER PRIMARY KEY,
        	first_name TEXT,
        	last_name TEXT,
        	blood_group BLOB,
        	area TEXT,
        	sex TEXT,
        	birthdate DATE,
        	last_donated DATE)""")

    c.execute(
        'INSERT INTO donors(first_name, last_name, blood_group, area, sex, birthdate, last_donated) VALUES("Ikramul", "Alam", "O+", "Chittagong", "Male", "09-12-1990", "10-07-2015")')
    c.execute(
        'INSERT INTO donors(first_name, last_name, blood_group, area, sex, birthdate, last_donated) VALUES("Safayet", "Alam", "B+", "Chittagong", "Male", "27-08-1992", "12-05-2015")')
    c.execute(
        'INSERT INTO donors(first_name, last_name, blood_group, area, sex, birthdate, last_donated) VALUES("Humaira", "Islam", "A+", "Chittagong", "Female", "11-02-1991", "20-02-2015")')
    c.execute(
        'INSERT INTO donors(first_name, last_name, blood_group, area, sex, birthdate, last_donated) VALUES("John", "Doe", "A-", "Dhaka", "Male", "11-02-1991", "20-02-2015")')
    c.execute(
        'INSERT INTO donors(first_name, last_name, blood_group, area, sex, birthdate, last_donated) VALUES("Jao", "Ji", "B-", "Rajshahi", "Female", "11-02-1991", "20-02-2015")')
    c.execute(
        'INSERT INTO donors(first_name, last_name, blood_group, area, sex, birthdate, last_donated) VALUES("Dick", "Head", "O-", "Sylhet", "Male", "11-02-1991", "20-02-2015")')
    c.execute(
        'INSERT INTO donors(first_name, last_name, blood_group, area, sex, birthdate, last_donated) VALUES("Butt", "Head", "AB+", "Rangpur", "Female", "11-02-1991", "20-02-2015")')
    c.execute(
        'INSERT INTO donors(first_name, last_name, blood_group, area, sex, birthdate, last_donated) VALUES("Shit", "Head", "AB-", "Khulna", "Female", "11-02-1991", "20-02-2015")')
    c.execute(
        'INSERT INTO donors(first_name, last_name, blood_group, area, sex, birthdate, last_donated) VALUES("Piss", "Head", "O+", "Barisal", "Female", "11-02-1991", "20-02-2015")')
    c.execute(
        'INSERT INTO donors(first_name, last_name, blood_group, area, sex, birthdate, last_donated) VALUES("Fart", "Head", "O-", "Dhaka", "Male", "11-02-1991", "20-02-2015")')
    c.execute(
        'INSERT INTO donors(first_name, last_name, blood_group, area, sex, birthdate, last_donated) VALUES("Mad", "Man", "A+", "Rajshahi", "Male", "11-02-1991", "20-02-2015")')
    c.execute(
        'INSERT INTO donors(first_name, last_name, blood_group, area, sex, birthdate, last_donated) VALUES("Mad", "Woman", "A+", "Khulna", "Female", "11-02-1991", "20-02-2015")')
    c.execute(
        'INSERT INTO donors(first_name, last_name, blood_group, area, sex, birthdate, last_donated) VALUES("Dimm", "Egg", "B-", "Sylhet", "Female", "11-02-1991", "20-02-2015")')
