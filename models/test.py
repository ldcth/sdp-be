import pyrebase
import uuid

from core.config import db

problems = db.child("user").get()

# Iterate through the retrieved data
for problem in problems.each():
    print(problem.key(), problem.val())