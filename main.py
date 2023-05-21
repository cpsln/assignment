from fastapi import FastAPI
from routers import courses
from seeds import initseed

app = FastAPI()

# parse the course.json file
# if data already added then skip else adding course data in local db `course`
initseed.all()

app.include_router(courses.router)
