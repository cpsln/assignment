from database import connection
from bson import ObjectId

def all_courses_from_db(sort_by, sort_order):
     try:
          courses_information = connection.db.courses_information.find()
          if sort_by != "":
               courses_information = courses_information.sort(sort_by,sort_order)

          return list(courses_information)
     except Exception as e:
          print(e)
          return {"error":e.args}

def courses_overview_from_db(course_id):
     try:
          courses_information = connection.db.courses_information.find_one({"_id":ObjectId(course_id)})
          return dict(courses_information)
     except Exception as e:
          print(e)
          return {"error":e.args}

def chapter_information_from_db(chapter_name):
     try:
          courses_information = connection.db.courses_information.aggregate(
               [
                    {'$unwind':"$chapters"}, 
                    {'$match':{"chapters.name":chapter_name}}
               ]
          )
          return list(courses_information)
     except Exception as e:
          print(e)
          return {"error":e.args}

def get_chapter_information_from_db(id):
     try:
          courses_information = connection.db.courses_information.find_one(
               {'_id':ObjectId(id)}
          )
          return dict(courses_information)
     except Exception as e:
          print(e)
          return {"error":e.args}

def update_chapter_information(id,query):
     try:
          courses_information = connection.db.courses_information.update_one(
               {'_id':ObjectId(id)},
               {
                    '$set': query
               }
          )
          print(int(courses_information))
          return 
     except Exception as e:
          print(e)
          return {"error":e.args}

