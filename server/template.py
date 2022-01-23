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

from jinja2 import FileSystemLoader, Environment
from markupsafe import Markup
from server import counter


def include_file(name):
    return Markup(loader.get_source(env, name)[0])

def getcss(path: str):
    return "<style>" + open(f"web/static/user_scripts/{path}.css", "r").read() + "</style>"

templates_dir = 'web/'

loader = FileSystemLoader(searchpath=templates_dir)
env = Environment(loader=loader, enable_async=True)
env.globals['include_file'] = include_file
env.globals['getcss'] = getcss
env.globals['counter'] = counter

async def render_template(request, file_name, **kwargs):
    template = env.get_template(file_name)

    context = {
        'request': request
    }
    rendered_template = await template.render_async(context, **kwargs)
    return rendered_template

