import sys
import json
from app import app
from models.marker import Marker
from extensions import db
from datetime import datetime
from flask import jsonify



def index():
    markers = Marker.query.all()
    return jsonify(markers)  


def store(request):
    position = json.loads(request.data.decode('utf-8'))['position']
    try:
        newMarker = Marker(lat=position['lat'], lng=position['lng'], created_at=datetime.now())
        with app.app_context():
            db.session.add(newMarker)
            db.session.commit()
        return jsonify(newMarker)
    except Exception as inst:
        print('Sth went wrong', file=sys.stderr)
        print(type(inst), file=sys.stderr) # the exception instance
        print(inst.args, file=sys.stderr) # arguments stored in .args
        print(inst, file=sys.stderr)
        return "failed"

def delete(id):
    # delete specific marker
    pass