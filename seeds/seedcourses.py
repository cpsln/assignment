from database import connection
import logging
import json

def seed_courses():
    # if course details already added
    if check_already_added():
        return

    try:
        with open("courses.json") as my_file:
            courses_details = json.load(my_file)
        connection.db.courses_information.insert_many(courses_details)

    except Exception as e:
        print(e)
        return

# check course details added or not
def check_already_added():
    try:
        courses_info = list(connection.db.courses_information.find())
        if len(courses_info) > 0:
            return True
        return False
    except Exception as e:
        logging.error('Db connection err')
        return False
        