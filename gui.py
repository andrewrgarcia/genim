from flaskwebgui import FlaskUI
import utils
from main import app

# Created by ScillFury(scillfury@gmail.com)
FlaskUI(server='flask', app= app, fullscreen=True, port=1234,).run()
# FlaskUI(server='flask', app=app, fullscreen=True, port=1234, browser_path='/usr/bin/firefox').run()