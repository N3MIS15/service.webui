import os
import xbmcaddon
from flask import Flask

__addonpath__ = xbmcaddon.Addon(id='script.webui').getAddonInfo('path')
app = Flask(__name__)

app.root_path     = __addonpath__
app.static_path   = '/static'
app.static_folder = os.path.join(__addonpath__, 'resources', 'static')
app.template_folder   = os.path.join(__addonpath__, 'resources', 'templates')
app.add_url_rule(app.static_path + '/<path:filename>', endpoint='static', view_func=app.send_static_file)

from jinja2 import FileSystemLoader
app.jinja_loader = FileSystemLoader(os.path.join(__addonpath__, 'resources', 'templates'))