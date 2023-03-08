import random

from flask import request

from app.resources import create_or_update_resource, delete_resource
from app.models import Student, course
