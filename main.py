from fastapi import FastAPI
from routers import courses
from seeds import initseed

app = FastAPI()

# parse the course.json file
# if data already added then skip else adding course data in local db `course`
initseed.all()

app.include_router(courses.router)

# docker-compose -f docker-compose.yaml up -d --build

# echo "# assignment" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/cpsln/assignment.git
# git push -u origin main
# git remote add origin https://github.com/cpsln/assignment.git
# git branch -M main
# git push -u origin main