from sanic import Blueprint, response
from sanic.exceptions import NotFound
import requests as r

static = Blueprint("static")
static.static("/static", "./web/static")
