from flask import Blueprint
from flask import request
from controllers.markerController import index, store

maps = Blueprint('maps', __name__)
@maps.route("/markers", methods=['GET'])
def get_markers():
  return index()


@maps.route("/markers", methods=['POST'])
def store_marker():
  return store(request)
