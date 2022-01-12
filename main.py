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
from email.utils import format_datetime
from datetime import datetime, timedelta
#from sanic_compress import Compress

app = Sanic("Schoology")
#Compress(app)

app.static("/", "./web")
compressed = lambda : "<style>" + open("web/static/user_scripts/main.css", "r").read() + "</style>"
compressed_fonts = "<style>" + open("web/static/user_scripts/fontscompressed.css", "r").read() + "</style>"
pages = [
    "slope",
    "ducklife",
    "ducklifespace",
    "getawayshootout",
    "launcher",
    "ducklifetreasure"
]


@app.route("/")
async def index(req):
    return response.html(
        open("web/index.html", "r").read().replace('<link rel="stylesheet" href="static/user_scripts/main.css">', compressed())\
        .replace('<link href="https://fonts.googleapis.com/css2?family=Inconsolata:wght@500&family=Lato&family=Oswald&display=swap" rel="stylesheet" onload="this.media=\'all\'">', compressed_fonts)
        )

@app.route("/<path:" + "|".join(pages) + ">")
async def routes(req, path: str):
    return response.html(open(f"web/{path}.html", "r").read().replace('<link rel="stylesheet" href="static/user_scripts/main.css">', compressed())\
        .replace('<link href="https://fonts.googleapis.com/css2?family=Inconsolata:wght@500&family=Lato&family=Oswald&display=swap" rel="stylesheet">', compressed_fonts))

@app.route("/secretlinktotally")
async def discordlink(req):
    return response.redirect("https://womginx.arph.org/")


ssl = {
    "cert": "/etc/letsencrypt/live/schology.duckdns.org/fullchain.pem",
    "key": "/etc/letsencrypt/live/schology.duckdns.org/privkey.pem",
}

app.run(
    '0.0.0.0',
    443,
    ssl=ssl,
    debug=True
)

