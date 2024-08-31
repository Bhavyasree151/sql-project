Student Management System README
Overview
This is a database schema for a student management system, designed to store information about students, teachers, parents, classes, and subjects.

Tables
1. user_login
user_id (TEXT, PRIMARY KEY)
user_password (TEXT)
first_name (TEXT)
last_name (TEXT)
sign_up_on (DATE)
email_id (TEXT)

2. parent_details
parent_id (TEXT, PRIMARY KEY)
father_first_name (TEXT)
father_last_name (TEXT)
father_email_id (TEXT)
father_mobile (TEXT)
father_occupation (TEXT)
mother_first_name (TEXT)
mother_last_name (TEXT)
mother_email_id (TEXT)
mother_mobile (TEXT)
mother_occupation (TEXT)

3. teachers
teacher_id (TEXT, PRIMARY KEY)
first_name (TEXT)
last_name (TEXT)
date_of_birth (DATE)
email_id (TEXT)
contact (TEXT)
registration_date (DATE)
registration_id (TEXT, UNIQUE)

4. class_details
class_id (TEXT, PRIMARY KEY)
class_teacher (TEXT, FOREIGN KEY referencing teachers)
class_year (TEXT)

6. student_details
student_id (TEXT, PRIMARY KEY)
first_name (TEXT)
last_name (TEXT)
date_of_birth (DATE)
class_id (TEXT, FOREIGN KEY referencing class_details)
roll_no (TEXT)
email_id (TEXT)
parent_id (TEXT, FOREIGN KEY referencing parent_details)
registration_date (DATE)
registration_id (TEXT, UNIQUE)

7. subject
subject_id (TEXT, PRIMARY KEY)
subject_name (TEXT)
class_year (TEXT)
subject_head (TEXT, FOREIGN KEY referencing teachers)

8. subject_tutors
row_id (SERIAL, PRIMARY KEY)
subject_id (TEXT, FOREIGN KEY referencing subject)
teacher_id (TEXT, FOREIGN KEY referencing teachers)
class_id (TEXT, FOREIGN KEY referencing class_details)
SQL Code
The SQL code for creating the above tables is provided in the accompanying SQL file.

I hope this rewritten README file meets your requirements! Let me know if you need any further assistance.
