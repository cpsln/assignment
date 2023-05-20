from services import courses_service
from fastapi import HTTPException
from bson import json_util
import json

def get_all_courses(sort_by):
    try:
        sort_with ={
            "date":-1,
            "title":1,
            "rating":1
        }

        if sort_by != '' and sort_by not in sort_with.keys():
            return HTTPException(status_code=400, detail="Invalid type of sort, we allow only `date, title, rating`")

        sort_order = 1
        if sort_by != '':
            sort_order = sort_with[sort_by]

        courses_details = courses_service.all_courses_from_db(sort_by,sort_order)
        response = json.loads(json_util.dumps(courses_details))

        if type(response) is dict and "error" in response.keys():
            return HTTPException(status_code=404, detail="Details not found.")

        return response

    except Exception as e:
        print(e)
        return HTTPException(status_code=500, detail="Internal server error.")


def get_courses_overview(course_id):

    if course_id == '':
        return HTTPException(status_code=400, detail="Please provide course id.")

    try:
        courses_overview = courses_service.courses_overview_from_db(course_id)
        response = json.loads(json_util.dumps(courses_overview))

        if type(response) is dict and "error" in response.keys():
            return HTTPException(status_code=404, detail="Details not found.")

        return response

    except Exception as e:
        print(e)
        return HTTPException(status_code=500, detail="Internal server error.")

def courses_chapter_information(name):
    if name == '':
        return HTTPException(status_code=400, detail="Please provide course id.")

    try:
        courses_overview = courses_service.chapter_information_from_db(name)
        response = json.loads(json_util.dumps(courses_overview))

        if type(response) is dict and "error" in response.keys():
            return HTTPException(status_code=404, detail="Details not found.")

        return response

    except Exception as e:
        print(e)
        return HTTPException(status_code=500, detail="Internal server error.")

def courses_chapter_rating(cId,name, rating):
    if cId == '' or name =='' or rating not in [-1,1]:
        return HTTPException(status_code=400, detail="Please provide valid id, name and rating value")
    
    try:
        courses_overview = courses_service.get_chapter_information_from_db(cId)
        response = json.loads(json_util.dumps(courses_overview))

        if type(response) is dict and "error" in response.keys():
            return HTTPException(status_code=404, detail="Details not found.")

        query = {}
        for i, v in enumerate(courses_overview['chapters']):
            if name == v['name']:
                if 'rating' in v.keys():
                    if rating == 1:
                        v['rating'] = v['rating'] + 1
                        query[f'chapters.{i}'] = v
                    else:
                        v['rating'] = v['rating'] - 1
                        query[f'chapters.{i}'] = v
                else:
                    v['rating'] = rating
                    query[f'chapters.{i}'] = v
                break
        print(query)
        courses_service.update_chapter_information(cId,query)
        return response
        # return {'msg':"Thank for giving rating"}

    except Exception as e:
        print(e)
        return HTTPException(status_code=500, detail="Internal server error.")

