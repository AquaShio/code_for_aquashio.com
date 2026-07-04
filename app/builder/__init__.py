from flask import Blueprint
builder = Blueprint("builder", __name__, url_prefix="/builder")
from app.builder import routes