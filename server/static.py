from sanic import Blueprint, response

static = Blueprint("static")
static.static("/static", "./web/static")

@static.middleware("response")
async def auth(req, res):
    # Doesn't exist yet, and will be hard to implement due to the usage of a CDN
    ...
