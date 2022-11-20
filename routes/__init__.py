from app import app
from .maps.routes import maps as maproutes

@app.route('/')
def index():
  return "Hello Willy."

app.register_blueprint(maproutes, url_prefix='/map')