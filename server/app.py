"""
Copyright (C) 2022  Zebulon Taylor <zceboys@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from sanic import Sanic, response
from server import template, counter, static
import json

app = Sanic("Schoology")

app.config.NOISY_EXCEPTIONS = True

app.blueprint(static.static)

games = json.loads(open("server/games.json").read())
game_urls = {k.split("#")[0] for k in games.keys()}

@app.route("/")
async def index(req):
    if "duckdns" in req.url:
        return response.redirect("https://schology.my.to/")
    return response.html(await template.render_template(req, "index.html", games=games))

@app.route("/<path:" + "|".join(game_urls) + ">")
async def routes(req, path: str):
    return response.html(await template.render_template(req, "template.html", game=path))

@app.route("/cc")
async def cookieclicker(req):
    return response.html(await template.render_template(req, "cc.html"))
