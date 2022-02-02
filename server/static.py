from sanic import Blueprint, response
from sanic.exceptions import NotFound
import requests as r

static = Blueprint("static")
static.static("/static", "./web/static")


@static.exception(NotFound)
async def fetch_retrobowl(req, exception):
    if not req.path.startswith("/static/1v1lol"):
        return response.text("Not found", status=404)

    print("Fetching", req.path)

    res = r.get("https://game316009.konggames.com/gamez/0031/6009/live/html5game/"+req.path.split("/static/retrobowl/html5game/")[1])

    print("Found it", res.status_code)

    if res.status_code != 200:
        return response.text("Not found", status=404)

    print("Saving")

    with open("web" + req.path, "wb") as f:
        f.write(res.content)

    print(res.content[:100])
    
    return response.raw(res.content)
