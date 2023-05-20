from fastapi import APIRouter
from controllers import courses_controller
from .base_model import ChapterRating

router = APIRouter()


# This function return all course details order by give value
# Accept only 3 type sorting
# Sorting by data or title or rating
# [GET]
@router.get("/courses", tags=["courses"])
async def get_all_courses(sort_by: str=''):
    return courses_controller.get_all_courses(sort_by)


# This take course id in query params
# Return the course details if found
# [GET]
@router.get("/courses/overview", tags=["courses"])
async def get_courses_overview(id: str=''):
    return courses_controller.get_courses_overview(id)


# This function take chapter name
# Return the chapter details
# [GET]
@router.get("/courses/chapter/information", tags=["courses"])
async def get_courses_chapter_information(id: str=''):
    return courses_controller.courses_chapter_information(id)


# This function take chapter name
# Return the chapter details
# [GET]
@router.get("/courses/chapter/rating", tags=["courses"])
async def get_courses_chapter_rating(id: str,req_body: ChapterRating):
    print(req_body.name)
    return courses_controller.courses_chapter_rating(id,req_body.name,req_body.rating)